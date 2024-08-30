import sys
sys.path.append('C:\\Users\\Stephenhuang\\Python')
from Library.dictionary import goPage, redfish
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Library.Redfish_requests import *
from Library.SMASH import SMASH
from Library.Call_Method import GetPath
from Library.Common_Func import Check_PWD

Account=Password='ADMIN'

def Scrape(Account, Password):
    Ldap = GetPath('Account Services.Directory Services.LDAP')

    browser=webdriver.Chrome('chromedriver.exe')
    browser.get('http://'+ BMC_ip)
    browser.find_element(By.ID,value=GetPath('Privacy.Advance')).click()
    browser.find_element(By.ID,value=GetPath('Privacy.Advance.Go ahead')).click()
    sleep(2)
    browser.find_element(By.ID,value=GetPath('Login.username')).send_keys(Account)
    browser.find_element(By.ID,value=GetPath('Login.password')).send_keys(Password)
    browser.find_element(By.ID,value=GetPath('Login.Button')).click()
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
    print(f"Server: {BMC_ip}")
    url = 'https://'+BMC_ip+'/redfish/v1/AccountService'
    setup = PATCH(url=url, auth=auth, body=redfish['LDAP Setup'])
    if setup[0] == 200:
        print('LDAP setup success')
    else:
        print(f'LDAP Setup failed, Status code: {setup[0]}\n{setup[-1]}')

def Clear_setup():
    print('Clear LDAP setup')
    url = 'https://'+BMC_ip+'/redfish/v1/AccountService'
    clear = PATCH(url=url, auth=auth, body=redfish['LDAP clear'])
    if clear[0] == 200:
        print('Setup has cleared')
    else:
        print(f'Clear failed, Status code: {clear[0]}\n{clear[-1]}')

if __name__=='__main__':
    BMC_ip = '10.184.30.139'
    auth = Check_PWD(BMC_ip, unique='DWDKCNBMVW')
    Redfish_setup()
    # SMASH(ip=BMC_ip)
    # Clear_setup()