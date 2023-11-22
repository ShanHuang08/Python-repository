from Library.SMASH import ssh_reboot
from Library.POSTCode import Get_PostCode
from Library.Redfish_requests import GET, POST
from Library.Strings import Check_PWD
import requests
import subprocess
import unittest
from time import sleep

def Check_ipaddr(ip):
    command = 'ping -n 3 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text=''
    for line in List:
        if "TTL=" in line:
            Text+=line
    return len(Text) > 0

def Check_Host_in_OS(ip):
    Checkpoint = []
    stdout = ssh_reboot(ip=ip, cmd='ip add')
    for i in stdout:
        if '169.254.3' in i:
            Checkpoint.append('Enable')
    return Checkpoint

def Check_Host_Interface():
    file = open('log.txt', 'w')
    count = 0
    Fail_list = []
    for _ in range(150):       
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

                if len(Check_Host_in_OS(ip=os_ip)) > 0:
                    file.write('Host interface Enable on OS\n') 
                else:
                    file.write('Host interface Disable on OS\n') 
                    Fail_list.append(f'NO.{count} Disable')

            elif PingOS == False and '00' in Check_PostCode:
                file.write('\nTry again!\n')
                sleep(30)
                if Check_ipaddr(ip=os_ip):
                    file.write('Boot into OS\n')

                    if len(Check_Host_in_OS(ip=os_ip)) > 0:
                        file.write('Host interface Enable on OS\n') 
                    else:
                        file.write('Host interface Disable on OS\n') 
                        Fail_list.append(f'NO.{count} Disable')
                else:
                    file.write('\nBoot failed\n')
            else:    
                file.write('\nBoot failed\n')

            Check = GET(url='https://'+bmc_ip+'/redfish/v1//Managers/1/EthernetInterfaces/ToHost', auth=auth)
            if Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == True:
                file.write('Host interface Enable on Redfish\n') #Data write
                if count == 100 or count == 150:
                    print(f'NO.{count} Host interface Enable') 
            elif Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == False:
                file.write('Host interface Disable on Redfish\n') #Data write
                Fail_list.append(f'NO.{count} Disable')
                if count == 100 or count == 150:
                    print(f'NO.{count} Host interface Disable') 
            else:
                file.write(f'Status code: {Check[0]}\nContent:{Check[1]}\n')
            
        except requests.exceptions.HTTPError as e:
            file.write(str(e)+'\n')
            continue
        except requests.exceptions.ConnectTimeout as e:
            file.write(str(e)+'\n')
            continue
        except requests.exceptions.ConnectionError as e:
            file.write(str(e)+'\n')
            continue
        except TypeError as e:
            file.write(str(e)+'\n')
            continue

    file.close()
    print(f'Reboot {count} times\nRun PASS') if len(Fail_list) == 0 else print(f'Reboot {count} times\nRun FAIL')

class BMCResetTest(unittest.TestCase):
    def test(self):
        Check_Host_Interface()

if __name__=='__main__':
    bmc_ip = '10.184.25.25'
    os_ip = '10.184.22.137'
    auth = Check_PWD(ip=bmc_ip, unique='SMUVZINHBZ')
    unittest.main()   

