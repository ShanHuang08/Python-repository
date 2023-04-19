<<<<<<< HEAD
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook

SelectBrowser='Chrome'
if SelectBrowser=='Chrome':
    PATH='./chromedriver.exe'
    browser=webdriver.Chrome(PATH)
elif SelectBrowser=='Edge':
    PATH='./msedgedriver.exe'
    browser=webdriver.Edge(PATH)

wb=Workbook()
ws=wb.active
ws.title='小狗資訊'
ws.append(['動物編號','入園日期','品種','性別','來源地點'])

url='https://taw.tycg.gov.tw/X16_FResults.aspx'
browser.get(url)

element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(((By.ID,'ddlCategory'))
))
Category=browser.find_element_by_id('ddlCategory').click()
browser.find_element(By.XPATH,value='//option[@value="1"]').click()
browser.find_element_by_id('btnSearch').click()

i=1
while i<5:
    time.sleep(1) #To solve Message: stale element reference: element is not attached to the page document
    DogList=browser.find_elements(By.XPATH,value='//div[@style="padding: 9px; color: #333;"]/h5')
    List=[]
    for dogs in DogList:
        List.append(dogs.text)
    # print(len(List))

        #字串分割
    j=0
    while j<len(List)/5:
        List2=[]
        # print(j)
        List2.append(List[0+5*j][5:])
        List2.append(List[1+5*j][5:])
        List2.append(List[3+5*j][5:])
        List2.append(List[4+5*j][5:])
        List2.append(List[2+5*j][5:])
        ws.append(List2)
        j+=1
        
    time.sleep(1)
    browser.find_element(By.XPATH,value='//a[contains(text(),"»")]').click()
    i+=1

wb.save('Dogs.xlsx')
time.sleep(5)
browser.quit()
=======
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook

SelectBrowser='Chrome'
if SelectBrowser=='Chrome':
    PATH='./chromedriver.exe'
    browser=webdriver.Chrome(PATH)
elif SelectBrowser=='Edge':
    PATH='./msedgedriver.exe'
    browser=webdriver.Edge(PATH)

wb=Workbook()
ws=wb.active
ws.title='小狗資訊'
ws.append(['動物編號','入園日期','品種','性別','來源地點'])

url='https://taw.tycg.gov.tw/X16_FResults.aspx'
browser.get(url)

element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(((By.ID,'ddlCategory'))
))
Category=browser.find_element_by_id('ddlCategory').click()
browser.find_element(By.XPATH,value='//option[@value="1"]').click()
browser.find_element_by_id('btnSearch').click()

i=1
while i<5:
    time.sleep(1) #To solve Message: stale element reference: element is not attached to the page document
    DogList=browser.find_elements(By.XPATH,value='//div[@style="padding: 9px; color: #333;"]/h5')
    List=[]
    for dogs in DogList:
        List.append(dogs.text)
    # print(len(List))

        #字串分割
    j=0
    while j<len(List)/5:
        List2=[]
        # print(j)
        List2.append(List[0+5*j][5:])
        List2.append(List[1+5*j][5:])
        List2.append(List[3+5*j][5:])
        List2.append(List[4+5*j][5:])
        List2.append(List[2+5*j][5:])
        ws.append(List2)
        j+=1
        
    time.sleep(1)
    browser.find_element(By.XPATH,value='//a[contains(text(),"»")]').click()
    i+=1

wb.save('Dogs.xlsx')
time.sleep(5)
browser.quit()
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
