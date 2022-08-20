from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import time

wb=Workbook()

# Crash.Net scrape
ws=wb.active
ws.title='Crash.Net'
ws.append(['Created time','Link','Title'])

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
ws2.append(['Created time','Link','Title'])

wb.save('test.xlsx')
time.sleep(5)
browser.quit()