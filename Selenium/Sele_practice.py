# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SelectBrowser='Chrome'
if SelectBrowser=='Chrome':
    PATH='C:/Users/shan_huang/Python/chromedriver.exe'
    browser=webdriver.Chrome(PATH)
elif SelectBrowser=='Edge':
    PATH='C:/Users/shan_huang/Python/msedgedriver.exe'
    browser=webdriver.Edge(PATH)

url='https://www.google.com'
# options = Options()
# options.add_argument('--headless')
# browser=webdriver.Chrome(PATH, options=options)

# 最大化窗口  
# browser.maximize_window() 
browser.get(url)
print(browser.title)
browser.find_element(By.NAME, value='q').send_keys('pixel 7', Keys.RETURN)

# try except判斷元素是否存在
try:
    element = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located(((By.XPATH,'//a[contains(text(),"圖片")]'))
    ))
    print('Element is available')
    # browser.find_element(By.XPATH,value='//a[contains(text(),"圖片")]').click()
    element.click()
except:
    print('Element is unavailable')
    browser.quit()


# search_btn.submit() #送出
# 抓圖
# urllib.urlretrieve()

time.sleep(5)
# browser.close() #關閉Tab
browser.quit() #關閉Web browser
