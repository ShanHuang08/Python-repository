from ast import keyword
from openpyxl import Workbook
from selenium.webdriver import Chrome
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
PATH='C:/Users/Shan/Workspace2/chromedriver.exe'
url='https://www.bing.com/'
# options=Options()
# options.add_argument('--headless')
# browser=Chrome(PATH,options=options)
browser=Chrome(PATH)
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
    i+=1 
    if i<=pages:
        browser.find_element(By.XPATH,value='//a[@title="下一頁"]').click()
    else:
        break    

wb.save('GoogleSearch.xlsx')
time.sleep(5)
browser.close()


