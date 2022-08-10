#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
ws.title='世界人口排名'
ws.append(['名次','國家','人口'])
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
    AllList.append(country.text)



# 刪除空陣列
AllList.pop(235)
AllList.pop(211)
AllList.pop(109)
# print(len(AllList[0:58])) #非洲(AFRICA) len=58
# print(len(AllList[58:109])) #亞洲(ASIA) len=51 109-58
# print(len(AllList[109:157])) #歐洲(EUROPE) len=48 157-109
# print(len(AllList[157:205])) #拉美和加勒比 len=48 205-157
# print(len(AllList[205:210])) #北美 len=5 210-205
# print(len(AllList[210:233])) #大洋洲 len=23 233-210

EngCountryList=[]
Population=[]
ChnCountryList=[]
for i in range(len(AllList)):
    StringText2=AllList[i].split('|')
    EngCountryList.append(StringText2[0])
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
# print(Population)

for i in range(len(EngCountryList)):
    EngCountryList[i]=EngCountryList[i]+'('+ChnCountryList[i]+')'
# print(EngCountryList[0:3])

# 六次字典
# 1
dictList={EngCountryList[i]:Population[i] for i in range(0,len(AllList[0:58]))}
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

AFR_Result=[]
for i in range(len(AllList[0:58])-1,-1,-1):
    for j in range(2):
        AFR_Result.append(PopulationCompare[i][j])
# print(AFR_Result)

# 2
dictList={EngCountryList[i]:Population[i] for i in range(len(AllList[0:58]),len(AllList[0:58])+len(AllList[58:109]))} #For loop範圍不對
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

ASIA_Result=[]
for i in range(len(AllList[58:109])-1,-1,-1):
    for j in range(2):
        ASIA_Result.append(PopulationCompare[i][j])
# print(ASIA_Result) 

# 3
dictList={EngCountryList[i]:Population[i] for i in range(len(AllList[0:58])+len(AllList[58:109]),len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157]))}
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

EUR_Result=[]
for i in range(len(AllList[109:157])-1,-1,-1):
    for j in range(2):
        EUR_Result.append(PopulationCompare[i][j])
# print(EUR_Result[0:6])

# 4
dictList={EngCountryList[i]:Population[i] for i in range(len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157]),len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157])+len(AllList[157:205]))}
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

LATIN_Result=[]
for i in range(len(AllList[157:205])-1,-1,-1):
    for j in range(2):
        LATIN_Result.append(PopulationCompare[i][j])
# print(LATIN_Result[0:6])

# 5
dictList={EngCountryList[i]:Population[i] for i in range(len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157])+len(AllList[157:205]),len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157])+len(AllList[157:205])+len(AllList[205:210]))}
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

NA_Result=[]
for i in range(len(AllList[205:210])-1,-1,-1):
    for j in range(2):
        NA_Result.append(PopulationCompare[i][j])
# print(NA_Result)

# 6
dictList={EngCountryList[i]:Population[i] for i in range(len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157])+len(AllList[157:205])+len(AllList[205:210]),len(AllList[0:58])+len(AllList[58:109])+len(AllList[109:157])+len(AllList[157:205])+len(AllList[205:210])+len(AllList[210:233]))}
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

OCE_Result=[]
for i in range(len(AllList[210:233])-1,-1,-1):
    for j in range(2):
        OCE_Result.append(PopulationCompare[i][j])
# print(OCE_Result)

# 人口加逗號
# 1
b=[]
for i in range(len(AFR_Result)//2):
    s=''.join(str(AFR_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        AFR_Result.pop(1+2*i)
        AFR_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        AFR_Result.pop(1+2*i)
        AFR_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        AFR_Result.pop(1+2*i)
        AFR_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        AFR_Result.pop(1+2*i)
        AFR_Result.insert(1+2*i,b[i][0:3])
# 2
b=[]
for i in range(len(ASIA_Result)//2):
    s=''.join(str(ASIA_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        ASIA_Result.pop(1+2*i)
        ASIA_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        ASIA_Result.pop(1+2*i)
        ASIA_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        ASIA_Result.pop(1+2*i)
        ASIA_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        ASIA_Result.pop(1+2*i)
        ASIA_Result.insert(1+2*i,b[i][0:3])  
# 3
b=[]
for i in range(len(EUR_Result)//2):
    s=''.join(str(EUR_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        EUR_Result.pop(1+2*i)
        EUR_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        EUR_Result.pop(1+2*i)
        EUR_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        EUR_Result.pop(1+2*i)
        EUR_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        EUR_Result.pop(1+2*i)
        EUR_Result.insert(1+2*i,b[i][0:3])  
# 4
b=[]
for i in range(len(LATIN_Result)//2):
    s=''.join(str(LATIN_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        LATIN_Result.pop(1+2*i)
        LATIN_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        LATIN_Result.pop(1+2*i)
        LATIN_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        LATIN_Result.pop(1+2*i)
        LATIN_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        LATIN_Result.pop(1+2*i)
        LATIN_Result.insert(1+2*i,b[i][0:3])  
# 5
b=[]
for i in range(len(NA_Result)//2):
    s=''.join(str(NA_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        NA_Result.pop(1+2*i)
        NA_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        NA_Result.pop(1+2*i)
        NA_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        NA_Result.pop(1+2*i)
        NA_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        NA_Result.pop(1+2*i)
        NA_Result.insert(1+2*i,b[i][0:3])  
# 6
b=[]
for i in range(len(OCE_Result)//2):
    s=''.join(str(OCE_Result[1+2*i]))
    b.append(s)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        OCE_Result.pop(1+2*i)
        OCE_Result.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        OCE_Result.pop(1+2*i)
        OCE_Result.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        OCE_Result.pop(1+2*i)
        OCE_Result.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        OCE_Result.pop(1+2*i)
        OCE_Result.insert(1+2*i,b[i][0:3])  

# 1
ws.append(['Continent',ChnTerr[0]])
for i in range(len(AFR_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(AFR_Result[0+2*i])
    res.append(AFR_Result[1+2*i])
    ws.append(res)
# 2
ws.append(['Continent',ChnTerr[1]])
for i in range(len(ASIA_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(ASIA_Result[0+2*i])
    res.append(ASIA_Result[1+2*i])
    ws.append(res)
# 3
ws.append(['Continent',ChnTerr[2]])
for i in range(len(EUR_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(EUR_Result[0+2*i])
    res.append(EUR_Result[1+2*i])
    ws.append(res)
# 4
ws.append(['Continent',ChnTerr[3]])
for i in range(len(LATIN_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(LATIN_Result[0+2*i])
    res.append(LATIN_Result[1+2*i])
    ws.append(res)    
# 5
ws.append(['Continent',ChnTerr[4]])
for i in range(len(NA_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(NA_Result[0+2*i])
    res.append(NA_Result[1+2*i])
    ws.append(res)
# 6
ws.append(['Continent',ChnTerr[5]])
for i in range(len(OCE_Result)//2):
    res=[]
    res.append('NO.'+str(i+1))
    res.append(OCE_Result[0+2*i])
    res.append(OCE_Result[1+2*i])
    ws.append(res)

wb.save('WorldPopulation.xlsx')
browser.quit()
