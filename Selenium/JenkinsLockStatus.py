from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def LockStatus():
    options=Options() 
    options.add_argument('--headless') 
    SelectBrowser='Chrome'
    if SelectBrowser=='Chrome':
        PATH='./chromedriver.exe'
        browser=webdriver.Chrome(PATH,options=options)
    elif SelectBrowser=='Edge':
        PATH='./msedgedriver.exe'
        browser=webdriver.Edge(PATH,options=options)

    url='https://jenkins.paradise-soft.com.tw/login'
    browser.get(url)
    # browser.maximize_window()

    browser.find_element(By.ID,value='j_username').send_keys('shan_huang')
    browser.find_element(By.NAME,value='j_password').send_keys('Dethl8889')
    browser.find_element(By.NAME,value='Submit').click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(((By.ID,'projectstatus'))))

    browser.get('https://jenkins.paradise-soft.com.tw/job/Deploy/job/UAT/job/DeployScript/job/00-Enable-Disable-Jobs-All/')

    if browser.maximize_window():
        BuildDetail=browser.find_element(By.XPATH,value='//tr[@class="build-row multi-line overflow-checked"]') #Message: no such element: Unable to locate element:
    else:
        BuildDetail=browser.find_element(By.XPATH,value='//tr[@class="build-row single-line overflow-checked"]')
    ProcessNO=BuildDetail.find_element(By.XPATH,value='//a[@update-parent-class=".build-row"]')
    ProcessTime=BuildDetail.find_element(By.XPATH,value='//div[@class="pane build-details"]/a')
    Status=BuildDetail.find_element(By.XPATH,value='//span[@style="padding:1px;border:1px solid #C0C000;margin:0px;background:#FFFF00;color:#000000"]')
    Status2=Status.text
    print(ProcessNO.text,ProcessTime.text,Status.text)
    # print(Status2[11:])

    browser.quit()

if __name__=='__main__':
    LockStatus()