from datetime import datetime
from xml.etree import ElementTree

FileName = 'Change_setting.txt'
def TXT_to_List():
    file = open(FileName, 'r')
    content = file.read()
    file.close()
    return content.splitlines()

DataList = TXT_to_List()

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

def Today():
    date_time = str(datetime.now())
    Month_Day = date_time[5:7]+date_time[8:10]
    Time = date_time[11:13]+date_time[14:16]
    return f"{Month_Day}_{Time}"


tree = ElementTree.parse("D:\\Old\H13SRD-F\\01.01.05\\bmccfg_0712_1558.xml")
root = tree.getroot()
# print(root.tag)

List= ['BoardMfgDateTime', 'BoardSerialNum', 'ProductSerialNum', 'BitRate', 'RetryTime', 'SSH', 'HTTP']
for i in List:
    for child in root.iter(i):
        print(child.tag, child.text, child.attrib)

# 出現兩次的Element, 第一次的value是Enable or Disable, 可以先用這個做判斷 (由上到下)
# 支援Xpath

# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://hackmd.io/@top30339/rJYlKYpml?type=view

if __name__=='__main__':
    # Tag_Name, Tag_Value = GetTagData()
    # for i in range(len(Tag_Name)):
    #     print(f'{Tag_Name[i]} : {Tag_Value[i]}')
    pass

