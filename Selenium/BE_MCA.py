from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

brands=[]

browser=webdriver.Chrome('./Chromedriver.exe')
browser.get('https://central-web-uat.paradise-soft.com.tw/')
# browser.implicitly_wait(5)
browser.maximize_window()
time.sleep(1)
browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys('shanbot')
browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys('shan612283')
browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
time.sleep(1)
browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
time.sleep(2)

for i in range(1,11):
    print(f'pages={i}')
    BankCodes=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
    # print(BankCodes.text)
    for res in BankCodes:
        result=res.text
        if result not in ['AAA','test']:
        # if result not in ['AAA'] and result not in ['test']: bad method
            brands.append(result)    
    if i<10:
        NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
        time.sleep(1)
    else:
        pass

print(len(brands)) #len=193
print(brands)
# print(brands[0]) AAA print(brands[165]) test




time.sleep(5)
browser.quit()