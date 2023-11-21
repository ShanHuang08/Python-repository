from Library.Redfish_requests import *
from time import sleep
# from Redfish_requests import *
from Library.Strings import Check_PWD

ip = '172.31.32.216'


def Get_PostCode(ip, auth):
    # 寫個while loop, power state on = False. off = True
    jdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
    if jdata['PostCode'] != '00':
        count = 0
        while True:
            kdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
            count+=1
            print(f"{count}. PostCode = {kdata['PostCode']}")
            if kdata['PostCode'] == '00':
                break
            sleep(3)
    else:
        print(jdata['PostCode'])
if __name__=='__main__':
    auth = Check_PWD(ip)
    Get_PostCode(ip, auth)
