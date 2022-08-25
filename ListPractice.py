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
# print(jdata[0][1:178]) #237
# print(jdata[0][179:356]) #236

# for i in range(20,30):
#     count=0
#     if jdata[0][90*i] in ['0','1','2','3','4','5','6','7','8','9']:
#         count+=1
#     else:
#         count=0
#     print(jdata[0][1+178*i:178*(i+1)+count])

for i in range(20,23):
    print(jdata[0][1+178*i:178*(i+1)])

print(jdata[0][1+178*20:178*21])
print(jdata[0][1+178*21:178*22+2])
print(jdata[0][1+178*22+2:178*23+2])
    


# print(len(jdata[0])) #len=44567


# a04":"日期","a05":"總確診數","a06":"新增確診數","a09":"新增確診數/百萬", 
# "a12":"新聞稿發佈新增確診數", 
# wb.save('covid.xlsx')
