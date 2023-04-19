import requests
import json
from BE_InfoControl import Webchannel, Webbranch
balance=[]
channel=Webchannel()
branch=Webbranch()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    #cookie要手動更新
    'cookie':'Hm_lvt_ca4875a2d78d98cace56a96514e152a8=1667876186; popupBillboard=2020-10-30 16:53:47; quick_ui_right=1; quick_ui_left=1; setCookie=1667876198605; .xy-web=MTY2Nzg3NjE5OHw2OU40YzM3Z0VSZzZIUkMwMlc3dFJ0cnh5WEw5YTQxU3AzTHRBZ0c4eWhmRWpwSFU2T2dtTm9GdDByTkV0TEl5d1N1RVVLN1dFRlFKY3JtSXVPWFR0X05UZlZjRG1lcXItUzNPSGU4Qi1UVkUwcDRiNHlKQkxLODdSUUVnaS1xTTFsSVpwNlJRUmZyVEhJMjFBXzVuXzBLeThUbzFhUWRnS0lwRVY5U2ZqNEJzYkd3eU9iNkxFcTRrdG1YZGZPZDZFSTYxV0lCNDZpaF9Pa29XZ19iMVlhYUNWN0hkTE83SVdyWHlYYWg5cDhHaVQyQjJRekk9fN0J4wE3nwmqWGaO0QUgKe1XvwIwWC_CJnbt3bcdbhqk; has_check_passwd=1; Hm_lpvt_ca4875a2d78d98cace56a96514e152a8=1667876257; referer=MTY2Nzg3NjI2N3xIdDdTdUtNTGlYeVJQUk5hVXBrOXhPUERYY3RBVndQSGhFVGdZTFlzUjFwSThXU0dqSG5aWE1ORjRkNWtMY0hoSU56QXZmOEJMckNVemM2b0c3R0RucXJSMnBCUny42ZOm8MWZnuDhaVdBJe2XnptiFm-Yc6IjxK4clJAopg==',
}

url = 'https://'+channel+'-web-'+branch+'.paradise-soft.com.tw/apis/my/wallet/balance?&_=1667876257062'
data=requests.get(url, headers=headers).text
# print(len(data)) #<class 'str'> len=2361
jdata=json.loads(data)
# print(len(jdata)) #<class 'list'> len=22

for i in range(len(jdata)):
    balance.append(jdata[i]['walletname']+'('+jdata[i]['walletcode']+'):'+str(jdata[i]['balance']))

print('品牌='+channel+' '+branch+', 帳號:'+jdata[0]['memberlogin'])
print('---------------')
for i in range(len(balance)):
    print(balance[i])


