from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
wb=Workbook()
ws=wb.create_sheet('Bing')
# ws.title='Bing'
ws.append(['連結','標題'])
keywords='測'
pages=5
Browsers='edge'
if Browsers=='chrome':
    PATH='C:/Users/Shan/Workspace2/chromedriver.exe'
elif Browsers=='edge':
    PATH='C:/Users/Shan/Workspace2/msedgedriver.exe'
url='https://www.bing.com/'
# options=Options()
# options.add_argument('--headless')
# browser=webdriver.Edge(PATH,options=options)
# browser=webdriver.Chrome(PATH)
browser=webdriver.Edge(PATH)
browser.get(url)
browser.find_element(By.XPATH,value='//input[@name="q"]').send_keys(keywords,Keys.RETURN)

i=1
while i<=pages:
    print(f'pages={i}') 
    title=browser.find_elements(By.XPATH,value='//h2/a')

    for titles in title:
        GetContent=[]
        Links=titles.get_attribute('href')
        GetContent.append(Links)
        GetContent.append(titles.text)
        # print(GetContent)
        ws.append(GetContent)
    
    # notiContainer=browser.find_element(By.XPATH,value='//div[@id="b_notificationContainer_bop"]')
    #點擊稍後在說
    if EC.presence_of_element_located((By.ID,'b_notificationContainer_bop')) and i==1:
        time.sleep(1)
        browser.find_element(By.XPATH,value='//span[@id="bnp_hfly_cta2"]').click()
    else:
        pass
    
    i+=1
    if i<=pages:
        browser.find_element(By.XPATH,value='//a[@title="下一頁"]').click()
    else:
         break    

wb.save('GoogleSearch.xlsx')
time.sleep(5)
browser.close()
