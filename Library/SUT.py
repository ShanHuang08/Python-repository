from dictionary import SUT
from Redfish_requests import *

def AddSUT():
    key = input("SUT: ")
    BMC_IP = input("BMC IP: ")
    OS_IP = input("OS IP: ")
    SUT_info = {key : {"BMC" : BMC_IP, "OS" : OS_IP}}
    print(str(SUT_info)[1:-1])

def Check_PWD(ip):
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        pwd = input('Input unique password: ')
        return ('ADMIN', pwd)

def GetFWInfo(ip:str):
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

if __name__=='__main__':
    # AddSUT()
    GetFWInfo('172.31.32.94')

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'