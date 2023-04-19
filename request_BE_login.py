<<<<<<< HEAD
import requests
import json
from BE_InfoControl import *
import time

# Brand_codes=MCA_Bankcodes()
# Channel=Webchannel()
# Branch=Webbranch()

Login_api='https://3h-admin-uat.paradise-soft.com.tw/apis/session'
Banks_api='https://3h-admin-uat.paradise-soft.com.tw/apis/bank?code=&name=&status=-1&recommend=-1&pi=1&ps=500'
payload={
    'login':'shanbot',
    'passwd':'shan612283',
    'otp':1
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}
session_requests = requests.session() #session()放到變數, 用同一個跑

Login=session_requests.post(Login_api, data=payload, headers=headers)
# print(Login.text) #有登入
time.sleep(1)
Banksinfo=session_requests.get(Banks_api, headers=headers).text
time.sleep(1)
print(Banksinfo) #有登入 沒抓到json

jdata=json.loads(Banksinfo)
# print(jdata)
=======
import requests
import json
from BE_InfoControl import *
import time

# Brand_codes=MCA_Bankcodes()
# Channel=Webchannel()
# Branch=Webbranch()

Login_api='https://3h-admin-uat.paradise-soft.com.tw/apis/session'
Banks_api='https://3h-admin-uat.paradise-soft.com.tw/apis/bank?code=&name=&status=-1&recommend=-1&pi=1&ps=500'
payload={
    'login':'shanbot',
    'passwd':'shan612283',
    'otp':1
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}
session_requests = requests.session() #session()放到變數, 用同一個跑

Login=session_requests.post(Login_api, data=payload, headers=headers)
# print(Login.text) #有登入
time.sleep(1)
Banksinfo=session_requests.get(Banks_api, headers=headers).text
time.sleep(1)
print(Banksinfo) #有登入 沒抓到json

jdata=json.loads(Banksinfo)
# print(jdata)
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
