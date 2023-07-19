from Library.dictionary import Path, scripts
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

BMC_ip = '172.31.34.231'
Account='ADMIN'
Password='ADMIN'
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
browser.execute_script(scripts['Account Services'])
sleep(7)
browser.quit()