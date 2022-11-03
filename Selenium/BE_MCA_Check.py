#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from BE_InfoControl import *
import json
from BE_MCA_Sync import MCA_SyncManagement

def MCA_CheckBanks_Contents():
    excluce_code=['Miles','test','ABC123']  
    exclude_name=['MBANK','ewqewqe','123321']
    exclude_url=['test','555555']
    exclude_pic=['https://squirrel-uat.paradise-soft.com.tw//brand-image/base/bank/abc123.jpeg?1667384821','https://squirrel-uat.paradise-soft.com.tw//brand-image/base/bank/miles.png?1666681915','https://squirrel-uat.paradise-soft.com.tw//brand-image/base/bank/test.jpeg?1666860254']
    Banks_code=[]
    Banks_code_for_exclude=[]
    Banks_name=[]
    Banks_url=[]
    Banks_picture=[]
    Banks_status=[]
    Banks_recommend=[]
    Banks_name_success=0 
    Banks_name_failed=0
    Banks_url_success=0
    Banks_url_failed=0
    Banks_picture_success=0
    Banks_picture_failed=0
    Banks_status_success=0
    Banks_status_failed=0
    Banks_recommend_success=0
    Banks_recommend_failed=0
    NameFailBanks=[]
    UrlFailBanks=[]
    PicFailBanks=[]
    StatusFailBanks=[]
    RecommendFailBanks=[]

    options=Options() 
    options.add_argument('--headless')
    browser=webdriver.Chrome('./Chromedriver.exe', options=options)
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

    for i in range(1,int(Endpage)):
        # print(f'pages={i}')
        BankCodes=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
        BankNames=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[4]/div')
        BankUrls=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[5]/div')
        BankPics=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div/img')
        BankStatus=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span')
        BanksRec=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[8]/div/span')
        # print(BankCodes.text)
        for res in BankCodes: #len=191
            Banks_code_for_exclude.append(res.text)
            code=res.text
            if code not in excluce_code:
                Banks_code.append(code)
        for res in BankNames: #len=191
            name=res.text
            if name not in exclude_name:
                Banks_name.append(name)
        for res in BankUrls: #len=191
            url=res.text
            if url not in exclude_url:
                Banks_url.append(url)
        for res in BankPics: #len=191
            pic=res.get_attribute('src')
            if pic not in exclude_pic:
                Banks_picture.append(pic)

        for res in BankStatus: #len=193 要先篩選
            status=res.text
            if status=='是': 
                Banks_status.append(1)
            elif status=='否':
                Banks_status.append(0)
        for res in BanksRec: #len=193
            recomm=res.text
            if recomm=='是': 
                Banks_recommend.append(1)
            elif recomm=='否':
                Banks_recommend.append(0)

        if i<int(Endpage)-1: #7-1 pages
            NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
            time.sleep(1)

    # exclude i=121 Miles, i=164 test
    for i in range(len(Banks_code_for_exclude)):
        if Banks_code_for_exclude[i] in excluce_code:
            Banks_status.pop(i)
            Banks_recommend.pop(i)

    print(f'銀行數目:{len(Banks_code)}, 名稱:{len(Banks_name)}, 網址:{len(Banks_url)}, 圖片:{len(Banks_picture)}, 狀態:{len(Banks_status)}, 推薦:{len(Banks_recommend)}') #len=193 扣掉無效銀行=190+1

    # print(len(Banks_picture))
    # print(Banks)
    browser.quit()

    with open('C:/Users/shan_huang/Python/Banks.json','r',encoding="utf-8") as jsonfile:
        jdata=json.load(jsonfile)

    if len(Banks_name) and len(Banks_url) and len(Banks_picture) != len(jdata['Items']):
        if len(Banks_name) != len(jdata['Items']):
            print(f'names({len(Banks_name)}) != jdata ')
        elif len(Banks_url) != len(jdata['Items']):
            print(f'urls({len(Banks_url)}) != jdata ')
        elif len(Banks_picture) != len(jdata['Items']):
            print(f'pictures({len(Banks_picture)}) != jdata ')
        raise ValueError('Unable to make a comparison. Lengths are not the same!')


    for i in range(len(jdata['Items'])): #len=191
            if jdata['Items'][i]['name'] == Banks_name[i]:
                Banks_name_success+=1
            else:
                Banks_name_failed+=1
                NameFailBanks.append(Banks_code[i])
            
            if jdata['Items'][i]['url'] == Banks_url[i]: #IndexError: list index out of range
                Banks_url_success+=1
            else:
                Banks_url_failed+=1
                UrlFailBanks.append(Banks_code[i])
            
            if jdata['Items'][i]['imgpath'][0:4] and Banks_picture[i][0:4] in ['http']: #圖片網址比對有問題
                Banks_picture_success+=1
            else:
                Banks_picture_failed+=1
                PicFailBanks.append(Banks_code[i])
            
            if jdata['Items'][i]['status'] == Banks_status[i]:
                Banks_status_success+=1
            else:
                Banks_status_failed+=1
                StatusFailBanks.append(Banks_code[i])

            if jdata['Items'][i]['recommend'] == Banks_recommend[i]:
                Banks_recommend_success+=1
            else:
                Banks_recommend_failed+=1
                RecommendFailBanks.append(Banks_code[i])
    
    print('---比對結果:---')
    print(f'成功數目:銀行名稱:{Banks_name_success}, 銀行網址:{Banks_url_success}, 銀行圖片:{Banks_picture_success}, 銀行狀態:{Banks_status_success}, 銀行推薦:{Banks_recommend_success}')
    print(f'失敗數目:銀行名稱:{Banks_name_failed}, 銀行網址:{Banks_url_failed}, 銀行圖片:{Banks_picture_failed}, 銀行狀態:{Banks_status_failed}, 銀行推薦:{Banks_recommend_failed}')
    print()
    if len(NameFailBanks)>0:
        print(f'失敗銀行代號(名稱):{NameFailBanks}')
    if len(UrlFailBanks)>0:
        print(f'失敗銀行代號(網址):{UrlFailBanks}')
    if len(PicFailBanks)>0:
        print(f'失敗銀行代號(圖片):{PicFailBanks}')
    if len(StatusFailBanks)>0:
        print(f'失敗銀行代號(狀態):{StatusFailBanks}')
    if len(RecommendFailBanks)>0:
        print(f'失敗銀行代號(推薦):{RecommendFailBanks}')

