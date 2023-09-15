from Library.dictionary import Path, goPage, redfish
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Library.Redfish_requests import *
from Library.SMASH import SMASH


BMC_ip = '10.184.19.24'
url = 'https://'+BMC_ip+'/redfish/v1/AccountService'
Account=Password='ADMIN'
auth = ('ADMIN', 'ADMIN')


def Scrape(Account, Password):
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
    setup = PATCH(url=url, auth=auth, body=redfish['LDAP Setup'])
    if setup[0] == 200:
        print('LDAP setup success')
    else:
        print(f'Setup failed, Status code: {setup[0]}\n{setup[-1]}')

def Clear_setup():
    print('Clear LDAP setup')
    clear = PATCH(url=url, auth=auth, body=redfish['LDAP clear'])
    if clear[0] == 200:
        print('Setup has cleared')
    else:
        print(f'Clear failed, Status code: {clear[0]}\n{clear[-1]}')

if __name__=='__main__':
    print(f"Server: {BMC_ip}")
    Redfish_setup()
    SMASH(ip=BMC_ip)
    Clear_setup()