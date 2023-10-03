from Library.dictionary import SUT
from pprint import pprint
from Library.Redfish_requests import *

BMC_IP = '10.184.28.110'
FW_url = 'https://'+BMC_IP+'/redfish/v1/UpdateService/FirmwareInventory/'
auth = ('ADMIN','ADMIN')
Check_SUT = GET(url='https://'+BMC_IP+'/redfish/v1//Systems', auth=auth)

def PrintSUT():
    pprint(SUT)
    return SUT

def GetFWInfo():
    print(f"Server IP: {BMC_IP}")
    if Check_SUT[0] == 200:
        try:
            BMC_Data = GET(url=FW_url+'BMC', auth=auth)
            BIOS_Data = GET(url=FW_url+'BIOS', auth=auth)
            # print(BMC_Data['Version'])
            BMC_FW = BMC_Data[-1]['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1]['Oem']['Supermicro']['UniqueFilename']
            return print(f"{BMC_FW}\n{BIOS_FW}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1]}\nBIOS Data: {BIOS_Data[-1]}")
    else:
        New_pw = input('Input Unique Password: ')
        auth2 = ('ADMIN', New_pw)
        Check_Again = GET(url='https://'+BMC_IP+'/redfish/v1//Systems', auth=auth2)
        
        if Check_Again[0] == 200:
            try:
                BMC_Data = GET(url=FW_url+'BMC', auth=auth2)
                BIOS_Data = GET(url=FW_url+'BIOS', auth=auth2)
                BMC_FW = BMC_Data[-1]['Oem']['Supermicro']['UniqueFilename']
                BIOS_FW = BIOS_Data[-1]['Oem']['Supermicro']['UniqueFilename']
                return print(f"{BMC_FW}\n{BIOS_FW}")
            except KeyError as e:
                print(f"{e}\nBMC Data: {BMC_Data[-1]}\nBIOS Data: {BIOS_Data[-1]}")
        else:
            return print(f"Status code: {BMC_Data[0]}\n{BMC_Data}")

if __name__=='__main__':
    GetFWInfo()

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'