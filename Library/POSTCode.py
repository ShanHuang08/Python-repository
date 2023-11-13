# from Library.Redfish_requests import *
from time import sleep
from Redfish_requests import *
from SUT import Check_PWD

ip = '10.184.26.167'
auth = Check_PWD(ip)

def Get_PostCode(ip, auth):
    # 寫個while loop, power state on = False. off = True
    jdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1]
    if jdata['PostCode'] != '00':
        count = 0
        while True:
            kdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1]
            count+=1
            print(f"{count}. PostCode = {kdata['PostCode']}")
            if kdata['PostCode'] == '00':
                break
            sleep(3)
    else:
        print(jdata['PostCode'])

Get_PostCode(ip, auth)
