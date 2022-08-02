#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def Login(url,browser):
    browser.get(url)
    browser.maximize_window()
    browser.find_element(By.ID,value='login').send_keys('a')
    browser.find_element(By.ID,value='password').send_keys('a')
    browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
    time.sleep(1)
    browser.find_element(By.XPATH,value='//button[contains(text(),"OK")]').click()
    browser.get('https://')
    time.sleep(1)

# 新增公司入款
def WireTransfer(browser):
    browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
    browser.find_element(By.CLASS_NAME,value='form-control').send_keys('公司')
    DepositType=browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
    DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="0"]').click() #公司入款radio
    # 每次入款
    browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('15')

    MemberType=browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
    # 保存
    browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()

def OnlineTransfer(browser):
    browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
    browser.find_element(By.CLASS_NAME,value='form-control').send_keys('在線')
    DepositType=browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
    DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click() #在線入款radio

    # 每次入款
    browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('10')

    MemberType=browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
    # 保存
    browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()

def VirtualTransfer(browser):
    browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
    browser.find_element(By.CLASS_NAME,value='form-control').send_keys('虛擬幣')
    DepositType=browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
    DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="3"]').click() #虛擬幣入款radio

    # 每次入款
    browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
    browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('20')

    MemberType=browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
    MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
    # 保存
    browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()

def main():
    PATH='./chromedriver.exe'
    url=''
    browser=webdriver.Chrome(PATH)
    Login(url,browser)
    WireTransfer(browser)
    browser.implicitly_wait(3)
    OnlineTransfer(browser)
    browser.implicitly_wait(3)
    VirtualTransfer(browser)
    time.sleep(20)
    browser.quit()
main()


