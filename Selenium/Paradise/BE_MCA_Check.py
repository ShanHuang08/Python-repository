#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from BE_InfoControl import *
from BE_MCA_Sync import MCA_SyncManagement, MCA_SyncOnManagement
from BrandJSON import BE_BrandJSON
from MCA_datetime import MCAToday

branch=MCA_branch()
def MCA_CheckBanks_Contents():
    excluce_code=['123','Miles','test','ABC123','ABABAB','AAAC','AAA']  #bh has AAAC bank
    exclude_name=['測測一','MBANK','ewqewqe','123321','四川川川川川银行','名称名称','AAA'] #
    exclude_url=['wwwyyy','test','555555','https://www.scbank.cnn/','c','aa'] #
    exclude_pic=['http://stage.squirrel.pstdsf.com/brand-image/base/bank/aaa.jpeg?1668585592','https://squirrel-'+branch+'.paradise-soft.com.tw/brand-image/base/bank/aaac.jpeg?1668406375','https://squirrel-'+branch+'.paradise-soft.com.tw/brand-image/base/bank/ababab.jpeg?1667984438','https://squirrel-'+branch+'.paradise-soft.com.tw//brand-image/base/bank/123.png?1667458982','https://squirrel-'+branch+'.paradise-soft.com.tw//brand-image/base/bank/abc123.jpeg?1667384821','https://squirrel-'+branch+'.paradise-soft.com.tw//brand-image/base/bank/miles.png?1666681915','https://squirrel-'+branch+'.paradise-soft.com.tw//brand-image/base/bank/test.jpeg?1666860254']
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

    # options=Options() 
    # options.add_argument('--headless')
    # browser=webdriver.Chrome('./Chromedriver.exe', options=options)
    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    if branch == 'uat':
        browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    else:
        browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/brand-setting/brand.bank')
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
        BankNames=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[4]/div')
        BankUrls=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[5]/div')
        BankPics=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div/img')
        BankStatus=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span')
        BanksRec=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[8]/div/span')
        # print(BankCodes.text)
        for res in BankCodes: #len=191
            Banks_code_for_exclude.append(res.text) #len=193
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
    # print(Banks_status)
    # exclude i=121 Miles, i=164 test
    for i in range((len(Banks_code_for_exclude)-1),-1,-1): #Pop()要用逆迴圈刪除．從後面刪到前面，才不會刪錯
        if Banks_code_for_exclude[i] in excluce_code:
            Banks_status.pop(i)
            Banks_recommend.pop(i)
            # print('i='+str(i), Banks_code_for_exclude[i])
            # print(Banks_status)

    print(f'銀行數目:{len(Banks_code)}, 名稱:{len(Banks_name)}, 網址:{len(Banks_url)}, 圖片:{len(Banks_picture)}, 狀態:{len(Banks_status)}, 推薦:{len(Banks_recommend)}') #len=193 扣掉無效銀行=190+1

    # print(len(Banks_picture))
    # print(Banks)
    browser.quit()
    
    #Get api info, return jdata(各品牌) call到這裡
    jdata=BE_BrandJSON()
    #檢查品牌是否有新增銀行, 把JSON codes抓下來, 改用set做差集
    jdata_list=[]
    for i in range(jdata['Pager']['Total']):
        jdata_list.append(jdata['Items'][i]['code'])

    if jdata['Pager']['Total'] == len(Banks_code):
        pass
    elif jdata['Pager']['Total'] > len(Banks_code):
        jdataB=set(jdata_list)
        central=set(Banks_code)
        Code_diff=list(jdataB-central) #set差集 大-小
    elif jdata['Pager']['Total'] < len(Banks_code):
        central=set(Banks_code)
        jdataB=set(jdata_list)
        Code_diff=list(central-jdataB) #set差集 大-小


    # Raise error if lengths aren't the same
    if len(Banks_name) != len(jdata['Items']):
        print(f'names({len(Banks_name)}) != jdata({jdata["Pager"]["Total"]})')
        print(f'diff bank code = {Code_diff}')
        raise ValueError('Unable to make a comparison. Name lengths are not the same!')
    elif len(Banks_url) != len(jdata['Items']):
        print(f'urls({len(Banks_url)}) != jdata({jdata["Pager"]["Total"]})')
        raise ValueError('Unable to make a comparison. Url lengths are not the same!')
    elif len(Banks_picture) != len(jdata['Items']):
        print(f'pictures({len(Banks_picture)}) != jdata({jdata["Pager"]["Total"]})')
        raise ValueError('Unable to make a comparison. Picture lengths are not the same!')
    elif len(Banks_status) != len(jdata['Items']):
        print(f'pictures({len(Banks_status)}) != jdata({jdata["Pager"]["Total"]})')
        raise ValueError('Unable to make a comparison. Status lengths are not the same!')
    elif len(Banks_recommend) != len(jdata['Items']):
        print(f'pictures({len(Banks_recommend)}) != jdata({jdata["Pager"]["Total"]})')
        raise ValueError('Unable to make a comparison. Recommend lengths are not the same!')

    for i in range(len(jdata['Items'])): #len=191
            if jdata['Items'][i]['name'] == Banks_name[i]:
                Banks_name_success+=1
            else:
                Banks_name_failed+=1
                NameFailBanks.append(Banks_code[i])
            
            if jdata['Items'][i]['url'] == Banks_url[i]: #IndexError: list index out of range
                Banks_url_success+=1
            elif Banks_url[i]=='':
                Banks_url_success+=1 
            else:
                Banks_url_failed+=1
                UrlFailBanks.append(Banks_code[i])
            
            # if jdata['Items'][i]['imgpath'][0:4] == Banks_picture[i][0:4] and jdata['Items'][i]['imgpath'][-(len(Banks_code[i])+4):-1]+jdata['Items'][i]['imgpath'][-1]==Banks_picture[i][-(len(Banks_code[i])+15):-11]: #圖片網址比對有問題
            if jdata['Items'][i]['imgpath'][0:4] == Banks_picture[i][0:4]:
            # if jdata['Items'][i]['imgpath'][-(len(Banks_code[i])+4):-1]+jdata['Items'][i]['imgpath'][-1]==Banks_picture[i][-(len(Banks_code[i])+15):-11]:
                Banks_picture_success+=1
            else:
                Banks_picture_failed+=1
                PicFailBanks.append(Banks_code[i])
            
            if jdata['Items'][i]['status'] == Banks_status[i]:
                Banks_status_success+=1
            else:
                Banks_status_failed+=1
                StatusFailBanks.append(Banks_code[i])
                # print(Banks_code[i], jdata['Items'][i]['status'], Banks_status[i])

            if jdata['Items'][i]['recommend'] == Banks_recommend[i]:
                Banks_recommend_success+=1
            else:
                Banks_recommend_failed+=1
                RecommendFailBanks.append(Banks_code[i])
                # print(Banks_code[i], jdata['Items'][i]['status'], Banks_status[i])
    
    print('---比對結果:---')
    print(f'成功數目:銀行名稱:{Banks_name_success}, 銀行網址:{Banks_url_success}, 銀行圖片:{Banks_picture_success}, 銀行狀態:{Banks_status_success}, 銀行推薦:{Banks_recommend_success}')
    print(f'失敗數目:銀行名稱:{Banks_name_failed}, 銀行網址:{Banks_url_failed}, 銀行圖片:{Banks_picture_failed}, 銀行狀態:{Banks_status_failed}, 銀行推薦:{Banks_recommend_failed}')

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

