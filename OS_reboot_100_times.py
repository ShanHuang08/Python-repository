from Library.SMASH import ssh_reboot
from Library.POSTCode import Get_PostCode
from Library.Strings import Check_PWD
from Library.Redfish_requests import GET
import requests
os_ip = '10.184.22.137'
bmc_ip = '10.184.25.25'
auth = Check_PWD(bmc_ip)
"""
Reboot (cmd)
Check PostCode to confirm whether reboot is completed, PostCode == 00 will finish the function.  (Get_PostCode)
wait a few secs (time.sleep())
Check Host interface via Redfish (/redfish/v1//Managers/1/EthernetInterfaces/ToHost) GET {"InterfaceEnabled": true}
Check Host interface via OS (ip addr)
Data writes into log (log.txt) with open(filenaame, 'w')
Reboot 137 times (cmd)
print check info on 100 times and 150 times

"""

    
def Check_Host_Interface():
    Check = GET(url='https://'+bmc_ip+'/redfish/v1//Managers/1/EthernetInterfaces/ToHost', auth=auth)
    stdout = ssh_reboot(ip=os_ip, cmd='ip add')
    # testList = ['Enable' for i in stdout if '169.254.3' in i] 
    testList = []
    if Check[0] == 200 and Check[-1].json()['InterfaceEnabled'] == True:
        testList.append('Enable')
    for i in stdout:
        if '169.254.3' in i:
            testList.append('Enable')
    
    print('Host interface Enable') if len(testList) == 2 else print('Host interface Disable')
        

        


Check_Host_Interface()
# Get_PostCode(ip=bmc_ip, auth=auth)

#     for i in stdout:
# TypeError: 'NoneType' object is not iterable

# for _ in range(150):
#     try:    
#         function1()
#     except TypeError:
#         continue
#     except requests.exceptions.HTTPError:
#         continue
#     except requests.exceptions.ConnectTimeout:
#         continue
#     except requests.exceptions.ConnectionError:
#         continue