# 二進位補0
num='1011110011111111011110111111010111111111' 
one='0'
two='00'
three='000'
List=[]
if len(num)%4!=0:
    s=num.split()
    if len(num)%4==1:          
        s.insert(0,three)
    elif len(num)%4==2:
        s.insert(0,two)
    elif len(num)%4==3:
        s.insert(0,one)
    num=''.join(s)
print(f'二進位={num}') #補0後結果
# 反轉Num
for i in range(len(num)-1,-1,-1):
    List.append(num[i])
    # print(List)
res=''.join(List)    
# print(res, len(res)) #反轉num
# 將二進位分開並轉換成十進位
List2=[]
List3=[]
n=0 
ans=0
while n<len(res)/4: #n=10
    List2.append(res[0+4*n:0+4*(n+1)])
    for k in range(4):
        if List2[n][k]=='1':
            ans=2**k
        elif List2[n][k]=='0':
            ans=0
        List3.append(str(ans))
    # print(List3[4*n:4*(n+1)])
    n+=1
Decres=''.join(List3)
# print(Decres)
# 把分開的十進位加總,轉換成十六進位
x=0
List4=[]
while x<len(Decres)/4:
    Dres=int(Decres[4*x+0])+int(Decres[4*x+1])+int(Decres[4*x+2])+int(Decres[4*x+3])
    # print(Dres, type(Dres))
    if Dres<10:
        Dres=str(Dres)
    elif Dres==10:
        Dres='a'
    elif Dres==11:
        Dres='b'
    elif Dres==12:
        Dres='c'
    elif Dres==13:
        Dres='d'
    elif Dres==14:
        Dres='e'
    elif Dres==15:
        Dres='f'
    # print(Dres, type(Dres))
    List4.append(Dres)    
    x+=1
List4.reverse()
hex=''.join(List4)
print(f'十六進位={hex}')

