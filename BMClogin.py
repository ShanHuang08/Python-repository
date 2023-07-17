from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Library.dictionary import *

# https://gitlab.supermicro.com/swqa/ipmi-test-automation/-/blob/master/asset/xpath/webpagexpath.py
ip = '172.31.52.168'
account='ADMIN'
password='ADMIN'


def Chrome_LaunchConsole():
    browsers=[]
    for i in range(4):
        browser=webdriver.Chrome('chromedriver.exe')
        # browser=webdriver.Firefox(executable_path='geckodriver.exe')
        browser.get('http://'+ip)
        browsers.append(browser)
        browser.find_element(By.ID,value='details-button').click()
        browser.find_element(By.ID,value='proceed-link').click()
        sleep(2)
        browser.find_element(By.ID,value='usrName').send_keys(account)
        browser.find_element(By.ID,value='pwd').send_keys(password)
        browser.find_element(By.ID,value='login_word').click()
        sleep(7)
        browser.maximize_window()
            # Launch ikvm
        # browser.execute_script('window.scrollTo(0,800)') #Scroll down
        # sleep(3)
        # browser.find_element(By.ID,value='consoleImg').click()
        # Remote Control Launch console
        browser.execute_script('goPage("remote")')
        sleep(5)
    
        browser.find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
        print(f'NO.{i} times')
        sleep(3)
    print('5 times')
    browsers[0].find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
    print('Waiting...')
    sleep(100)

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