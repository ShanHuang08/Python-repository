<<<<<<< HEAD
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
# 因为url的r.text是个json数据，所以要json.loads(),才能把json格式转为python识别的格式。
import json
jdata=json.loads(data)
# print(jdata)

for clist in jdata:
    # print(clist['a04'])
    covid=[]
    covid.append(clist['a04'])
    covid.append(clist['a06'])
    covid.append(clist['a05'])
    covid.append(clist['a09'])
    covid.append(clist['a12'])
    ws.append(covid)

# a04":"日期","a05":"總確診數","a06":"新增確診數","a09":"新增確診數/百萬", 
# "a12":"新聞稿發佈新增確診數", 
wb.save('covid.xlsx')
=======
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
# 因为url的r.text是个json数据，所以要json.loads(),才能把json格式转为python识别的格式。
import json
jdata=json.loads(data)
# print(jdata)

for clist in jdata:
    # print(clist['a04'])
    covid=[]
    covid.append(clist['a04'])
    covid.append(clist['a06'])
    covid.append(clist['a05'])
    covid.append(clist['a09'])
    covid.append(clist['a12'])
    ws.append(covid)

# a04":"日期","a05":"總確診數","a06":"新增確診數","a09":"新增確診數/百萬", 
# "a12":"新聞稿發佈新增確診數", 
wb.save('covid.xlsx')
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
