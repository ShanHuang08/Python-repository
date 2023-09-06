from datetime import datetime
from xml.etree import ElementTree

Change_FileName = 'Change_setting.txt'
Ori_xml = "D:\\Old\H13SRD-F\\01.01.05\\bmccfg_0712_1558.xml"

def Modify_Name():
    date_time = str(datetime.now())
    Month_Day = date_time[5:7]+date_time[8:10]
    Time = date_time[11:13]+date_time[14:16]
    num = Ori_xml.index('b')
    New_Name = Ori_xml[num:-14]+'_'+f"{Month_Day}_{Time}"+'.xml'
    return New_Name

def Check_Name():
    if New_XMLName[0:3] in ['bmc', 'bio']:
        return True
    else:
        print(f'File name error! {New_XMLName}')
        return False

def TXT_to_List():
    file = open(Change_FileName, 'r')
    content = file.read()
    file.close()
    return content.splitlines()


def GetTagData():
    # 1.算出<跟>的index, 用來定位tag Name')
    Tag_Name_List = []
    Tag_Value_List = []
    for data in DataList:
        Start_Pos = data.index('<')
        End_Pos = data.index('>')
        # print(data[Start_Pos+1:End_Pos])
        Tag_Name = data[Start_Pos+1:End_Pos]
        Tag_Name_List.append(Tag_Name)
    # 2.算出第三個">"跟第四個"<"的index, 用來定位tag value
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
            # print(data[More_List[2]+1:Less_List[3]])
            Tag_Value = data[More_List[2]+1:Less_List[3]]
            Tag_Value_List.append(Tag_Value)
        else:
            print(f'More_List length:{len(More_List)} not equal Less_List length:{len(Less_List)}')
    return Tag_Name_List, Tag_Value_List


def Modify_test():
    # TagName = ['BoardMfgDateTime', 'BoardSerialNum', 'ProductSerialNum', 'BitRate', 'RetryTime', 'SSH', 'HTTP']
    # TagValue = ['BDT_test','BS_test','PS_test','12345','5','223','82']
    tree = ElementTree.parse(Ori_xml)
    # tree = ElementTree.parse('test.xml')
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
                    elif TagValue[i] in ['Enable', 'Disable'] and child.text == TagValue[i]:
                        print(f'{child.text} == {TagValue[i]}, {TagName[i]}不用更新')
                else:
                    if TagValue[i] in ['Enable', 'Disable']:
                        print(f'{child.text} != {TagValue[i]}, {TagName[i]}不用更新')
                    elif child.text != TagValue[i]:    
                        print(f'{child.text} != {TagValue[i]}, {TagName[i]} 更新第二個')
                    else:
                        print(f'{child.text} == {TagValue[i]}, {TagName[i]}不用更新')
                # 2.<User UserID="2"> <User UserID="3">, 下面子節點全部一樣, 先get參數的值, 再去查看下一層的child.text, 修改text
        else:
            print(f'{TagName[i]} 不重複--------------------')
            for child in root.iter(TagName[i]):
                print(f'{child.text} != {TagValue[i]}, 更新{TagName[i]}')
# 支援Xpath
# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://hackmd.io/@top30339/rJYlKYpml?type=view

if __name__=='__main__':
    DataList = TXT_to_List()
    TagName, TagValue = GetTagData()
    New_XMLName = Modify_Name()
    # for i in range(len(Tag_Name)):
    #     print(f'{Tag_Name[i]} : {Tag_Value[i]}')
    if Check_Name():
        Modify_test()