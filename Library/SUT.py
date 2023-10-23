from Library.dictionary import SUT
from pprint import pprint
from Library.Redfish_requests import *

def PrintSUT():
    pprint(SUT)
    return SUT

def Check_PWD(ip):
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        pwd = input('Input unique password: ')
        return ('ADMIN', pwd)

def GetFWInfo():
    ip = input('Input BMC IP: ')
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    auth = Check_PWD(ip)
    BMC_Data = None
    Check_Pwd = GET(url='https://'+ip+'/redfish/v1/Systems', auth=auth)

    if Check_Pwd[0] == 200:
        try:
            BMC_Data = GET(url=url+'BMC', auth=auth)
            BIOS_Data = GET(url=url+'BIOS', auth=auth)
            # print(BMC_Data['Version'])
            BMC_FW = BMC_Data[-1]['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1]['Oem']['Supermicro']['UniqueFilename']
            return print(f"{BMC_FW}\n{BIOS_FW}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1]}\nBIOS Data: {BIOS_Data[-1]}")
    else:
        return print(f"Status code: {Check_Pwd[0]}\n{Check_Pwd[1]}")


# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'