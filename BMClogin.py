from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Library.dictionary import *

# https://gitlab.supermicro.com/swqa/ipmi-test-automation/-/blob/master/asset/xpath/webpagexpath.py
ip = '10.184.14.49'
account='ADMIN'
password='ADMIN'
Privacy = Path['Privacy']
Login = Path['Login']

def Chrome_LaunchConsole():
    browsers=[]
    for i in range(1):
        browser=webdriver.Chrome('chromedriver.exe')
        # browser=webdriver.Firefox(executable_path='geckodriver.exe')
        browser.get('http://'+ip)
        browser.maximize_window()
        browsers.append(browser)
        browser.find_element(By.ID,value=Privacy['Advance']).click()
        browser.find_element(By.ID,value=Privacy['Go ahead']).click()
        sleep(2)
        browser.find_element(By.ID,value=Login['username']).send_keys(account)
        browser.find_element(By.ID,value=Login['password']).send_keys(password)
        browser.find_element(By.ID,value=Login['Button']).click()
        sleep(7)
        
            # Launch ikvm
        # browser.execute_script('window.scrollTo(0,800)') #Scroll down
        # sleep(3)
        # browser.find_element(By.ID,value='consoleImg').click()
        # Remote Control Launch console
        browser.execute_script(goPage['Remote Control'])
        sleep(7)
    
        browser.find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
        print(f'NO.{i+1} times')
        sleep(3)
    print(f'{i+1} times')
    # browsers[0].find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
    print('Waiting...')
    sleep(600)

    # browser.execute_script('doLogout()')
    # sleep(5)

    browser.quit()

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
    Chrome_LaunchConsole()
    # Firefox()