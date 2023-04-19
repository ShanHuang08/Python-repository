<<<<<<< HEAD
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
ws.title='世界人口排名'
ws.append(['洲名','國家','人口'])
options=Options()
options.add_argument('--headless')
PATH='./chromedriver.exe'
browser=webdriver.Chrome(PATH,options=options)
browser.get('https://www.ifreesite.com/population/')

Continents=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@class="if_table starj taggllj"]')
Countries=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@width="50%"]/div')

CtnsList=[]
for ctns in Continents:
    CtnsList.append(ctns.text)
# print(len(TerrList)) #len=12

EngTerr=[]
ChnTerr=[]
for i in range(len(CtnsList)//2):
    ChnTerr.append(CtnsList[0+2*i])
    EngTerr.append(CtnsList[1+2*i])

for i in range(len(ChnTerr)):
    ChnTerr[i]=ChnTerr[i]+'('+EngTerr[i]+')'
# print(ChnTerr) #['非洲(AFRICA)', '亞洲(ASIA)', '歐洲(EUROPE)', '拉美和加勒比(LATIN AMERICA AND THE CARIBBEAN)', '北美(NORTHERN AMERICA)', '大洋洲(OCEANIA)']
AllList=[]
for country in Countries:
    GetData=[]
    GetData.append(country.text)
    # 把['']變成空陣列
    if GetData==['']:
        GetData.pop(0)
    # print(len(GetData),GetData)
    if len(GetData)==1:
        AllList.append(GetData[0])

EngCountryList=[]
Population=[]
ChnCountryList=[]
for i in range(len(AllList)):
    StringText2=AllList[i].split('|')
    EngCountryList.append(StringText2[0][0:-1]) #[0:-1] 去掉最後一位的空格
    # print(StringText2)
    StringText3=StringText2[1].split('\n')
    # print(StringText3)
    PopulationText=StringText3[0][1:].split(',')
    # print(PopulationText) #len=1,2,3,4
    if len(PopulationText)==1:
        PopulationText=PopulationText[0]
    elif len(PopulationText)==2:
        PopulationText=PopulationText[0]+PopulationText[1]
    elif len(PopulationText)==3:
        PopulationText=PopulationText[0]+PopulationText[1]+PopulationText[2]
    elif len(PopulationText)==4:
        PopulationText=PopulationText[0]+PopulationText[1]+PopulationText[2]+PopulationText[3]
    # print(PopulationText) #str
    PopulationNum=int(PopulationText)
    Population.append(PopulationNum)
    ChnCountryList.append(StringText3[1])

for i in range(len(EngCountryList)):
    EngCountryList[i]=EngCountryList[i]+'('+ChnCountryList[i]+')'

# 有六大洲 做六次處理
leng=[len(AllList[0:58]),len(AllList[58:109]),len(AllList[109:157]),len(AllList[157:205]),len(AllList[205:210]),len(AllList[210:233])]
ctnsum=0
for s in range(len(leng)):
    ctnsum=ctnsum+leng[s]
    if s==0:
        x=0
        y=leng[s]
    elif s>0:
        x=ctnsum-leng[s]
        y=ctnsum

    # 字典
    dictList={EngCountryList[i]:Population[i] for i in range(x,y)} 
    # print(dictList) #OK
    PopulationCompare=sorted(dictList.items(),key=lambda t:t[1])
    # print(PopulationCompare) #OK
    CTN_Result=[]
    for i in range(len(AllList[x:y])-1,-1,-1): 
        for j in range(2):
            CTN_Result.append(PopulationCompare[i][j])

    # 人口加逗號
    b=[]
    for i in range(len(CTN_Result)//2):
        ss=''.join(str(CTN_Result[1+2*i]))
        b.append(ss)

    for i in range(len(b)):
        length=0
        for j in b[i]:
            length+=1
        # print(f'a={length}') #10
        if length==10:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
        elif length>=7 and length<=9:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
        elif length>=4 and length<=6:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
        else:    
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:3])

    ws.append([ChnTerr[s]]) 
    for i in range(len(CTN_Result)//2):
        res=[]
        res.append('')
        res.append(CTN_Result[0+2*i])
        res.append(CTN_Result[1+2*i])
        ws.append(res)


wb.save('WorldPopulation.xlsx')
=======
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
ws.title='世界人口排名'
ws.append(['洲名','國家','人口'])
options=Options()
options.add_argument('--headless')
PATH='./chromedriver.exe'
browser=webdriver.Chrome(PATH,options=options)
browser.get('https://www.ifreesite.com/population/')

Continents=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@class="if_table starj taggllj"]')
Countries=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@width="50%"]/div')

