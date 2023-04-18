from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

Mac_Add = input('BMC MAC Address: ')

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get('http://172.31.0.8/dct/cburnTools/uniquePW/')
sleep(2)
browser.find_element(By.ID, value='INPUT').send_keys(Mac_Add)
browser.find_element(By.ID, value='id1').click()
sleep(1)

WebText = browser.find_element(By.XPATH, value='/html/body/tt').text
List = WebText.split(' ')
# print(List)

if len(List) > 5 and List[5][0:6] == 'Found:':
    print(List[3][-6:]+' '+List[4]+' '+List[5][0:6])
    print(List[5][-7:]+' '+List[6]+' '+List[7])
else:
    print(WebText)

browser.quit()