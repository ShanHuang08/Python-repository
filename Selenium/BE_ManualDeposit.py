#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def AdminLogin(browser,branch,url):
    browser.get(url)
    browser.maximize_window()
    browser.find_element(By.ID,value='login').send_keys('shanbot') 
    browser.find_element(By.ID,value='password').send_keys('shan612283')
    if branch=='uat':
        browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
    elif branch=='stage':
        browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
    time.sleep(1)

    browser.get(url+'v2/finance/deposit/man-deposit')
    browser.implicitly_wait(5)

# 人工存入
def ManualDeposit(browser,NewAccount,amount):
    browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(NewAccount)
    time.sleep(1)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
    browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[2]').click() #按人工存入
    browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(amount-20))
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')
    browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
    print(f'人工存入{amount-20}元')
    time.sleep(5)
    
# 人工公司
def WireDeposit(browser,NewAccount,amount):
    browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
    time.sleep(1)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').send_keys(Keys.UP) #下拉選單往上按
    # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable ＂因為send_keys()沒有用在input element裡面＂
    browser.find_element(By.XPATH,value='/html/body/div[9]/div[1]/div[1]/ul/li[10]').click() #按人工公司入款
    browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(amount))
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')

    browser.find_element(By.XPATH,value='//div[@class="el-form-item account_numbers"]/div[@class="el-form-item__content"]/div[@class="el-select"]/div[@class="el-input el-input--suffix"]/input').click() #選擇銀行帳號
    browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇銀行帳號
    browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
    print(f'人工公司入款{amount}元')
    time.sleep(5)
    
# 人工在線
def OnlineDeposit(browser,NewAccount,amount):
    browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
    time.sleep(1)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').send_keys(Keys.UP) #下拉選單往上按
    # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable ＂因為send_keys()沒有用在input element裡面＂
    browser.find_element(By.XPATH,value='/html/body/div[10]/div[1]/div[1]/ul/li[11]').click() #按人工在線入款 

    browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(amount))
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')
    time.sleep(1)
    browser.find_element(By.XPATH,value='//div[@qa-select="add-dialog-merchantid"]/div[@class="el-input el-input--suffix"]/input').click() #選擇在線商號
    browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇在線商號
    browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出
    time.sleep(1)
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
    browser.implicitly_wait(3)
    time.sleep(1)
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
    print(f'人工在線入款{amount}元')
    time.sleep(5)
    
# 人工虛擬
def VirtualDeposit(browser,NewAccount,amount):
    browser.find_element(By.XPATH,value='//button[@qa-button="add"]').click()
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-memberlogin"]').send_keys(NewAccount)
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH,value='//div[@qa-select="actioncode"]/div/input[@class="el-input__inner"]').click() #按下拉選單
    browser.find_element(By.XPATH,value='/html/body/div[11]/div[1]/div[1]/ul/li[1]').click() #按人工虛擬幣
    browser.find_element(By.XPATH,value='//textarea[@qa-input="add-dialog-remark"]').send_keys('bot_test') #備註
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-transferamount"]').send_keys(str(amount))
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountamount"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditpoint"]').send_keys('5')
    browser.find_element(By.XPATH,value='//input[@qa-input="add-dialog-discountauditdue"]').send_keys('5')

    browser.find_element(By.XPATH,value='//div[@qa-select="add-dialog-cryptodeposit"]//div[@class="el-input el-input--suffix"]/input').click() #選擇錢包地址
    browser.find_element(By.XPATH,value='//div[@x-placement="top-start"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]').click() #選擇錢包地址
    browser.find_element(By.XPATH,value='//button[@qa-button="add-dialog-submit"]').click() #送出

    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-confirm"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//button[@qa-button="tab-group-detail-dialog-confirm"]').click()
    print(f'人工虛擬入款{amount}元')
    
if __name__=='__main__':
    PATH='./chromedriver.exe'
    channel='bh'
    branch='uat'
    NewAccount='stest053'
    url='https://'+channel+'-admin-'+branch+'.paradise-soft.com.tw/'
    browser=webdriver.Chrome(PATH)
    amount=100
    AdminLogin(browser,branch,url)
    ManualDeposit(browser,NewAccount,amount)
    WireDeposit(browser,NewAccount,amount)
    OnlineDeposit(browser,NewAccount,amount)
    VirtualDeposit(browser,NewAccount,amount)
    time.sleep(2)
    browser.quit()
