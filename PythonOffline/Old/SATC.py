from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

ip='10.184.30.32'
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get('https://satc.supermicro.com/login')
browser.find_element(By.NAME, value='username').send_keys('StephenHuang')
browser.find_element(By.NAME, value='password').send_keys('Sh@nDethl8889')
browser.find_element(By.XPATH, value='//button[@class="ui fluid button"]').click()

sleep(1)
browser.get('https://satc.supermicro.com/inventory/motherboard')
sleep(1)

browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[4]/div/div/input').send_keys(ip)
sleep(1)
BmcMac=browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[17]/div/div/span/div').text
UniquePW=browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/span/span').text

print(f'BMC MAC: {BmcMac}')
print(f'Unique PW: {UniquePW}')

sleep(5)
browser.quit()