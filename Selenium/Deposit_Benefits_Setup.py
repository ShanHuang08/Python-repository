<<<<<<< HEAD
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BE_InfoControl import *

class BE_Deposit_Benefits_Setup():
    def __init__(self) -> None:
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.channel=Webchannel()
        self.branch=Webbranch()
        self.url='https://'+self.channel+'-admin-'+self.branch+'.paradise-soft.com.tw/'

    def AdminLogin(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.find_element(By.ID,value='login').send_keys(BE_account())
        self.browser.find_element(By.ID,value='password').send_keys(BE_password())
        if self.branch=='uat':
            self.browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
        elif self.branch=='stage':
            self.browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
        time.sleep(1)
        self.browser.get(self.url)
    
        # self.browser.find_element(By.XPATH,value='//button[contains(text(),"OK")]').click()
    
        self.browser.get(self.url+'discount/deposit')
        self.browser.implicitly_wait(1)

    # 新增公司入款優惠
    def WireTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('公司')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="0"]').click() #公司入款radio
        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('15')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)
    # 新增在線入款優惠
    def OnlineTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('在線')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click() #在線入款radio

        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('10')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)
    # 新增虛擬幣入款優惠
    def VirtualTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('虛擬幣')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="3"]').click() #在線入款radio

        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('20')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)

    def FeeSetup(self):
        self.browser.get(self.url+'/fee')
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: withdrawcharge"]').clear()
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: withdrawcharge"]').send_keys('1',Keys.RETURN)
        # 保存
        # browser.find_element(By.XPATH,value='//div[@class="col-md-offset-2"]/button[@data-bind="click: submit"]').click()
        self.browser.get(self.url+'/merchant')
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//*[@id="tab_inout_0"]/div/table/tbody/tr[1]/td[11]/a[1]').click()   
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: charge"]').clear()
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: charge"]').send_keys('1',Keys.RETURN)
        time.sleep(5)
        self.browser.quit()


if __name__=='__main__':
    # 上分優惠設定
    BE_Deposit_Benefits_Setup.AdminLogin()
    BE_Deposit_Benefits_Setup.WireTransfer()
    BE_Deposit_Benefits_Setup.OnlineTransfer()
    BE_Deposit_Benefits_Setup.VirtualTransfer()
    # 手續費設定
    BE_Deposit_Benefits_Setup.FeeSetup()

=======
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BE_InfoControl import *

class BE_Deposit_Benefits_Setup():
    def __init__(self) -> None:
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.channel=Webchannel()
        self.branch=Webbranch()
        self.url='https://'+self.channel+'-admin-'+self.branch+'.paradise-soft.com.tw/'

    def AdminLogin(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.find_element(By.ID,value='login').send_keys(BE_account())
        self.browser.find_element(By.ID,value='password').send_keys(BE_password())
        if self.branch=='uat':
            self.browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
        elif self.branch=='stage':
            self.browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
        time.sleep(1)
        self.browser.get(self.url)
    
        # self.browser.find_element(By.XPATH,value='//button[contains(text(),"OK")]').click()
    
        self.browser.get(self.url+'discount/deposit')
        self.browser.implicitly_wait(1)

    # 新增公司入款優惠
    def WireTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('公司')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="0"]').click() #公司入款radio
        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('15')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)
    # 新增在線入款優惠
    def OnlineTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('在線')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click() #在線入款radio

        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('10')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)
    # 新增虛擬幣入款優惠
    def VirtualTransfer(self):
        self.browser.find_element(By.XPATH,value='//a[@class="btn btn-default btn-sm"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(((By.CLASS_NAME,'col-md-12'))))
        self.browser.find_element(By.CLASS_NAME,value='form-control').send_keys('虛擬幣')
        DepositType=self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]')
        DepositType.find_element(By.XPATH,value='//div[@data-bind="validationElement: deposittype"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="3"]').click() #在線入款radio

        # 每次入款
        self.browser.find_element(By.XPATH,value='//div[@data-bind="validationElement: depositwhen"]/div[@class="col-md-9"]/label[@class="radio-inline"]/input[@value="1"]').click()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: fromamount"]').send_keys('100')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: toamount"]').send_keys('1000')
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').clear()
        self.browser.find_element(By.XPATH,value='//input[@data-bind="value: amount"]').send_keys('20')

        MemberType=self.browser.find_element(By.XPATH,value='//div[@class="col-md-8"]')
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="1"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="2"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="3"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="4"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="5"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="6"]').click()
        MemberType.find_element(By.XPATH,value='//label[@class="checkbox-inline  text-control"]/input[@value="7"]').click()
        # 保存
        self.browser.find_element(By.XPATH,value='//button[@data-bind="click: submit"]').click()
        self.browser.implicitly_wait(3)

    def FeeSetup(self):
        self.browser.get(self.url+'/fee')
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: withdrawcharge"]').clear()
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: withdrawcharge"]').send_keys('1',Keys.RETURN)
        # 保存
        # browser.find_element(By.XPATH,value='//div[@class="col-md-offset-2"]/button[@data-bind="click: submit"]').click()
        self.browser.get(self.url+'/merchant')
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//*[@id="tab_inout_0"]/div/table/tbody/tr[1]/td[11]/a[1]').click()   
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: charge"]').clear()
        self.browser.find_element(By.XPATH,value='//div[@class="input-group"]/input[@data-bind="value: charge"]').send_keys('1',Keys.RETURN)
        time.sleep(5)
        self.browser.quit()


if __name__=='__main__':
    # 上分優惠設定
    BE_Deposit_Benefits_Setup.AdminLogin()
    BE_Deposit_Benefits_Setup.WireTransfer()
    BE_Deposit_Benefits_Setup.OnlineTransfer()
    BE_Deposit_Benefits_Setup.VirtualTransfer()
    # 手續費設定
    BE_Deposit_Benefits_Setup.FeeSetup()

>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
