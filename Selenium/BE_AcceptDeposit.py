from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BE_InfoControl import *

class Accept_Deposit():
    def __init__(self):
        channel=Webchannel()
        self.branch=Webbranch()
        self.NewAccount=WebNewaccount()
        self.url='https://'+channel+'-admin-'+self.branch+'.paradise-soft.com.tw/'
        self.browser=webdriver.Chrome('./chromedriver.exe')
        print(f'品牌:{channel} {self.branch}')
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.find_element(By.ID,value='login').send_keys(BE_account()) 
        self.browser.find_element(By.ID,value='password').send_keys(BE_password())
        if self.branch=='uat':
            self.browser.find_element(By.NAME,value='otp').send_keys('1', Keys.RETURN)
        elif self.branch=='stage':
            self.browser.find_element(By.NAME,value='otp').send_keys('2', Keys.RETURN)
        time.sleep(1)
        self.browser.implicitly_wait(5)
        
    # 公司入款
    def WireAccept(self):
        self.browser.get(self.url+'v2/finance/deposit/deposit')
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(self.NewAccount)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="quick-time-today"]').click()
        self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[2]/div[8]/div/div/label[4]/span[1]/span').click()
        self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
        time.sleep(2)
        D_TotalResult=self.browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
        Number=D_TotalResult.text
        Number2=Number[1:].split(' ')
        # print(Number2) #['', '0', '条']
        if int(Number2[1])>0:
            for i in range(1,int(Number2[1])+1):
                # print(f'i={i}')
                self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[12]/div/div/button[@qa-button="accept"]').click()
                time.sleep(1)
                try:
                    self.browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
                except:
                    self.browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
                time.sleep(1)
                self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
                time.sleep(1)
            print(Number,'公司入款OK')
        else:
            print(f'公司入款共{Number2[1]}條 Skip')
        time.sleep(2)
        self.browser.quit()

    # 在線入款
    def OnlineAccept(self):
        self.browser.get(self.url+'v2/finance/deposit/web-deposit')
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(self.NewAccount)
        self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[1]/div[3]/div/div/label[3]/span[1]/span').click()
        self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
        time.sleep(2)
        W_TotalResult=self.browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
        Number=W_TotalResult.text
        Number2=Number[1:].split(' ')
        # print(Number2) #['', '0', '条']
        if int(Number2[1])>0:
            for i in range(1,int(Number2[1])+1):
                # print(f'i={i}')
                self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[17]/div/div/button[@qa-button="accept"]').click()
                time.sleep(1)
                if self.branch=='uat':
                    try:
                        self.browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[2]/div[2]/div[1]/input').send_keys('1')
                    except:
                        self.browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[2]/div[2]/div[1]/input').send_keys('1')
                if self.branch=='stage':
                    try:
                        self.browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[2]/div[2]/div[1]/input').send_keys('2') #會定位失敗
                    except:
                        self.browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[2]/div[2]/div[1]/input').send_keys('2')
                try:
                    self.browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
                except:
                    self.browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
                time.sleep(1)
                self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
                time.sleep(1)
            print(Number,'在線入款OK')
        else:
            print(f'在線入款共{Number2[1]}條 Skip')
        time.sleep(2)
        self.browser.quit()

    # 虛擬幣入款
    def VirtualAccept(self):
        self.browser.get(self.url+'v2/finance/deposit/cryptocurrency')
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.XPATH,value='//input[@qa-input="member_login"]').send_keys(self.NewAccount)
        self.browser.find_element(By.XPATH,value='//button[@qa-button="quick-time-today"]').click()
        self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[1]/div[1]/form/div[2]/div[8]/div/div/label[4]/span[1]').click()
        self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
        time.sleep(2)
        C_TotalResult=self.browser.find_element(By.XPATH,value='//span[@class="el-pagination__total"]')
        Number=C_TotalResult.text
        Number2=Number[1:].split(' ')
        # print(Number2) #['', '0', '条']
        if int(Number2[1])>0:
            for i in range(1,int(Number2[1])+1):
                # print(f'i={i}')
                self.browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[2]/div/section/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[@qa-button="accept"]').click()
                time.sleep(1)
                try:
                    self.browser.find_element(By.XPATH,value='/html/body/div[8]/div/div[3]/button[2]').click()
                except: 
                    self.browser.find_element(By.XPATH,value='/html/body/div[7]/div/div[3]/button[2]').click()
                time.sleep(1)
                self.browser.find_element(By.XPATH,value='//button[@qa-button="search"]').click()
                time.sleep(1)
            print(Number,'虛擬幣入款OK')
        else:
            print(f'虛擬幣入款共{Number2[1]}條 Skip')
        time.sleep(2)
        self.browser.quit()

if __name__=='__main__':
    try:
        Accept_Deposit().WireAccept()
    except:
        print(f'公司入款失敗')
    try:
        Accept_Deposit().OnlineAccept()
    except:
        print(f'在線入款失敗')
    try:
        Accept_Deposit().VirtualAccept()
    except:
        print(f'虛擬幣入款失敗')
