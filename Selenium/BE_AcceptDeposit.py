from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BE_InfoControl import Webchannel, Webbranch, WebNewaccount

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

# 公司入款
def WireAccept(browser,NewAccount):
    browser.get(url+'v2/finance/deposit/deposit')
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='//button[@qa-button="quick-time-today"]').click()
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[2]/div[8]/div/div/label[4]/span[1]/span').click()
    browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
    time.sleep(2)
    D_TotalResult=browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
    Number=D_TotalResult.text
    Number2=Number[1:].split(' ')
    # print(Number2) #['', '0', '条']
    if int(Number2[1])>0:
        for i in range(1,int(Number2[1])+1):
            # print(f'i={i}')
            browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[12]/div/div/button[@qa-button="accept"]').click()
            time.sleep(1)
            try:
                browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
            except:
                browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
            time.sleep(1)
            browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
            time.sleep(1)
        print(Number,'公司入款OK')
    else:
        print(f'公司入款共{Number2[1]}條 Skip')

# 在線入款
def OnlineAccept(browser,NewAccount):
    browser.get(url+'v2/finance/deposit/web-deposit')
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[1]/div[3]/div/div/label[3]/span[1]/span').click()
    browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
    time.sleep(2)
    W_TotalResult=browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
    Number=W_TotalResult.text
    Number2=Number[1:].split(' ')
    # print(Number2) #['', '0', '条']
    if int(Number2[1])>0:
        for i in range(1,int(Number2[1])+1):
            # print(f'i={i}')
            browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[17]/div/div/button[@qa-button="accept"]').click()
            time.sleep(1)
            if branch=='uat':
                try:
                    browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[2]/div[2]/div[1]/input').send_keys('1')
                except:
                    browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[2]/div[2]/div[1]/input').send_keys('1')
            if branch=='stage':
                try:
                    browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[2]/div[2]/div[1]/input').send_keys('2') #會定位失敗
                except:
                    browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[2]/div[2]/div[1]/input').send_keys('2')
            try:
                browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
            except:
                browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
            time.sleep(1)
            browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
            time.sleep(1)
        print(Number,'在線入款OK')
    else:
        print(f'在線入款共{Number2[1]}條 Skip')

# 虛擬幣入款
def VirtualAccept(browser,NewAccount):
    browser.get(url+'v2/finance/deposit/cryptocurrency')
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(NewAccount)
    browser.find_element(By.XPATH,value='//button[@qa-button="quick-time-today"]').click()
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[2]/div[8]/div/div/label[4]/span[1]').click()
    browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
    time.sleep(2)
    C_TotalResult=browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
    Number=C_TotalResult.text
    Number2=Number[1:].split(' ')
    # print(Number2) #['', '0', '条']
    if int(Number2[1])>0:
        for i in range(1,int(Number2[1])+1):
            # print(f'i={i}')
            browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[@qa-button="accept"]').click()
            time.sleep(1)
            try:
                browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
            except: 
                browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
            time.sleep(1)
            browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
            time.sleep(1)
        print(Number,'虛擬幣入款OK')
    else:
        print(f'虛擬幣入款共{Number2[1]}條 Skip')

if __name__=='__main__':
    PATH='./chromedriver.exe'
    channel=Webchannel()
    branch=Webbranch()
    NewAccount=WebNewaccount()
    url='https://'+channel+'-admin-'+branch+'.paradise-soft.com.tw/'
    browser=webdriver.Chrome(PATH)
    print(f'品牌:{channel} {branch}')
    AdminLogin(browser,branch,url)
    # OnlineAccept(browser,NewAccount)
    try:
        WireAccept(browser,NewAccount)
    except:
        print(f'公司入款失敗')
    try:
        OnlineAccept(browser,NewAccount)
    except:
        print(f'在線入款失敗')
    try:
        VirtualAccept(browser,NewAccount)
    except:
        print(f'虛擬幣入款失敗')
    time.sleep(2)
    browser.quit()