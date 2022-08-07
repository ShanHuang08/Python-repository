#coding=utf-8
from tokenize import String
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--headless')
PATH='./chromedriver.exe'
browser=webdriver.Chrome(PATH,options=options)
browser.get('https://www.ifreesite.com/population/')

Countries=browser.find_elements(By.XPATH,value='//table[@class="if_tabletd"]/tbody/tr/td/table/tbody/tr/td[@width="50%"]/div')

Scraping_result=[]
for country in Countries:
#     print(country.text)
    Scraping_result.append(country.text)
# print(len(Scraping_result))

AllList=[]
for i in range(len(Scraping_result)):
    StringText=Scraping_result[i]
    AllList.append(StringText)
# print(AllList)

# 刪除空集合
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
    PopulationText=int(PopulationText)
    Population.append(PopulationText)
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

for i in range(len(ResultList)//2):
    print(f'NO.{i+1}. {ResultList[0+2*i]}:{ResultList[1+2*i]}')

browser.quit()
