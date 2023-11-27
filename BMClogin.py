from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Library.dictionary import *
from Library.Selenium import SeleniumBase
from Library.Call_Method import Check_ipaddr

driver_path = 'C:\\Users\\Stephenhuang\\Python\\'
Privacy = Path['Privacy']
Login = Path['Login']
class BMCLogin(SeleniumBase):
    def Chrome_LaunchConsole(self):
        self.browser = self.Chrome(path=driver_path)
        self.browser.get('http://'+ip)
        self.browser.maximize_window()
        sleep(1)
        self.find_ID(value=Privacy['Advance']).click()
        self.find_ID(value=Privacy['Go ahead']).click()
    
        sleep(2)
        self.find_ID(value=Login['username']).send_keys(account)
        self.find_ID(value=Login['password']).send_keys(password)
        self.find_ID(value=Login['Button']).click()
        sleep(10) #用wait element會比較好
        self.browser.execute_script(goPage['Remote Control'])
        sleep(7)
        self.find_xpath(value='//button[@id="launchConsole"]').click()

        sleep(10)
        self.browser.execute_script('doLogout()')
        sleep(5)
        self.browser.quit()

            
                # Launch ikvm
            # browser.execute_script('window.scrollTo(0,800)') #Scroll down
            # sleep(3)
            # browser.find_element(By.ID,value='consoleImg').click()
            # Remote Control Launch console

    def Firefox():
        browsers=[]
        for i in range(4):
            browser=webdriver.Firefox(executable_path='geckodriver.exe')
            browser.get('http://'+ip)
            browsers.append(browser)
            # browser.find_element(By.ID,value='advancedButton').click()
            # browser.find_element(By.ID,value='exceptionDialogButton-link').click()
            sleep(2)
            browser.find_element(By.ID,value='usrName').send_keys(account)
            browser.find_element(By.ID,value='pwd').send_keys(password)
            browser.find_element(By.ID,value='login_word').click()
            sleep(7)
            browser.maximize_window()

            # Remote Control Launch console
            browser.execute_script('goPage("remote")')
            sleep(5)
        
            browser.find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
            print(f'NO.{int(i)+1} times')
            sleep(5)
        print('5 times')
        browsers[0].switch_to.window(browsers[0].current_window_handle)
        browsers[0].find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
        print('Waiting...')
        sleep(100)

        # browser.execute_script('doLogout()')
        # sleep(5)

        browser.quit()

if __name__=='__main__':
    ip = '10.184.14.49'
    account='ADMIN'
    password='ADMIN'
    if Check_ipaddr(ip=ip):
        BMCLogin().Chrome_LaunchConsole()
    else:
        print(f'{ip} is unable to connect')
    # Firefox()