from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from BE_InfoControl import *
import random
from selenium.webdriver.chrome.options import Options
Test_Banks=['123','AAA','ABC123','Miles','test']
MaxNum=15 #15個品牌
Change=True #False=不做修改, custom品牌全選

def MCABankSync_default():
    Banks=[]
    SyncSucess=0
    SyncFailed=0
    FailBanks=[]
    
    # options=Options()
    # options.add_argument('--headless')
    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
    time.sleep(2)

    TotalBank=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div/span[1]').text
    # print(TotalBank) #共 193 条
    BNum=TotalBank.split(' ')
    Endpage=int(BNum[1])/30+2 #8
    # print(f'Endpage={Endpage}')
    if int(BNum[1])==0:
        ErrorMsg='銀行數目為'+BNum[1]
        browser.quit()
        raise ValueError(ErrorMsg)

    for i in range(1,int(Endpage)):
        # print(f'pages={i}')
        BankCodes=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
        # print(BankCodes.text)
        for res in BankCodes:
            result=res.text
            if result not in Test_Banks:
            # if result not in ['AAA'] and result not in ['test']: bad method
                Banks.append(result)    
        if i<int(Endpage)-1: #11-1
            NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
            time.sleep(1)

    print(f'銀行數目:{len(Banks)}') #len=193 扣掉無效銀行=190
    # print(Banks)

    # 全選 len=MaxNum=15
    for i in range(len(Banks)):
    # for i in range(2):
        browser.find_element(By.XPATH,value='//form[@class="el-form el-form--default el-form--label-right ps-query-container"]/div/div[2]/div[@class="el-form-item__content"]/div[@class="el-input"]/div[@class="el-input__wrapper"]/input').send_keys(Banks[i]) #輸入銀行代號
        browser.find_element(By.XPATH,value='//div[@class="query-action"]/div[1]/button').click() #查找
        time.sleep(1)
        browser.find_element(By.XPATH,value='//table[@class="el-table__body"]/tbody/tr/td[10]/div/button[2]').click() #同步按鈕
        time.sleep(1)
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div/div[@class="el-form-item__content"]/label/span[1]/span').click() #勾全選
        # browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div/div[@class="el-form-item__content"]/div/label[2]/span[1]').click() #勾BH
        
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

        # browser.find_element(By.XPATH,value='//div[@class="ps-query-container__optional"]/div[1]/div[@class="el-form-item__content"]/div/label[1]').click() #今日
        # browser.find_element(By.XPATH,value='//div[@class="ps-query-container__optional"]/div[1]/div[@class="el-form-item__content"]/div/label[4]').click() #上週
        # browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/button').click() #查找

        # Records=browser.find_elements(By.XPATH,value='table[@class="el-table__body"]/tbody/tr/td[5]/div')
        Records=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[5]/div') #同步結果
        num=1
        for res in Records:
            SyncRecord=res.text
            if num<=MaxNum:
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
    if len(FailBanks)>0:
        print(f'同步失敗:{SyncFailed}, 銀行代碼:{FailBanks}')
    else:
        print(f'同步失敗:{SyncFailed}')
    print('总控后台(预设值)同步完成')

    time.sleep(2)
    browser.quit()

