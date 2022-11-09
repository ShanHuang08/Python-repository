from bs4 import BeautifulSoup
import requests
import json
from BE_InfoControl import *
import time

# Brand_codes=MCA_Bankcodes()
Branch=Webbranch()
Login_url='https://bh-admin-uat.paradise-soft.com.tw/login'
Login_api='https://bh-admin-uat.paradise-soft.com.tw/apis/session'
Banks_url='https://bh-admin-uat.paradise-soft.com.tw/bank'
Banks_api='https://bh-admin-uat.paradise-soft.com.tw/apis/bank?code=&name=&status=-1&recommend=-1&pi=1&ps=500&po=&_=1667981702338'
payload={
    'login':'shan',
    'passwd':'shan612283',
    'otp':1
}
headers={
    'Connection': 'keep-alive',
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-TW,zh;q=0.9',
    'content-length':'35',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'origin':'https://bh-admin-uat.paradise-soft.com.tw',
    'referer':Banks_url,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
    'Cookie':''
}
session_requests = requests.session() #session()放到變數, 用同一個跑

Login=session_requests.post(Login_api, data=payload, headers=headers)
# print(Login.text) #有登入
time.sleep(1)

Banksinfo=session_requests.get(Banks_api).text
time.sleep(1)
print(Banksinfo) #有登入 沒抓到json

# jdata=json.loads(Banksinfo)
# print(jdata)
