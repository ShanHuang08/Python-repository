from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import time

wb=Workbook()

# Crash.Net scrape
ws=wb.active
ws.title='Crash.Net'
ws.append(['Crash.Net MotoGP News'])
ws.append(['時間','連結','標題'])

options=Options()
options.add_argument('--headless')
# FLoC permissions-policy: interest-cohort=().
options.add_argument('--log-level=1')
options.add_argument('--log-level=2')
browser=webdriver.Chrome('./chromedriver.exe',options=options)
browser.get('https://www.crash.net/motogp/news')

page=1
while page<=2:   
    CreatedTime=browser.find_elements(By.XPATH,value='//div[@class="views-field views-field-created"]/span[@class="field-content"]')
    Titles=browser.find_elements(By.XPATH,value='//*[@id="block-system-main"]/div/div/div[1]/div/div[@class="views-field views-field-title"]/span/a')

    Get_CreatedTime=[]
    for times in CreatedTime:
        Get_CreatedTime.append(times.text)

    Get_Links=[]
    Get_Titles=[]
    for i in Titles:
        Links=i.get_attribute('href')
        Get_Links.append(Links)
        Get_Titles.append(i.text)

    for i in range(len(Get_CreatedTime)):
        Result=[]
        Result.append(Get_CreatedTime[i])
        Result.append(Get_Links[i])
        Result.append(Get_Titles[i])
        ws.append(Result)
    if page<2:
        browser.get('https://www.crash.net/motogp/news?page=1')
    page+=1

# Motorsport
wb.create_sheet('Motorsport')
ws2=wb['Motorsport']
ws2.append(['Motorsport MotoGP News'])
ws2.append(['時間','連結','標題'])

browser.get('https://www.motorsport.com/motogp/news/')
CreatedTime2=browser.find_elements(By.XPATH,value='//time[@class="ms-item_date-value"]')
Title2_1st=browser.find_elements(By.XPATH,value='//*[@id="app_article_browse"]/div[4]/div[3]/div[3]/div/div[1]/div/div[3]/div[@class="ms-item--art "]/div[@class="ms-item_info"]/p/a')
Titles2_2nd=browser.find_elements(By.XPATH,value='//*[@id="app_article_browse"]/div[4]/div[3]/div[3]/div/div[1]/div/div[1]/div[@class="ms-item--art "]/div[@class="ms-item_info"]/p/a')

Get_CreatedTime2=[]
for times in CreatedTime2:
    Time=times.get_attribute('datetime')
    Get_CreatedTime2.append(times.text)
# print(len(Get_CreatedTime2))

Get_Links2=[]
for link in Title2_1st:
    Link=link.get_attribute('href')
    Get_Links2.append(Link)
for link in Titles2_2nd:
    Link=link.get_attribute('href')
    Get_Links2.append(Link)
# print(len(Get_Links2))

Get_Titles2=[]
for title in Title2_1st:
    Get_Titles2.append(title.text)
for title in Titles2_2nd:
    Get_Titles2.append(title.text)
# print(len(Get_Titles2))

for i in range(len(Get_CreatedTime2)):
    Result=[]
    Result.append(Get_CreatedTime2[i])
    Result.append(Get_Links2[i])
    Result.append(Get_Titles2[i])
    ws2.append(Result)

wb.save('test.xlsx')
# time.sleep(5)
browser.quit()