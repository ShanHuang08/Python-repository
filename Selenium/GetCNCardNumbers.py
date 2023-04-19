#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PATH='./chromedriver.exe'
options=Options()
options.add_argument('--headless')
# 谷歌FLoC技术：目的：为区分不同用户群体，更加精准的推送广告，谷歌启用了新的追踪技术FLoC（同类群组联合学习 Federated Learning of Cohorts）以替代 cookie。
# 反谷歌 FLoC 联盟添加响应头 permissions-policy: interest-cohort=(). 添加浏览器启动参数 --log-level=1 或 --log-level=2 忽略此错误
options.add_argument('--log-level=1')
options.add_argument('--log-level=2')
browser=webdriver.Chrome(PATH,options=options)
browser.get('https://ddu1222.github.io/bankcard-validator/bcBuilder.html')
browser.find_element(By.XPATH,value='//button[@onclick="getCards()"]').click()

cards=browser.find_elements(By.ID,value="cards")
AllData=[]
for card in cards:
    # print(card.text)
    AllData.append(card.text)
# print(type(AllData[0])) #len=1
test=AllData[0].split('\n') #len=20
CardNumber=[]
for i in range(len(test)):
    test2=test[i].split(',')
    # print(test2) #len=2
    CardNumber.append(test2[0])
# print(len(CardNumber)) #len=20

for i in range(len(CardNumber)//2):
    print(CardNumber[i])

browser,quit()