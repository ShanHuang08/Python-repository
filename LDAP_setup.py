from Library.dictionary import Path, goPage, redfish
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


BMC_ip = '172.31.34.231'
Account=Password='ADMIN'
auth = ('ADMIN', 'ADMIN')

def Sccape(Account, Password):
    Privacy = Path['Privacy']
    Login = Path['Login']
    Ldap = Path['Account Services']['Directory Services']['LDAP']

    browser=webdriver.Chrome('chromedriver.exe')
    browser.get('http://'+BMC_ip)
    browser.find_element(By.ID,value=Privacy['Advance']).click()
    browser.find_element(By.ID,value=Privacy['Go ahead']).click()
    sleep(2)
    browser.find_element(By.ID,value=Login['username']).send_keys(Account)
    browser.find_element(By.ID,value=Login['password']).send_keys(Password)
    browser.find_element(By.ID,value=Login['Button']).click()
    sleep(7)
    browser.maximize_window()
    browser.execute_script(goPage['Account Services'])
    sleep(7)

    # Turn on LDAP
    browser.find_element(By.ID,value='').click()
    sleep(5)
    browser.find_element(By.ID,value=Ldap['Bind DN']).send_keys('cn=Manager,dc=ipmi,dc=com')
    browser.find_element(By.ID,value=Ldap['Bind Password']).send_keys('secret')
    browser.find_element(By.ID,value=Ldap['Username Attribute']).send_keys('cn')

    # Add buttin
    browser.find_element(By.ID,value=Ldap['Server Add']).click()
    sleep(2)
    browser.find_element(By.ID,value=Ldap['Ip add']).send_keys('10.140.168.235')

    browser.quit()

def Redfish_setup():
    pass