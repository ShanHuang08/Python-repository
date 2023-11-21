from Library.Redfish_requests import *
from time import sleep
# from Redfish_requests import *

ip = '172.31.32.216'

def Check_PWD(ip):
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        pwd = input('Input unique password: ')
        return ('ADMIN', pwd)

def Get_PostCode(ip, auth):
    # 寫個while loop, power state on = False. off = True
    jdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
    if jdata['PostCode'] != '00':
        count = 0
        while True:
            kdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
            count+=1
            # print(f"{count}. PostCode = {kdata['PostCode']}")
            if kdata['PostCode'] == '00':
                return f"{count}. PostCode = {kdata['PostCode']}"
            if count > 200 and kdata['PostCode'] != '00':
                # use redfish to reboot and select OS
                sleep(2)
            sleep(3)
    else:
        # print(jdata['PostCode'])
        return f"1. PostCode = {jdata['PostCode']}"
    
if __name__=='__main__':
    auth = Check_PWD(ip)
    Get_PostCode(ip, auth)