def MCABankSync_custom():
    Banks=[]
    SyncSucess=0
    SyncFailed=0
    FailBanks=[]
    SelectAll=0
    if Change==True:
        Digit=input('請問要勾選幾個品牌(1-5)? ')
        # label[1]=3H, label[2]=BH, label[3]=C7, label[4]=C8, label[5]=CDD
        if int(Digit)==0 or int(Digit)>5:
            Digit=input('請輸入(1-5)之間的數字 ')
    SelectSome=int(Digit) #要勾幾個品牌 全選=0

    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
    time.sleep(2)

    TotalBank=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div/span[1]').text
    # print(TotalBank) #共 193 条
    BNum=TotalBank.split(' ')
    Endpage=int(BNum[1])/30+2 #8
    # print(f'Endpage={Endpage}')
    if int(BNum[1])==0:
        ErrorMsg='銀行數目為'+BNum[1]
        browser.quit()
        raise ValueError(ErrorMsg)

    for i in range(1,int(Endpage)):
        # print(f'pages={i}')
        BankCodes=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
        # print(BankCodes.text)
        for res in BankCodes:
            result=res.text
            if result not in Test_Banks:
            # if result not in ['AAA'] and result not in ['test']: bad method
                Banks.append(result)    
        if i<int(Endpage)-1: #11-1
            NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
            time.sleep(1)

    # print(f'銀行數目:{len(Banks)}') #len=193 扣掉無效銀行=190
    # print(Banks)

    # 全選 len=MaxNum=15
    # for i in range(len(Banks)):
    for i in range(2):
        browser.find_element(By.XPATH,value='//form[@class="el-form el-form--default el-form--label-right ps-query-container"]/div/div[2]/div[@class="el-form-item__content"]/div[@class="el-input"]/div[@class="el-input__wrapper"]/input').send_keys(Banks[i]) #輸入銀行代號
        browser.find_element(By.XPATH,value='//div[@class="query-action"]/div[1]/button').click() #查找
        time.sleep(1)
        browser.find_element(By.XPATH,value='//table[@class="el-table__body"]/tbody/tr/td[10]/div/button[2]').click() #同步按鈕
        time.sleep(1)
        
        if Change==False:
            browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div/div[@class="el-form-item__content"]/label/span[1]/span').click() #勾全選
            SelectAll+=1
        else:
            if SelectSome>0:
                ch=0
                for k in range(SelectSome):
                    ch+=1
                    browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div/div[@class="el-form-item__content"]/div/label['+str(ch)+']/span[1]').click()
                    
        if SelectAll==SelectSome:
            raise ValueError('SelectAll=SelectSome, 全選跟單選的值不能相同')

        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[3]/div[@class="el-form-item__content"]/div[@class="el-select"]/div/div/div[@class="el-input__wrapper"]').click() #同步来源
        time.sleep(1)
        #总控后台(预设值)
        # ActionChains(browser).send_keys(Keys.RETURN)
        #自定义同步内容
        browser.find_element(By.XPATH,value='/html/body/div[2]/div[5]/div/div/div[1]/ul/li[2]').click()

        # 修改銀行網址
        Addurl=random.choice(['test1','test2','test3'])
        Addname=random.choice(['測試一','測試二'])
        if Change==True:
            # 改網址
            browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[7]/div[2]/div/div[1]/div/div/div/div/input').clear()
            browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[7]/div[2]/div/div[1]/div/div/div/div/input').send_keys('http://www.'+Addurl+'.com/')
            # 改銀行名稱
            # browser.find_element(By.XPATH,value='').clear()
            # browser.find_element(By.XPATH,value='').send_keys(Addname)
        else:
            pass

        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[6]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步1 银行名称
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[7]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步2 银行网址
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[8]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步3 银行图片
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[9]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步4 启用
        browser.find_element(By.XPATH,value='//div[@class="el-dialog__body"]/form/div[10]/div[@class="el-form-item__content"]/div[@class="el-row"]/div[@class="el-col el-col-6 is-guttered"]/label/span[1]/span').click() #勾是否同步5 推荐
        
        time.sleep(1)
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
            if SelectAll==0: #沒有全選
                MaxNum=SelectSome
            
            if num<=MaxNum:
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
    if len(FailBanks)>0:
        print(f'同步失敗:{SyncFailed}, 失敗銀行代碼:{FailBanks}')
    else:
        print(f'同步失敗:{SyncFailed}')
    print('自定義同步完成')
    time.sleep(2)
    browser.quit()

def MCA_SyncManagement():
    Brand_names=[]
    options=Options()
    options.add_argument('--headless')
    browser=webdriver.Chrome('./Chromedriver.exe',options=options)
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/system/system.brand_sync') #同步管理頁面
    browser.implicitly_wait(5)
    time.sleep(2)

    # 同步管理品牌名稱數量
    BrandNames=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]')
    for res in BrandNames:
        Brand_names.append(res.text)
    # print(Brand_names)
    return len(Brand_names) #16

if __name__=='__main__':
    # MCABankSync_default()
    MCABankSync_custom()
    # print(MCA_SyncManagement())
    
