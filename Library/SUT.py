from dictionary import SUT
from pprint import pprint
from Redfish_requests import *
import json
BMC_IP = '10.184.30.32'
FW_url = 'https://'+BMC_IP+'/redfish/v1/UpdateService/FirmwareInventory/'
auth = ('ADMIN','ADMIN')
def PrintSUT():
    pprint(SUT)
    return SUT

def GetFWInfo():
    # 要用GUID分類, 所以要找GUID的網址
    BMC_Data = json.loads(GET(url=FW_url+'BMC', auth=auth)[-1])
    BIOS_Data = json.loads(GET(url=FW_url+'BIOS', auth=auth)[-1])
    # print(BMC_Data['Version'])
    BMC_FW = BMC_Data['Oem']['Supermicro']['UniqueFilename']
    BIOS_FW = BIOS_Data['Oem']['Supermicro']['UniqueFilename']
    return print(f"{BMC_FW}\n{BIOS_FW}")
# X12
# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 21, in <module> 
#     GetFWInfo()
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 16, in GetFWInfo
#     BMC_FW = BMC_Data['Oem']['Supermicro']['UniqueFilename']
# KeyError: 'Oem'

if __name__=='__main__':
    GetFWInfo()