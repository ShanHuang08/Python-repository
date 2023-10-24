
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook

PATH='C:/Users/Shan/Workspace2/chromedriver.exe'
options=Options()
options.add_argument('--headless') 
url='https://www.google.com'

def Google_Mutiple_pages_title():
    keyword=input('Google搜尋關鍵字= ')
    pages=int(input('要搜尋幾頁(整數)? '))
    
    wb=Workbook()
    ws=wb.active
    ws.append(['連結','標題'])
    
    browser=webdriver.Chrome(PATH, options=options)
    browser.get(url)
    browser.find_element(By.XPATH, value='//input[@name="q"]').send_keys(keyword, Keys.RETURN)

    i=1
    while i<=pages:
        print('page='+str(i))
        titles=browser.find_elements(By.XPATH, value='//h3[@class="LC20lb MBeuO DKV0Md"]')
        titles_link=browser.find_elements(By.XPATH, value='//div[@class="yuRUbf"]/a')
        # browser.find_element(By.XPATH, '//button[text()="Some text"]')
        # cite=browser.find_elements(By.XPATH, value='//div[@class="TbwUpd NJjxre"]/cite')
        
        GetLink=[]
        for link in titles_link:
            # GetLink=[]
            links=link.get_attribute('href')
            GetLink.append(links)
            # GetLink.append(link.text) #會取到<cite>text
            # print(f'GetLink[]= {GetLink}')
            # ws.append(GetLink)
        
        GetTitle=[]
        for title in titles:
            GetTitle.append(title.text)
       
        # GetTitle[]加到GetLink[]
        k=0
        while k<len(GetTitle):
            GetLink.insert(1+2*k,GetTitle[k])
            k+=1 

        # 陣列分開輸出
        m=0
        while m<len(GetLink)/2:
            res=[]
            res.append(GetLink[0+2*m])
            res.append(GetLink[1+2*m])
            # print(res)
            ws.append(res)
            m+=1

        i+=1
        if i <= pages:
            NextPage=browser.find_element(By.XPATH, value='//span[@style="display:block;margin-left:53px"]').click()
        else:
            break

    wb.save('GoogleSearch.xlsx')
    time.sleep(3)
    browser.close()

def Google_Keywords_search():
    keyword_list=[]
    i=1
    keyword_times=int(input('請問要搜尋幾個關鍵字(整數)? '))
    while i<=keyword_times:
        keyword_input=input('第'+str(i)+'個關鍵字= ')
        keyword_list.append(keyword_input)
        i+=1
    
    browser=webdriver.Chrome(PATH)
 
    for j in range(len(keyword_list)):
        browser.get(url)
        search_input=browser.find_element(By.XPATH, value='//input[@class="gLFyf gsfi"]').send_keys(keyword_list[j], Keys.RETURN)
        titles=browser.find_elements(By.XPATH, value='//h3[@class="LC20lb MBeuO DKV0Md"]')
        # print('i='+str(i))
        print(keyword_list[j])
        for title in titles:   
            print(title.text)

    time.sleep(5)
    browser.close()

def mathods():
    Google_Mutiple_pages_title()
    Google_Keywords_search()

Google_Mutiple_pages_title()