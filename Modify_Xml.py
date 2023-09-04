def TXT_to_List():
    file = open('Change_setting.txt', 'r')
    content = file.read()
    # print(content)
    # print(type(content), len(content))
    file.close()
    Info_List = content.splitlines()
    return Info_List

Data = TXT_to_List()
# print(Data)
print(len(Data)) #31

content = '19:38:52.052    INFO            Setting: "<SSH>22</SSH>" to "<SSH>233</SSH>"'
content2 = '19:38:52.043    INFO            Setting: "<BoardMfgName>FruBM41</BoardMfgName>" to "<BoardMfgName>BM_1693481932</BoardMfgName>"'
print('1.算出<跟>的index, 可以定位tag Name')
Start_Pos = content.index('<') #42
# print(content[42:].index('<')) #0
End_Pos = Start_Pos + content[Start_Pos:].index('>') #4
End_Pos2 = Start_Pos + content2[Start_Pos:].index('>')
print(content[Start_Pos+1:End_Pos])
print(content2[Start_Pos+1:End_Pos2])



print('2.算出第三個">"跟第四個"<"的index, 可以定位tag value')

count = 0
List = []
for i in range(len(content)):
    if content[i] == '>':
        List.append(i)
        count+=1
print(f'"<" 出現{count}次')

List2 = []
count2 = 0
for i in range(len(content)):
    if content[i] == '<':
        List2.append(i)
        count2+=1
print(f'">" 出現{count2}次')


print(f'第{count-1}次 ">"  位於{List[(count-1)-1]}')
print(f'第{count2}次 "<"  位於{List2[(count2)-1]}')
print(content[65+1:69])