CtnsList=[]
for ctns in Continents:
    CtnsList.append(ctns.text)
# print(len(TerrList)) #len=12

EngTerr=[]
ChnTerr=[]
for i in range(len(CtnsList)//2):
    ChnTerr.append(CtnsList[0+2*i])
    EngTerr.append(CtnsList[1+2*i])

for i in range(len(ChnTerr)):
    ChnTerr[i]=ChnTerr[i]+'('+EngTerr[i]+')'
# print(ChnTerr) #['非洲(AFRICA)', '亞洲(ASIA)', '歐洲(EUROPE)', '拉美和加勒比(LATIN AMERICA AND THE CARIBBEAN)', '北美(NORTHERN AMERICA)', '大洋洲(OCEANIA)']
AllList=[]
for country in Countries:
    GetData=[]
    GetData.append(country.text)
    # 把['']變成空陣列
    if GetData==['']:
        GetData.pop(0)
    # print(len(GetData),GetData)
    if len(GetData)==1:
        AllList.append(GetData[0])

EngCountryList=[]
Population=[]
ChnCountryList=[]
for i in range(len(AllList)):
    StringText2=AllList[i].split('|')
    EngCountryList.append(StringText2[0][0:-1]) #[0:-1] 去掉最後一位的空格
    # print(StringText2)
    StringText3=StringText2[1].split('\n')
    # print(StringText3)
    PopulationText=StringText3[0][1:].split(',')
    # print(PopulationText) #len=1,2,3,4
    if len(PopulationText)==1:
        PopulationText=PopulationText[0]
    elif len(PopulationText)==2:
        PopulationText=PopulationText[0]+PopulationText[1]
    elif len(PopulationText)==3:
        PopulationText=PopulationText[0]+PopulationText[1]+PopulationText[2]
    elif len(PopulationText)==4:
        PopulationText=PopulationText[0]+PopulationText[1]+PopulationText[2]+PopulationText[3]
    # print(PopulationText) #str
    PopulationNum=int(PopulationText)
    Population.append(PopulationNum)
    ChnCountryList.append(StringText3[1])

for i in range(len(EngCountryList)):
    EngCountryList[i]=EngCountryList[i]+'('+ChnCountryList[i]+')'

# 有六大洲 做六次處理
leng=[len(AllList[0:58]),len(AllList[58:109]),len(AllList[109:157]),len(AllList[157:205]),len(AllList[205:210]),len(AllList[210:233])]
ctnsum=0
for s in range(len(leng)):
    ctnsum=ctnsum+leng[s]
    if s==0:
        x=0
        y=leng[s]
    elif s>0:
        x=ctnsum-leng[s]
        y=ctnsum

    # 字典
    dictList={EngCountryList[i]:Population[i] for i in range(x,y)} 
    # print(dictList) #OK
    PopulationCompare=sorted(dictList.items(),key=lambda t:t[1])
    # print(PopulationCompare) #OK
    CTN_Result=[]
    for i in range(len(AllList[x:y])-1,-1,-1): 
        for j in range(2):
            CTN_Result.append(PopulationCompare[i][j])

    # 人口加逗號
    b=[]
    for i in range(len(CTN_Result)//2):
        ss=''.join(str(CTN_Result[1+2*i]))
        b.append(ss)

    for i in range(len(b)):
        length=0
        for j in b[i]:
            length+=1
        # print(f'a={length}') #10
        if length==10:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
        elif length>=7 and length<=9:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
        elif length>=4 and length<=6:
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
        else:    
            CTN_Result.pop(1+2*i)
            CTN_Result.insert(1+2*i,b[i][0:3])

    ws.append([ChnTerr[s]]) 
    for i in range(len(CTN_Result)//2):
        res=[]
        res.append('')
        res.append(CTN_Result[0+2*i])
        res.append(CTN_Result[1+2*i])
        ws.append(res)


wb.save('WorldPopulation.xlsx')
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
browser.quit()