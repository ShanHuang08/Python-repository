from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# https://gitlab.supermicro.com/swqa/ipmi-test-automation/-/blob/master/asset/xpath/webpagexpath.py
ip = '10.184.30.32'
account='ADMIN'
password='ADMIN'

def test():
    browser=webdriver.Chrome('chromedriver.exe')
    browser.get('http://'+ip)

    browser.find_element(By.ID,value='details-button').click()
    browser.find_element(By.ID,value='proceed-link').click()
    sleep(1)
    browser.find_element(By.ID,value='usrName').send_keys(account)
    browser.find_element(By.ID,value='pwd').send_keys(password)
    browser.find_element(By.ID,value='login_word').click()
    sleep(5)
    browser.maximize_window()
    # Launch ikvm
    # browser.execute_script('window.scrollTo(0,800)') #Scroll down
    # sleep(3)
    # browser.find_element(By.ID,value='consoleImg').click()

    # Remote Control Launch console
    browser.execute_script('goPage("remote")')
    sleep(5)

    for i in range(5):
        browser.find_element(By.XPATH, value='//button[@id="launchConsole"]').click()
        sleep(3)

    sleep(10)

    browser.execute_script('doLogout()')
    sleep(5)

    browser.quit()

if __name__=='__main__':
    test()