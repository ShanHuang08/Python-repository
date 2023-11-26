from Library.SMASH import ssh_reboot
from Library.POSTCode import Get_PostCode
from Library.Redfish_requests import GET, POST
from Library.Call_Method import Check_PWD
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

            Check_PostCode = Get_PostCode(ip=bmc_ip, auth=auth)
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

            if Check_Host_in_Redfish(ip=bmc_ip, auth=auth, file=file):
                if count in [100, 150]:
                    print(f'NO.{count} Host interface Enable') 
            else:
                Fail_list.append(f'NO.{count} Disable')
                if count in [100, 150]:
                    print(f'NO.{count} Host interface Disable') 

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
        OS_reboot_loop(5)

if __name__=='__main__':
    bmc_ip = '10.184.16.55'
    os_ip = '10.184.21.44'
    auth = Check_PWD(ip=bmc_ip, unique='PEDRKBSHTO')
    unittest.main()   

