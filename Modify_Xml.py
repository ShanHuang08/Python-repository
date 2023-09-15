from datetime import datetime
# from xml.etree import ElementTree
from lxml import etree

Change_FileName = 'BMC_Change.txt'
Ori_xml = r'D:\Old\H13SRD-F\01.01.05\bmccfg_0712_1558.xml'


def TXT_to_List():
    file = open(Change_FileName, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content.splitlines()

def Modify_Name():
    date_time = datetime.now().strftime("%m%d_%H%M")
    file_name = Ori_xml.split('\\')[-1] #取最後一個斜線
    prefix = file_name[:6]
    # print(date_time)
    if prefix.startswith('bmc'):
        prefix = file_name[:6] # 取文件名前六個字符
        return f'{date_time.replace(date_time, f"{prefix}_{date_time}.xml")}'
    elif prefix.startswith('bios'):
        prefix = file_name[:7]
        return f'{date_time.replace(date_time, f"{prefix}_{date_time}.xml")}'
    else:
        print(f'File name error! {prefix}_{date_time}.xml')
    
# 根據txt檔案內容判斷要執行哪一種方法
def WhichData():
    result = []
    for check in DataList:
        if "Menu" not in check:
            result.append('BMC')
        else:
            result.append('Bios') 
    if "Bios" not in result:
        return GetBMCTagData()
    else:
        return GetBiosTagData()

def GetBMCTagData():
    First_filter = []
    for filter in DataList:
        if "Setting" in filter:
            First_filter.append(filter)
    # 1.算出<跟>的index, 用來定位tag Name')
    Tag_Name_List = []
    Tag_Value_List = []
    for data in First_filter:
        Start_Pos = data.index('<')
        End_Pos = data.index('>')
        # print(data[Start_Pos+1:End_Pos])
        Tag_Name = data[Start_Pos+1:End_Pos]
        Tag_Name_List.append(Tag_Name)
    # 2.算出 倒數第二個">"到最後一個"<"的index, 用來定位tag value, <![CDATA[]]>要用倒數第三個">"到最後一個"<"的index  
        More_List = []
        for i in range(len(data)):
            if data[i] == '>':
                More_List.append(i)
        # print(More_List) #len=4

        Less_List = []
        for i in range(len(data)):
            if data[i] == '<':
                Less_List.append(i)
        # print(Less_List) #len=4
        if len(More_List) == len(Less_List):
            # if Tag_Name == 'RemoteUser' or Tag_Name == 'RemoteGroup':
            if Tag_Name in ['RemoteUser', 'RemoteGroup', 'Name', 'Password']: #需要擴充, 不然會有例外
                # print(data[More_List[-3]+1:Less_List[-1]])
                Tag_Value = data[More_List[-3]+1:Less_List[-1]]
                Tag_Value_List.append(Tag_Value)
            else:
                Tag_Value = data[More_List[-2]+1:Less_List[-1]]
                Tag_Value_List.append(Tag_Value)
        else:
            print(f'More_List length:{len(More_List)} not equal Less_List length:{len(Less_List)}')
    # Tag_Name_List.append('child10')
    # Tag_Value_List.append('')
    if len(Tag_Name_List) == len(Tag_Value_List):
        return Tag_Name_List, Tag_Value_List
    else:
        return print(f"Length of tag name and tag value aren't equal {Tag_Name_List} != {Tag_Value_List}" )

def GetBiosTagData():
    First_filter = []
    for filter in DataList:
        # print(len(filter))
        if len(filter) > 19 and 'Menu' not in filter:
            First_filter.append(filter)
    Tag_Data = []
    Change_Data = []
    for filter in First_filter:
        if 'change' not in filter:
            Tag_Data.append(filter)
        else:
            Change_Data.append(filter)    
    
    Tag_Name_List = []
    Tag_Value_List = []
    for data in Tag_Data:   
        Tag_Pos = []    
        for i in range(len(data)):
            if data[i] =='"':
                Tag_Pos.append(i)
        # print(Tag_Pos)
        Tag_Name = data[Tag_Pos[0]+1:Tag_Pos[1]]
        # print(Tag_Name[0:11])
        if Tag_Name[0:11] != 'Boot Option':
            Tag_Name_List.append(Tag_Name)
        else:
            Tag_Name = data[Tag_Pos[0]+1:Tag_Pos[3]]
            Tag_Name_List.append(Tag_Name)

    for data in Change_Data:
        Value_Pos = []
        for i in range(len(data)):
            if data[i] == '"':
                Value_Pos.append(i)
        # print(Value_Pos)
        Tag_Value = data[Value_Pos[2]+1:Value_Pos[3]]
        # print(Tag_Value)
        Tag_Value_List.append(Tag_Value)

    if len(Tag_Name_List) == len(Tag_Value_List):
        return Tag_Name_List, Tag_Value_List
    else:
        print(f"Length of tag name and tag value aren't equal {Tag_Name_List} != {Tag_Value_List}" )


def Modify_test():
    tree = etree.parse(Ori_xml)
    # tree = ElementTree.parse('test.xml')
    # tree = etree.parse('test.xml')
    root = tree.getroot()
    # print(root.tag)
    
    for i in range(len(TagName)):
        count = 0
        for child in root.iter(TagName[i]):
            # print(child.tag, child.text) 
            count+=1
        if count > 1:
            print(f'{TagName[i]} 重複--------------------')
            for child in root.iter(TagName[i]):
                # 1.Tag value是Enable/Disable, 第二個value是數字
                if child.text in ['Enable', 'Disable']:
                    if TagValue[i] in ['Enable', 'Disable'] and child.text != TagValue[i]:
                        print(f'{child.text} != {TagValue[i]}, {TagName[i]} 更新第一個')
                        child.text = TagValue[i]
                    elif TagValue[i] in ['Enable', 'Disable'] and child.text == TagValue[i]:
                        print(f'{child.text} == {TagValue[i]}, {TagName[i]}不用更新')
                else:
                    if TagValue[i] in ['Enable', 'Disable']:
                        print(f'{child.text} != {TagValue[i]}, {TagName[i]}不用更新')
                    elif child.text != TagValue[i]:    
                        print(f'{child.text} != {TagValue[i]}, {TagName[i]} 更新第二個')
                        child.text = TagValue[i]
                    else:
                        print(f'{child.text} == {TagValue[i]}, {TagName[i]}不用更新')
                # 2.<User UserID="2"> <User UserID="3">, 下面子節點全部一樣, 先get參數的值, 再去查看下一層的child.text, 修改text
        else:
            print(f'{TagName[i]} 不重複--------------------')
            # Bios都不重複, 用是否有attribute來篩選
            for child in root.iter(TagName[i]):
                print(f'{child.text} != {TagValue[i]}, 更新{TagName[i]}')
                child.text = TagValue[i]
    
    tree.write(New_XMLName, encoding='utf-8', xml_declaration=True, pretty_print=True)
# 改用lxml工具可以保留註解
# https://lxml.de/tutorial.html
# https://imonce.github.io/2019/10/21/3%E5%B0%8F%E6%97%B6%E7%B2%BE%E9%80%9Alxml-etree-Python%E4%B8%ADxml%E7%9A%84%E8%AF%BB%E5%8F%96%E3%80%81%E8%A7%A3%E6%9E%90%E3%80%81%E7%94%9F%E6%88%90%E5%92%8C%E6%9F%A5%E6%89%BE/
# https://www.qiniu.com/qfans/qnso-40725428#comments

if __name__=='__main__':
    DataList = TXT_to_List()
    New_XMLName = Modify_Name()
    TagName, TagValue = WhichData()
    # for i in range(len(TagName)):
    #     print(f'{TagName[i]} : {TagValue[i]}')
    Modify_test()


# <Name> all
# <Password> all
# <CertFile/>
# <PrivKeyFile/>
# <HostName/>
# <Address/> 2nd