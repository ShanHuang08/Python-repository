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

Countries=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@width="50%"]/div')

AllList=[]
for country in Countries:
    AllList.append(country.text)
# print(AllList)

# 刪除空陣列
AllList.pop(235)
AllList.pop(211)
AllList.pop(109)
# print(AllList) 

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

for i in range(len(Population)):
    EngCountryList[i]=EngCountryList[i]+'('+ChnCountryList[i]+')'
# print(EngCountryList[0:3])

dictList={EngCountryList[i]:Population[i] for i in range(len(Population))}
# print(dictList)
PopulationCompare=sorted(dictList.items(),key=lambda s:s[1])
# print(PopulationCompare)

ResultList=[]
for i in range(len(Population)-1,-1,-1):
    for j in range(2):
        ResultList.append(PopulationCompare[i][j])
# print(ResultList[0:6])

# 人口加逗號
b=[]
for i in range(len(ResultList)//2):
    s=''.join(str(ResultList[1+2*i]))
    b.append(s)
# print(b)

for i in range(len(b)):
    length=0
    for j in b[i]:
        length+=1
    # print(f'a={length}') #10
    if length==10:
        ResultList.pop(1+2*i)
        ResultList.insert(1+2*i,b[i][0:1]+','+b[i][1:4]+','+b[i][4:7]+','+b[i][7:10])
    elif length>=7 and length<=9:
        ResultList.pop(1+2*i)
        ResultList.insert(1+2*i,b[i][0:length-6]+','+b[i][length-6:length-3]+','+b[i][length-3:length])
    elif length>=4 and length<=6:
        ResultList.pop(1+2*i)
        ResultList.insert(1+2*i,b[i][0:length-3]+','+b[i][length-3:length])
    else:    
        ResultList.pop(1+2*i)
        ResultList.insert(1+2*i,b[i][0:3])

for i in range(len(ResultList)//2):
    # print(f'NO.{i+1}. {ResultList[0+2*i]}:{ResultList[1+2*i]}')
    res=[]
    res.append('NO.'+str(i+1))
    res.append(ResultList[0+2*i])
    res.append(ResultList[1+2*i])
    ws.append(res)
wb.save('WorldPopulation.xlsx')
browser.quit()
