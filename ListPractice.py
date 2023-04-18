import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

Title = ['日期','新增確診數','總確診數','新增確診數/百萬','新聞稿發佈新增確診數' ]
ws.append(Title)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4051&limited=TWN'
r=requests.get(url, headers=headers)
# print(r.text)
data=r.text
jdata=[]
jdata.append(data)
# print(jdata[0][0]) #len=1
# print(jdata[0][1:12]) #id
# print(jdata[0][12:24]) #a01
# print(jdata[0][24:35]) #a02
# print(jdata[0][35:46]) #a03
# print(jdata[0][46:65]) #a04
# print(jdata[0][65:79]) #a05
# print(jdata[0][79:90]) #"a06":"新增確診數"
# print(jdata[0][90:105]) #a07
# print(jdata[0][105:121]) #a08
# print(jdata[0][121:135]) #a09
# print(jdata[0][135:149]) #a10
# print(jdata[0][149:166]) #a11
# print(jdata[0][166:178-1]) #"a12":"新聞稿發佈新增確診數"

count=0
sum=0
num=0 #0-103 OK
Data_1st=[]
for i in range(0,100):
    b=True
    # a06
    if jdata[0][178*i+89+count] in ['0','1','2','3','4','5','6','7','8','9']:
        if jdata[0][178*i+89+count] in ['0','1','2','3','4','5','6','7','8','9']:
            count+=1
            b=False
            # print('a06:'+str(b)+' i='+str(i))
        elif jdata[0][178*i+89+count] in ['0','1','2','3','4','5','6','7','8','9'] and jdata[0][178*i+90+count] in ['0','1','2','3','4','5','6','7','8','9']:
            count+=2
            b==False
            # print('a06:'+str(b)+' i='+str(i))
        elif jdata[0][178*i+89+count] in ['0','1','2','3','4','5','6','7','8','9'] and jdata[0][178*i+90+count] in ['0','1','2','3','4','5','6','7','8','9'] and jdata[0][178*i+91+count] in ['0','1','2','3','4','5','6','7','8','9']:
            count+=3
            b==False
            # print('a06:'+str(b)+' i='+str(i))
    # a07 increase from i=82
    if jdata[0][178*i+104+count] in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
        b=False
        # print('a07:'+str(b)+' i='+str(i))
    # a08 increase from i=91
    if jdata[0][178*i+120+count] in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
        b=False
        # print('a08:'+str(b)+' i='+str(i))
    # a09
    if jdata[0][178*i+134+count] in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
        b=False
        # print('a09:'+str(b)+' i='+str(i))
    # a10 increase from i=93
    if jdata[0][178*i+148+count] in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
        b=False
        # print('a10:'+str(b)+' i='+str(i))
    # a12
    if jdata[0][178*i+176+count] in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
        b=False
        # print('a12:'+str(b)+' i='+str(i))

    if b and i>=num:
        # print(jdata[0][1+178*i+count:178*(i+1)+count])
        Data_1st.append(jdata[0][1+178*i+count:178*(i+1)+count])
    elif b==False and i>=num:
        if count==2:
            # print(jdata[0][1+178*i:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i:178*(i+1)+count])
        elif count>2 and count<=6:
            # print(jdata[0][1+178*i+count-2:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-2:178*(i+1)+count])
        elif count>6 and count<22:
            # print(jdata[0][1+178*i+count-3:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-3:178*(i+1)+count])
        elif count==22:
            # print(jdata[0][1+178*i+count-1:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-1:178*(i+1)+count])
        elif count>22 and count<30:
            # print(jdata[0][1+178*i+count-3:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-3:178*(i+1)+count])
        elif count==31:
            # print(jdata[0][1+178*i+count-3:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-3:178*(i+1)+count])
        elif count>35 and count<=41:
            # print(jdata[0][1+178*i+count-5:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-5:178*(i+1)+count])
        elif count>41 and count<=107:
            # print(jdata[0][1+178*i+count-6:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-6:178*(i+1)+count])
        elif count>107:
            # print(jdata[0][1+178*i+count-6:178*(i+1)+count])
            Data_1st.append(jdata[0][1+178*i+count-6:178*(i+1)+count])
    # print(f'count={count}')
    # j=len(jdata[0][178*i+count-6:178*(i+1)+count])
    # sum=sum+j
# print(sum) #len=18216
print(Data_1st)
print(len(Data_1st)) #len=100

# print(jdata[0][1+178*91+31:178*92+36]) 
# print(jdata[0][1+178*81+6:178*82+6]) 
# print(jdata[0][1+178*82+6:178*83+9]) #+6 +9
# print(jdata[0][1+178*83+9:178*84+12]) #+9 +12
# print(jdata[0][1+178*83+9:178*84+12]) #+9 +12


# x=103
# print(x,jdata[0][1+178*x+79+107:1+178*x+89+107]) #a06
# print(x,jdata[0][1+178*x+105+30:1+178*x+120+30]) #a08
# print(x+1,jdata[0][1+178*(x+1)+79+113:1+178*(x+1)+89+113])
# print(x+2,jdata[0][1+178*(x+2)+105+32:1+178*(x+2)+120+34])

# print(len(jdata[0])) #len=44567


# a04":"日期","a05":"總確診數","a06":"新增確診數","a09":"新增確診數/百萬", 
# "a12":"新聞稿發佈新增確診數", 
# wb.save('covid.xlsx')
