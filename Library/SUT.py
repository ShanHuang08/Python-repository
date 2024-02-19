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

def GetGUID(ip, pwd):
    Mongo_url = 'https://satc.supermicro.com/api/mongohelper/tools/sut/'+ip+'/ADMIN/'+pwd+'/'
    First_Sector = ip.split()[0]
    if First_Sector == '10':
        Mongo_url = Mongo_url + '10.184.0.12'
        Guid = GET(url=Mongo_url, timeout=30)
        if Guid[0] == 200:
            return print(Guid[-1].json()['guid'])
        else:
            print(f"Status code: {Guid[0]}\n{Guid[1]}")
    else:
        Mongo_url = Mongo_url + '172.31.2.47'
        Guid = GET(url=Mongo_url, timeout=30)
        if Guid[0] == 200:
            return print(Guid[-1].json()['guid'])
        else:
            print(f"Status code: {Guid[0]}\n{Guid[1]}")

def GetFWInfo(ip:str):
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    auth = Check_PWD(ip)
    BMC_Data = None
    BIOS_Data = None
    Check_Pwd = GET(url='https://'+ip+'/redfish/v1/Systems', auth=auth)

    if Check_Pwd[0] == 200:
        try:
            # GetGUID(ip, pwd=auth[1])
            BMC_Data = GET(url=url+'BMC', auth=auth)
            BIOS_Data = GET(url=url+'BIOS', auth=auth)
            CPLD_Data = GET(url=url + 'CPLD_Motherboard', auth=auth) if GET(url=url + 'CPLD_Motherboard', auth=auth)[0] == 200 else 'Not support CPLD'
            # print(BMC_Data['Version'])
            BMC_FW = BMC_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            
            CPLD_Ver = CPLD_Data if CPLD_Data == 'Not support CPLD' else CPLD_Data[-1].json()['Version']
                   
            return print(f"{BMC_FW}\n{BIOS_FW}\n{CPLD_Ver}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()}\nBIOS Data: {BIOS_Data[-1].json()}\nCPLD Data: {CPLD_Data[-1].json()}")
        
    else:
        return print(f"Status code: {Check_Pwd[0]}\n{Check_Pwd[1]}")

if __name__=='__main__':
    # AddSUT()
    GetFWInfo('172.31.35.46')

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'