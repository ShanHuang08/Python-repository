from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# from library.webfunctional.robot_shortcut import (
    # run, run_many, var, get_lib_instance)

browser = webdriver.Chrome('./chromedriver.exe') 
browser.get('https://ehr.supermicro.com.tw/ehrportal/LoginFOpen.asp')
browser.maximize_window()
sleep(1)
browser.find_element(By.XPATH, value='//select[@name="companyid"]/option[3]').click()
sleep(1)
browser.find_element(By.XPATH, value='//input[@name="username"]').send_keys('TW3244')
browser.find_element(By.XPATH, value='//input[@name="password"]').send_keys('TW3244')
browser.find_element(By.XPATH,value='//input[@src="img/eHRLoginSumitGray.gif"]').click()
sleep(3)

# 用ActionChians定位滑鼠座標
PublicArea=browser.find_element(By.XPATH, value='//*[@id="T_PM000200"]') #公共事務區
ResourceApply=browser.find_element(By.XPATH, value='//*[@id="mtDropDown1"]/div/div[2]/div/table/tbody/tr[2]/td[1]') #資源申請
ActionChains(browser).move_to_element(PublicArea).perform() 
ActionChains(browser).move_to_element(ResourceApply).perform() 
browser.find_element(By.XPATH, value='//*[@id="mtDropDown2"]/div/div[2]/div/table/tbody/tr[2]/td[1]').click() #按便當訂購
sleep(2)

# 用餐時段下拉選單
# <iframe name="frmMAIN" id="frmMAIN" src="indexMainP.asp" marginheight="0" frameborder="0" marginwidth="0" width="100%" height="619.6pt">
# https://ithelp.ithome.com.tw/articles/10269242

iframeTag = browser.find_element(By.ID, value='frmMAIN')
browser.switch_to.frame(iframeTag)

DinnerDate=browser.find_element(By.NAME, value='txtOrderDate').get_attribute('value')
OrderPeriod = Select(browser.find_element(By.NAME, value='sltMealOrderPeriodId'))
OrderOption = OrderPeriod.select_by_visible_text("加班晚餐-八德廠")
ActionChains(OrderPeriod).click()
ActionChains(OrderOption).click()

# 送達地點下拉選單
ArrivalLocation = Select(browser.find_element(By.NAME, value="sltRareaId"))
OptionLocation = ArrivalLocation.select_by_visible_text("Bade_B62")
ActionChains(ArrivalLocation).click()
sleep(1)
ActionChains(OptionLocation).click()
browser.find_element(By.XPATH,value='//img[@src="../img/Go.gif"]').click()


# <iframe frameborder="0" height="750px" name="mainFrame" src="PubSrv_Resource_Meal_OrderTable.asp?OrderDate=2023/2/17&amp;MealOrderPeriodId=10&amp;RareaId=5" width="100%"></iframe>

Meal_iframeTag = browser.find_element(By.NAME, value='mainFrame')
browser.switch_to.frame(Meal_iframeTag)

# 用for loop取得所有便當資訊的字串, 判斷字串 != 素便當, 點選另外一個Checkbox

# browser.find_element(By.ID, value='chk_154164').click()
browser.find_element(By.XPATH, value='//*[@id="chk_154164"]').click()
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: 
# {"method":"css selector","selector":"[id="chk_154164"]"}

DinnerBox = browser.find_element(By.XPATH, value='//*[@id="tr_154164"]/td[3]').text
Price = browser.find_element(By.XPATH, value='//*[@id="tr_154164"]/td[4]').text

print(f'日期：{DinnerDate}, 便當名稱：{DinnerBox}, 價格：{Price}元')

browser.quit()

