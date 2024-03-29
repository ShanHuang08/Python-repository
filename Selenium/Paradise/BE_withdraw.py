from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BE_InfoControl import *

def Withdraw():
    channel=Webchannel()
    branch=Webbranch()
    NewAccount=WebNewaccount()
    url='https://'+channel+'-admin-'+branch+'.paradise-soft.com.tw/'
    browser=webdriver.Chrome('./chromedriver.exe') #webdriver2
    print(f'品牌:{channel} {branch}')
    browser.get(url)
    browser.maximize_window()
    browser.find_element(By.ID,value='login').send_keys(BE_account()) 
    browser.find_element(By.ID,value='password').send_keys(BE_password())
    if branch=='uat':
        browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
    elif branch=='stage':
        browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
    time.sleep(1)

# 提款
# def Withdraw(browser,NewAccount):
    browser.get(url+'withdraw')
    browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/input').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div[4]/button[1]').click() #今日 如果今日無資料 按昨日
    # browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div[4]/button[2]').click() #昨日
    browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div[7]/div/label[2]/input').click() #待確認
    browser.find_element(By.ID,value='btnSearch').click()
    time.sleep(2)
    TotalResult=browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[3]/div/div/div[2]/div/table/tfoot/tr/td/div[1]/div/span')
    Number=TotalResult.text

    if int(Number)>0:
        for i in range(1,int(Number)+1):
            # 如果鎖定沒按
            if browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[3]/div/div/div[2]/div/table/tbody[1]/tr[1]/td[12]/div/button[1]').is_displayed():
                browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[3]/div/div/div[2]/div/table/tbody[1]/tr[1]/td[12]/div/button[1]').click() #鎖定
                time.sleep(1)
            browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[3]/div/div/div[2]/div/table/tbody[1]/tr/td[12]/div/button[5]').click() #出款
            time.sleep(1)
            browser.find_element(By.XPATH,value='/html/body/div[3]/div[3]/div/div[3]/div/div/div[2]/div/table/tbody[1]/tr[1]/td[12]/div/div/div[2]/div/a[1]').click() #確定
            time.sleep(1)
            browser.find_element(By.ID,value='btnSearch').click()
            time.sleep(1)
        print(f'共{Number}條紀錄, 提款完成')
    else:
        print(f'共{Number}條紀錄, Skip')
    
    time.sleep(2)
    browser.quit()

if __name__=='__main__':
    try:
        Withdraw()
    except:
        print(f'提款失敗')
