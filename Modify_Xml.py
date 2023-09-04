from datetime import datetime

def TXT_to_List():
    file = open('Change_setting.txt', 'r')
    content = file.read()
    file.close()
    return content.splitlines()

DataList = TXT_to_List()
# print(Data)
# print(len(DataList)) #31

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
            value = data[More_List[2]+1:Less_List[3]]
            Tag_Value_List.append(value)
        else:
            print(f'More_List length:{len(More_List)} not equal Less_List length:{len(Less_List)}')
    return Tag_Name_List, Tag_Value_List

def Today():
    date_time = str(datetime.now())
    Month_Day = date_time[5:7]+date_time[8:10]
    Time = date_time[11:13]+date_time[14:16]
    return f"{Month_Day}_{Time}"


if __name__=='__main__':
    Tag_Name, Tag_Value = GetTagData()
    print(Tag_Name)
    print(Tag_Value)
