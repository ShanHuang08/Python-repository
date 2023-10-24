from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def MCABankSync():
    Banks=[]
    SyncSucess=0
    SyncFailed=0
    FailBanks=[]

    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    # browser.implicitly_wait(5)
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys('shanbot')
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys('shan612283')
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
    time.sleep(2)

    TotalBank=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div/span[1]').text
    # print(TotalBank) #共 193 条
    BList=TotalBank.split(' ')
    Endpage=int(BList[1])/20+2 #11

    for i in range(1,int(Endpage)):
        # print(f'pages={i}')
        BankCodes=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
        # print(BankCodes.text)
        for res in BankCodes:
            result=res.text
            if result not in ['AAA','Miles','test']:
            # if result not in ['AAA'] and result not in ['test']: bad method
                Banks.append(result)    
        if i<int(Endpage)-1: #11-1
            NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
            time.sleep(1)

    print(f'銀行數目:{len(Banks)}') #len=193 扣掉無效銀行=190
    # print(Banks)

    # 全選 len=16
    # for i in range(len(Banks)):
    for i in range(65,66):
        browser.find_element(By.XPATH,value='//form[@class="el-form el-form--default el-form--label-right ps-query-container"]/div/div[2]/div[@class="el-form-item__content"]/div[@class="el-input"]/div[@class="el-input__wrapper"]/input').send_keys(Banks[i]) #輸入銀行代號
        browser.find_element(By.XPATH,value='//div[@class="query-action"]/div[1]/button').click() #查找
        time.sleep(1)
        browser.find_element(By.XPATH,value='//table[@class="el-table__body"]/tbody/tr/td[10]/div/button[2]').click() #同步按鈕
        time.sleep(1)
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div/div[@class="el-form-item__content"]/label/span[1]/span').click() #勾全選
        
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[3]/div[@class="el-form-item__content"]/div[@class="el-select"]/div/div/div[@class="el-input__wrapper"]').click() #同步来源
        time.sleep(1)
        #总控后台(预设值)
        ActionChains(browser).send_keys(Keys.RETURN)
        #自定义同步内容
        # browser.find_element(By.XPATH,value='/html/body/div[2]/div[5]/div/div/div[1]/ul/li[2]').click()

        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[6]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步1 银行名称
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[7]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步2 银行网址
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[8]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步3 银行图片
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[9]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步4 启用
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[10]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步5 推荐

        browser.find_element(By.XPATH,value='//footer[@class="el-dialog__footer"]/button[2]').click() # 同步按鈕
        time.sleep(1)
        browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[8]/div/div/footer/button[1]').click() #確認同步
        time.sleep(2)

        browser.find_element(By.XPATH,value='//table[@class="el-table__body"]/tbody/tr/td[10]/div/button[3]').click() #同步紀錄
        browser.implicitly_wait(5)

        # Records=browser.find_elements(By.XPATH,value='table[@class="el-table__body"]/tbody/tr/td[5]/div')
        Records=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[5]/div') #同步結果
        num=1
        for res in Records:
            SyncRecord=res.text
            if num<=16:
                if SyncRecord=='成功':
                    SyncSucess+=1
                elif SyncRecord=='失败':
                    SyncFailed+=1
                    FailBanks.append(Banks[i])
                # print(f'{num}. {SyncRecord}')
            num+=1
        time.sleep(1)
        browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
        browser.implicitly_wait(5)
        time.sleep(2)

    print(f'同步成功:{SyncSucess}')
    print(f'同步失敗:{SyncFailed}, 銀行代碼:{FailBanks}')

    time.sleep(2)
    browser.quit()

if __name__=='__main__':
    MCABankSync()