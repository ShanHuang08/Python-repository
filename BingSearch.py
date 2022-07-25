from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
wb=Workbook()
ws=wb.create_sheet('Bing')
# ws.title='Bing'
ws.append(['連結','標題'])
keywords='測'
pages=5
# PATH='C:/Users/shan_huang/Python/chromedriver.exe'
PATH='C:/Users/shan_huang/Python/msedgedriver.exe'
url='https://www.bing.com/'
# options=Options()
# options.add_argument('--headless')
# browser=webdriver.Edge(PATH,options=options)
# browser=webdriver.Chrome(PATH)
browser=webdriver.Edge(PATH)
browser.get(url)
browser.find_element(By.XPATH,value='//input[@name="q"]').send_keys(keywords,Keys.RETURN)

# selenium.common.exceptions.WebDriverException: Message: unknown error: cannot determine loading status
# from unknown error: unexpected command response
#   (Session info: chrome=103.0.5060.114)
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

    if i==1: #點擊稍後在說
        time.sleep(1)
        browser.find_element(By.XPATH,value='//span[@id="bnp_hfly_cta2"]').click()

    i+=1
    if i<=pages:
        browser.find_element(By.XPATH,value='//a[@title="下一頁"]').click()
    else:
        break    

wb.save('GoogleSearch.xlsx')
time.sleep(5)
browser.close()

