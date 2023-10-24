#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from JenkinsLockStatus import LockStatus

SelectBrowser='Chrome'
if SelectBrowser=='Chrome':
    PATH='./chromedriver.exe'
    browser=webdriver.Chrome(PATH)
elif SelectBrowser=='Edge':
    PATH='./msedgedriver.exe'
    browser=webdriver.Edge(PATH)

url='https://jenkins.paradise-soft.com.tw/login'
browser.get(url)
browser.maximize_window()

browser.find_element_by_id('j_username').send_keys('shan_huang')
browser.find_element_by_name('j_password').send_keys('Dethl8889')
browser.find_element_by_name('Submit').click()
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(((By.ID,'projectstatus'))))
    
browser.get('https://jenkins.paradise-soft.com.tw/job/Deploy/job/UAT/job/DeployScript/job/00-Enable-Disable-Jobs-All/')
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(((By.XPATH,'//span[contains(text(),"Build with Parameters")]'))))
element.click()

# get disable info
BuildDetail=browser.find_element(By.XPATH,value='//tr[@class="build-row multi-line overflow-checked"]')
ProcessNO=BuildDetail.find_element(By.XPATH,value='//a[@update-parent-class=".build-row"]')
ProcessTime=BuildDetail.find_element(By.XPATH,value='//div[@class="pane build-details"]/a')
Status=BuildDetail.find_element(By.XPATH,value='//span[@style="padding:1px;border:1px solid #C0C000;margin:0px;background:#FFFF00;color:#000000"]')

Status2=Status.text 
if Status2[11:]=='false':
    browser.find_element_by_name('value').click()
    browser.find_element_by_id('yui-gen1-button').click()
    browser.refresh()
elif Status2[11:]=='true':
    browser.find_element_by_id('yui-gen1-button').click()
    browser.refresh()

time.sleep(5)
browser.quit()
LockStatus()