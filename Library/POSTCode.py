# from Library.Redfish_requests import *
from time import sleep
from Redfish_requests import *



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
    if jdata['PostCode'] not in ['00', '0000']:
        count = 0
        while True:
            kdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
            count+=1
            print(f"{count}. PostCode = {kdata['PostCode']}")
            if kdata['PostCode'] in ['00', '0000']:
                print(f"{count}. PostCode = {kdata['PostCode']}")
                return f"{count}. PostCode = {kdata['PostCode']}"
            if count > 300 and kdata['PostCode'] not in ['00', '0000']:
                POST(url='https://'+ip+'/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/', auth=auth, body={"ResetType": "ForceRestart"})
                sleep(2)
            sleep(3)
    else:
        print(f"PostCode = {jdata['PostCode']}")
        return f"PostCode = {jdata['PostCode']}"
    
if __name__=='__main__':
    ip = '172.31.35.83'
    auth = Check_PWD(ip)
    Get_PostCode(ip, auth)
