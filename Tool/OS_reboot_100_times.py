import sys
sys.path.append('C:\\Users\\Stephenhuang\\Python')
from Library.SMASH import ssh_reboot
from Library.Redfish_requests import GET, POST
from Library.Common_Func import Check_PWD
from requests.exceptions import HTTPError, ConnectTimeout, ConnectionError
import subprocess
import unittest
from time import sleep

def Check_ipaddr(ip):
    command = 'ping -n 3 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0

def Check_Host_in_OS(ip, file):
    stdout = ssh_reboot(ip=ip, cmd='ip add')
    Checkpoint = ['Enable' for i in stdout if '169.254.3' in i]
    if len(Checkpoint) > 0:
        file.write('Host interface Enable on OS\n')
    else:
        file.write('Host interface Disable on OS\n') 
    return len(Checkpoint) > 0

def Check_Host_in_Redfish(ip, auth, file):
    Check = GET(url='https://'+ip+'/redfish/v1//Managers/1/EthernetInterfaces/ToHost', auth=auth)
    if Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == True:
        file.write('Host interface Enable on Redfish\n') #Data write

    elif Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == False:
        file.write('Host interface Disable on Redfish\n') #Data write
    else:
        file.write(f'Status code: {Check[0]}\nContent:{Check[1]}\n')
        
    return Check[-1].json()['InterfaceEnabled'] == True

def Get_PostCode(ip, auth, file):
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
                # print(f"{count}. PostCode = {kdata['PostCode']}")
                file.write(str(count)+". PostCode = "+str(kdata['PostCode'])+'\n')

                if kdata['PostCode'] in ['00', '0000']:
                    file.write(str(count)+". PostCode = "+str(kdata['PostCode'])+'\n')
                    return f"{count}. PostCode = {kdata['PostCode']}"
                
                if count >= 200 and kdata['PostCode'] not in ['00', '0000']:
                    # print(f"Current Post Code is {kdata['PostCode']}")
                    file.write("Current Post Code is "+str(kdata['PostCode'])+'\n'+'ForceRestart')
                    POST_collection.append(kdata['PostCode'])
                    reboot_count+=1
                    POST(url='https://'+ip+'/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/', auth=auth, body={"ResetType": "ForceRestart"})
                    sleep(2)
                    count = 0
            else:
                # print(f"Reboot {reboot_count} times but unable to boot into OS\nPOST Code on each time {POST_collection}")
                file.write(f"Reboot {reboot_count} times but unable to boot into OS\nPOST Code on each time {POST_collection}")
                file.write(str(POST_collection))
                return POST_collection
            sleep(3)
    else:
        # print(f"PostCode = {jdata['PostCode']}")
        return f"PostCode = {jdata['PostCode']}"

def OS_reboot_loop(times:int):
    file = open('log.txt', 'w')
    count = 0
    Fail_list = []
    for _ in range(int(times)):       
        try:
            if Check_ipaddr(ip=os_ip):
                ssh_reboot(ip=os_ip, cmd='reboot')
            else:
                POST(url='https://'+bmc_ip+'/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/', auth=auth, body={"ResetType": "ForceRestart"})
            
            count+=1
            file.write(f'NO.{count}\n')

            Check_PostCode = Get_PostCode(ip=bmc_ip, auth=auth, file=file)
            file.write(Check_PostCode)

            PingOS = Check_ipaddr(ip=os_ip)
            if PingOS:
                file.write('\nBoot into OS\n')
                if not Check_Host_in_OS(ip=os_ip, file=file):
                    Fail_list.append(f'NO.{count} Disable')
       
            elif PingOS == False and '00' in Check_PostCode:
                file.write('\nTry again!\n')
                sleep(90)
                if Check_ipaddr(ip=os_ip):
                    file.write('Boot into OS\n')
                    if not Check_Host_in_OS(ip=os_ip, file=file):
                        Fail_list.append(f'NO.{count} Disable')
                else:
                    file.write('\nBoot failed\n')
            else:    
                file.write('\nBoot failed\n')

        except HTTPError as e:
            file.write(str(e)+'\n')
            continue
        except ConnectTimeout as e:
            file.write(str(e)+'\n')
            continue
        except ConnectionError as e:
            file.write(str(e)+'\n')
            continue
        except TypeError as e:
            file.write(str(e)+'\n')
            continue
    file.close()
    print(f'Reboot {count} times\nRun PASS') if len(Fail_list) == 0 else print(f'{Fail_list}\nReboot {count} times\nRun FAIL')

class OSRebootTest(unittest.TestCase):
    def test(self):
        OS_reboot_loop(2)

if __name__=='__main__':
    bmc_ip = '172.31.34.91'
    os_ip = '172.31.32.118'
    auth = Check_PWD(ip=bmc_ip, unique='WCTFDPTATX')
    unittest.main()   

