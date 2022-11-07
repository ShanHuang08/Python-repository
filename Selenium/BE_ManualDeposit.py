#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BE_InfoControl import *
class Manual_Deposit():
    def __init__(self) -> None:
        channel=Webchannel()
        branch=Webbranch()
        self.NewAccount=WebNewaccount()
        self.url='https://'+channel+'-admin-'+branch+'.paradise-soft.com.tw/'
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.amount=100
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.find_element(By.ID,value='login').send_keys(BE_account()) 
        self.browser.find_element(By.ID,value='password').send_keys(BE_password())
        if branch=='uat':
            self.browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
        elif branch=='stage':
            self.browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
        time.sleep(1)
        # browser.get(url+'v2/finance/deposit/man-deposit')
        self.browser.implicitly_wait(5)

    # 人工存入
    def ManualDeposit(self):
        self.browser.get(self.url+'v2/finance/deposit/man-deposit')
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(self.NewAccount)
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
        try:
            self.browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[2]').click() #按人工存入
        except:
            self.browser.find_element(By.XPATH,value='/html/body/div[8]/div[1]/div[1]/ul/li[2]').click()
        self.browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(self.amount-20))
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
        self.browser.implicitly_wait(2)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
        print(f'人工存入{self.amount-20}元')
        time.sleep(1)
        self.browser.quit()
        
    # 人工公司
    def WireDeposit(self):
        self.browser.get(self.url+'v2/finance/deposit/man-deposit')
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(self.NewAccount)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').send_keys(Keys.UP) #下拉選單往上按
        # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable ＂因為send_keys()沒有用在input element裡面＂
        try:
            self.browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[10]').click() #按人工公司入款
        except:
            self.browser.find_element(By.XPATH,value='/html/body/div[8]/div[1]/div[1]/ul/li[10]').click() #按人工公司入款
        self.browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(self.amount))
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')

        self.browser.find_element(By.XPATH,value='//div[@class="el-form-item account_numbers"]/div[@class="el-form-item__content"]/div[@class="el-select"]/div[@class="el-input el-input--suffix"]/input').click() #選擇銀行帳號
        self.browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇銀行帳號
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
        print(f'人工公司入款{self.amount}元')
        time.sleep(1)
        self.browser.quit()
        
    # 人工在線
    def OnlineDeposit(self):
        self.browser.get(self.url+'v2/finance/deposit/man-deposit')
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(self.NewAccount)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').send_keys(Keys.UP) #下拉選單往上按
        # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable ＂因為send_keys()沒有用在input element裡面＂
        try:
            self.browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[11]').click() #按人工在線入款 
        except:
            self.browser.find_element(By.XPATH,value='/html/body/div[8]/div[1]/div[1]/ul/li[11]').click()
        
        self.browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(self.amount))
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="add-dialog-merchantid"]/div[@class="el-input el-input--suffix"]/input').click() #選擇在線商號
        self.browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇在線商號
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
        self.browser.implicitly_wait(3)
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
        print(f'人工在線入款{self.amount}元')
        time.sleep(1)
        self.browser.quit()

    # 人工虛擬
    def VirtualDeposit(self):
        self.browser.get(self.url+'v2/finance/deposit/man-deposit')
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(self.NewAccount)
        self.browser.implicitly_wait(2)
        self.browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
        try:
            self.browser.find_element(By.XPATH,value='/html/body/div[8]/div[1]/div[1]/ul/li[1]').click() #按人工虛擬幣
        except:
            self.browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[1]').click() #按人工虛擬幣
        self.browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(self.amount))
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
        self.browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')

        self.browser.find_element(By.XPATH,value='//div[@qa-select="add-dialog-cryptodeposit"]//div[@class="el-input el-input--suffix"]/input').click() #選擇錢包地址
        self.browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇錢包地址
        self.browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出

        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
        print(f'人工虛擬入款{self.amount}元')
        time.sleep(1)
        self.browser.quit()
        
if __name__=='__main__':
    try:
        Manual_Deposit().ManualDeposit()
    except:
        print(f'人工入款失敗')
    try:
        Manual_Deposit().WireDeposit()
    except:
        print(f'人工公司入款失敗')
    try:
        Manual_Deposit().OnlineDeposit()
    except:
        print(f'人工在線入款失敗')
    try:    
        Manual_Deposit().VirtualDeposit()
    except:
        print(f'人工虛擬入款失敗')
    
    