def MCA_CheckBanksSync_in_brands():
    # options=Options() 
    # options.add_argument('--headless')
    # browser=webdriver.Chrome('./Chromedriver.exe', options=options)
    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    if branch == 'uat':
        browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    else:
        browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/brand-setting/brand.bank') #銀行管理頁面
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
    if MCA_SyncManagement() == 0:
        raise ValueError('同步管理未設定')
    elif MCA_SyncOnManagement() == 0:
        raise ValueError('同步管理品牌未開啟')
    if len(BrandList) != MCA_SyncManagement(): #16
        print(f'{len(BrandList)} != {MCA_SyncManagement()}')
        print(BrandList)
        raise ValueError('銀行管理品牌名稱數量和同步管理不一致')
    browser.quit()
    # 會登出 要分開寫

    # browser=webdriver.Chrome('./Chromedriver.exe', options=options)
    browser=webdriver.Chrome('./Chromedriver.exe')
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/')
    browser.maximize_window()
    time.sleep(1)
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录帐号"]').send_keys(BE_account())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入登录密码"]').send_keys(BE_password())
    browser.find_element(By.XPATH,value='//input[@placeholder="请输入OTP"]').send_keys(1)
    browser.find_element(By.XPATH,value='//*[@id="app"]/div/form/button').click()
    time.sleep(1)
    browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/brand-setting/brand.bank') #銀行管理頁面
    browser.implicitly_wait(5)
    time.sleep(2)

    # BrandList[0]=li[2] max=li[17] = BrandList[15]
    Banks_code=[]
    Failed_Banks_type=[]
    Failed_Banks_sync=[]
    for i in range(len(BrandList)):
        Banks_type_success=0
        Banks_type_failed=0
        Banks_sync_success=0
        Banks_sync_failed=0
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
            print(f'{BrandList[i]} {TotalBank}') #共 193 条
            BNum=TotalBank.split(' ')
            Endpage=int(BNum[1])/30+2 #8
            if int(BNum[1])==0:
                ErrorMsg='銀行數目為'+BNum[1]
                browser.quit()
                raise ValueError(ErrorMsg)
        
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
                
                # 爬同步時間
                BanksSyncTime=browser.find_elements(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[9]/div/span')
                for res in BanksSyncTime:
                    Time=res.text
                    if Time != '' and Time[0:10]==MCAToday():
                        Banks_sync_success+=1
                    else:
                        Banks_sync_failed+=1
                        Failed_Banks_sync.append(BrandList[i]+' '+Banks_code[i]) #品牌+代號

                    
                # 下一頁
                if j<int(Endpage)-1: #11-1
                    NextPage=browser.find_element(By.XPATH,value='//div[@class="ps-pager"]/div[@role="pagination"]/button[@class="btn-next"]').click()
                    time.sleep(1)
            # 列印結果
            print(f'{Banks_type_success} 家銀行正常顯示')
            if Banks_type_failed>0:
                print(f'{Banks_type_failed} 家顯示空白')
                print(Failed_Banks_type)
            print(f'{Banks_sync_success} 家銀行成功在{MCAToday()}做批量同步')
            if Banks_sync_failed>0:
                print(f'{Banks_sync_failed} 家銀行沒有同步')
                print(Failed_Banks_sync)

            print('---------------')
            # 頁面重整
            browser.get('https://central-web-'+branch+'.paradise-soft.com.tw/brand-setting/brand.bank')
            browser.implicitly_wait(5)
            time.sleep(2)

    time.sleep(2)
    browser.quit()


if __name__=='__main__':
    MCA_CheckBanks_Contents()
    # MCA_CheckBanksSync_in_brands()