def MCA_CheckBanksType_in_brands():
    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank') #銀行管理頁面
    browser.implicitly_wait(5)
    time.sleep(2)

    # 選品牌名稱
    BrandList=[] #16 ['3h', '測試']
    # 點下拉選單
    browser.find_element(By.XPATH,value='//div[@class="ps-query-container__optional"]/div[1]/div[@class="el-form-item__content"]/div[@class="el-select"]/div/div[@class="el-input el-input--suffix"]/div[@class="el-input__wrapper"]/input').click()
    time.sleep(1)
    BrandNames=browser.find_elements(By.XPATH,value='//div[@class="el-popper is-pure is-light el-select__popper"][1]/div/div/div[1]/ul/li')
    for res in BrandNames:
        Name=res.text
        if Name not in ['模控后台(预设值)']:
            BrandList.append(Name)
    # print(len(BrandList)) #len=16
    print('test1')
    if len(BrandList) != MCA_SyncManagement(): #16
        print('test2')
        print(f'{len(BrandList)} != {MCA_SyncManagement()}')
        print(BrandList)
        raise ValueError('銀行管理品牌名稱數量和同步管理不一致')
    browser.quit()
    # 會登出 要分開寫

    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-uat.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank') #銀行管理頁面
    browser.implicitly_wait(5)
    time.sleep(2)

    # BrandList[0]=li[2] max=li[17] = BrandList[15]
    Banks_code=[]
    Failed_Banks_type=[]
    for i in range(len(BrandList)):
        Banks_type_success=0
        Banks_type_failed=0
        if Banks_type_success and Banks_type_failed != 0:
            raise ValueError('變數未歸零')

        if BrandList[i] not in ['測試']:
            # 分別選擇各品牌
            num=str(i+2) #2456
            # 點下拉選單
            browser.find_element(By.XPATH,value='//div[@class="ps-query-container__optional"]/div[1]/div[@class="el-form-item__content"]/div[@class="el-select"]/div/div[@class="el-input el-input--suffix"]/div[@class="el-input__wrapper"]/input').click()
            time.sleep(1)
            browser.find_element(By.XPATH,value='/html/body/div[2]/div[2]/div/div/div[1]/ul/li['+num+']').click() #選擇各品牌
            browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button').click() #查找按鈕
            time.sleep(1)

            TotalBank=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div/span[1]').text
            print(f'{BrandList[i]} {TotalBank} num={num}') #共 193 条
            BNum=TotalBank.split(' ')
            Endpage=int(BNum[1])/30+2 #8
        
            for j in range(1,int(Endpage)):
                # 先爬代號
                BanksCode=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
                for res in BanksCode:
                    Banks_code.append(res.text)

                # 爬銀行類型
                BanksType=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[6]/div/span')
                for res in BanksType:
                    Type=res.text
                    if Type != '':
                        Banks_type_success+=1
                    else:
                        Banks_type_failed+=1
                        Failed_Banks_type.append(BrandList[i]+' '+Banks_code[i]) #品牌+代號
                
                # 下一頁
                if j<int(Endpage)-1: #11-1
                    NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
                    time.sleep(1)
            print(f'{Banks_type_success} 家銀行正常顯示')
            if Banks_type_failed>0:
                print(f'{Banks_type_failed} 家顯示空白')
                print(Failed_Banks_type)
            
            print('---------------')
            # 頁面重整
            browser.get('https://central-web-uat.paradise-soft.com.tw/brand-setting/brand.bank')
            browser.implicitly_wait(5)
            time.sleep(2)

    time.sleep(2)
    browser.quit()


if __name__=='__main__':
    MCA_CheckBanks_Contents()
    # MCA_CheckBanksType_in_brands()