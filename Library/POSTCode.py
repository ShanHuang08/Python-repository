from time import sleep
from Redfish_requests import *
import re

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False

def Check_PWD(ip, pwd):
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        return ('ADMIN', pwd)

def Get_PostCode(ip, auth):
    # 寫個while loop, power state on = False. off = True
    jdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
    if jdata['PostCode'] not in ['00', '0000']:
        count = 0
        reboot_count = 0
        POST_collection = []
        while True:
            kdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1].json()
            count+=1
            if reboot_count < 10:
                print(f"{count}. PostCode = {kdata['PostCode']}")

                if kdata['PostCode'] in ['00', '0000']:
                  return f"{count}. PostCode = {kdata['PostCode']}"
                
                if count >= 2000 and kdata['PostCode'] not in ['00', '0000']:
                    print(f"Current Post Code is {kdata['PostCode']}\nForceRestart")
                    POST_collection.append(kdata['PostCode'])
                    reboot_count+=1
                    # POST(url='https://'+ip+'/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/', auth=auth, body={"ResetType": "ForceRestart"})
                    sleep(2)
                    count = 0
            else:
                print(f"Reboot {reboot_count} times but unable to boot into OS\nPOST Code on each time {POST_collection}")
                return POST_collection
            sleep(3)
    else:
        print(f"PostCode = {jdata['PostCode']}")
        return f"PostCode = {jdata['PostCode']}"
    
if __name__=='__main__':
    ip = '172.31.35.195'
    auth = Check_PWD(ip, pwd='ALTWNBOQAN')
    Get_PostCode(ip, auth)
