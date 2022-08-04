#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def WebLogin(url,browser):
    browser.get(url)
    # browser.maximize_window()
    # 關閉平台公告
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//div[@class="img"]/div[@class="btn_close"]').click()
    browser.find_element(By.NAME,value='name').send_keys('5')
    browser.find_element(By.ID,value='nzc-header-password').send_keys('H')
    browser.find_element(By.ID,value='nzc-header-captcha').send_keys('1',Keys.RETURN)
    # 關閉帳戶安全
    time.sleep(2) #Message: stale element reference: element is not attached to the page document
    if browser.find_element(By.XPATH,value='//div[@class="popup__header"]').is_displayed(): # The return type of isDisplayed() method is Boolean.
        browser.find_element(By.XPATH,value='//a[@data-bind="click: nextTimeRemind"]').click()
    else:
        pass

#def彩票極速11選5投注總和 
def Jisu11x5Sum(browser,Sum):
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//div[@class="lottery2-jisu11x5"]').click()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[Sum]) #換分頁
    browser.implicitly_wait(5)
    # 判斷是否封盤
    if browser.find_element(By.XPATH,value='//div[@style="display: none;"]')==False:
        Timeout = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(((By.XPATH,'//div[@style="display: none;"]'))))
    else:
        pass
    # 投注10元
    browser.find_element(By.XPATH,value='//input[@class="game_control_money"]').send_keys('10')
    # 總和：和大
    SumBig=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[3]/input').click()
    # 和小
    # SumSmall=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[3]/input').click()
    # 和單
    # SumSingular=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[3]/input').click()
    # 和雙
    # SumPlural=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[3]/input').click()
    # print(type(SumBig)) <class 'NoneType'>

    browser.find_element(By.CLASS_NAME,value='game_control_subimt').click()
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH,value='//span/a[@class="betting_Btn active"]').click()
    time.sleep(3)
    # 關閉彈窗
    browser.find_element(By.XPATH,value='//button[@class="swal2-confirm swal2-styled"]').click()

# def 極速11選5投注任選
def Jisu11x5Any(browser,Any):
    browser.set_window_size(1045,1020) #寬度設為1045
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,value='//div[@class="lottery2-jisu11x5"]').click()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[Any]) #換分頁
    browser.implicitly_wait(5)
    # 判斷是否封盤
    if browser.find_element(By.XPATH,value='//div[@style="display: none;"]')==False:
        Timeout = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(((By.XPATH,'//div[@style="display: none;"]'))))
    else:
        pass

    # 關閉左邊彈窗
    if browser.find_element(By.XPATH,value='/html/body/div[2]/div[@style="left: 0px;"]'):
        browser.find_element(By.XPATH,value='/html/body/div[2]/div[2]/ul/li[5]/img').click()
    else:
        pass
    # 點任選
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[3]/div/div[2]/ul/li[4]/span').click()
    # 投注10元
    browser.find_element(By.XPATH,value='//input[@class="game_control_money"]').send_keys('10')

    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/div/ul/li[1]/a').click()
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/div/ul/li[2]/a').click()
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/div/ul/li[3]/a').click()
    browser.find_element(By.XPATH,value='//input[@class="game_control_money fn-reset-line_height"]').click()
    browser.find_element(By.CLASS_NAME,value='game_control_subimt').click()
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH,value='//span/a[@class="betting_Btn active"]').click()
    time.sleep(3)
    browser.find_element(By.XPATH,value='//button[@class="swal2-confirm swal2-styled"]').click()

# def 爬今日投注紀錄
def BetOrderRecord(browser):
    browser.find_element(By.ID,value='nzc-nav-order').click()
    browser.implicitly_wait(5)
    BetNumber=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[1]/span[1]')
    print(f'单号={BetNumber.text}')
    BetTime=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[1]/span[2]')
    print(f'時間={BetTime.text}')
    BetType=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[2]/span[1]')
    print(f'彩种={BetType.text}')
    BetDetails=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[3]/div[@class="product-result-content__scroll order -v2-ttmj"]/div[@class="order-detail"]/div[@class="order-detail__content"]/div[@class="order-detail__result"]/ul')
    print(f'注单详情=\n{BetDetails.text}')
    BetMoney=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[4]')
    print(f'金额={BetMoney.text}')
    BetStatus=browser.find_element(By.XPATH,value='//table[@class="tableData"]/tbody/tr/td[6]/div/span')
    print(f'状态={BetStatus.text}')


def main():
    PATH='./chromedriver.exe'
    channel='bh' #bh,sc
    branch='uat'
    url='https://'
    browser=webdriver.Chrome(PATH)
    WebLogin(url,browser)
    browser.find_element(By.ID,value='nzc-nav-lottery').click()
    Jisu11x5Any(browser,1)
    BetOrderRecord(browser)
    time.sleep(1)
    browser.get('https://')
    Jisu11x5Sum(browser,2)
    BetOrderRecord(browser)
    time.sleep(5)
    browser.quit()
main()
