from Library.SMASH import ssh_reboot
from Library.POSTCode import Get_PostCode
from Library.Redfish_requests import GET
import requests
import subprocess
os_ip = '10.184.22.137'
bmc_ip = '10.184.25.25'

"""
Reboot (cmd)
Check PostCode to confirm whether reboot is completed, PostCode == 00 will finish the function.  (Get_PostCode) Need timeout
ping OS IP True=Boot into OS, False=Boot failed, Redfish reboot-> PostCode
Check Host interface via Redfish (/redfish/v1//Managers/1/EthernetInterfaces/ToHost) GET {"InterfaceEnabled": true}
Check Host interface via OS (ip addr)
Data writes into log (log.txt) with open(filenaame, 'w')
Reboot 137 or 150 times (cmd) 
Record the host interface disabled start from which times
print check info on 100 times and 150 times

"""
def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text=''
    for line in List:
        if "TTL=" in line:
            Text+=line
    return len(Text) > 0
    
def Check_Host_Interface():
    file = open('log.txt', 'w')
    count = 0
    Fail_list = []
    for _ in range(5):
        count+=1
        file.write(f'NO.{count}\n')
        try:
            if Check_ipaddr(ip=os_ip):
                ssh_reboot(ip=os_ip, cmd='reboot')
            else:
                pass
                #Use redfish to reboot

            file.write(Get_PostCode(ip=bmc_ip, auth=('ADMIN', 'ADMIN')))

            if Check_ipaddr(ip=os_ip):
                file.write('Boot into OS')
                stdout = ssh_reboot(ip=os_ip, cmd='ip add')
                for i in stdout:
                    if '169.254.3' in i:
                        file.write('Host interface Enable on OS\n') #Data write
                    else:
                        file.write('Host interface Disable on OS\n') #Data write
            else:
                file.write('Boot failed')

            Check = GET(url='https://'+bmc_ip+'/redfish/v1//Managers/1/EthernetInterfaces/ToHost', auth=('ADMIN', 'ADMIN'))
            if Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == True:
                file.write('Host interface Enable on Redfish\n') #Data write
                if count == 100 or count == 150:
                    print('Host interface Enable') 
            elif Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == False:
                file.write('Host interface Disable on Redfish\n') #Data write
                Fail_list.append(f'NO.{count} Disable')
                if count == 100 or count == 150:
                    print('Host interface Disable') 
            else:
                file.write(f'Status code: {Check[0]}\nContent:{Check[1]}\n')
            
        except requests.exceptions.HTTPError as e:
            file.write(str(e)+'\n')
            Fail_list.append(f'NO.{count} {e}')
            continue
        except requests.exceptions.ConnectTimeout as e:
            file.write(str(e)+'\n')
            Fail_list.append(f'NO.{count} {e}')
            continue
        except requests.exceptions.ConnectionError as e:
            file.write(str(e)+'\n')
            Fail_list.append(f'NO.{count} {e}')
            continue
        except TypeError as e:
            file.write(str(e)+'\n')
            Fail_list.append(f'NO.{count} {e}')
            continue

    file.close()
    print('Run PASS') if len(Fail_list) == 0 else print('Run FAIL')
        
if __name__=='__main__':
    Check_Host_Interface()     

