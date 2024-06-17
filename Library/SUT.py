from Redfish_requests import *
import re


def AddSUT():
    key = input("SUT: ")
    BMC_IP = input("BMC IP: ")
    OS_IP = input("OS IP: ")
    SUT_info = {key : {"BMC" : BMC_IP, "OS" : OS_IP}}
    print(str(SUT_info)[1:-1])

def Check_PWD(ip):
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network == None: #會造成GetFWInfo()出現TypeError: 'NoneType' object is not subscriptable
        print('SUT is disconnected')
        exit()
    else:
        if Check_Network[0] == 200:
            return ('ADMIN', 'ADMIN')
        else:
            pwd = input('Input unique password: ')
            if pwd == '':
                print('Password is empty!')
                exit()
            return ('ADMIN', pwd)

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False

def GetGUID(ip, pwd):
    Mongo_url = 'https://satc.supermicro.com/api/mongohelper/tools/sut/'+ip+'/ADMIN/'+pwd+'/'
    First_Sector = ip.split()[0]
    if First_Sector == '10':
        Mongo_url += '10.184.0.12'
        Guid = GET(url=Mongo_url, timeout=30)
        return print(Guid[-1].json()['guid']) if Guid[0] == 200 else print(f"Status code: {Guid[0]}\n{Guid[1]}")
    else:
        Mongo_url += '172.31.2.47'
        Guid = GET(url=Mongo_url, timeout=30)
        return Guid[-1].json()['guid'] if Guid[0] == 200 else print(f"Status code: {Guid[0]}\n{Guid[1]}")

def GetFWInfo(ip:str):
    auth = Check_PWD(ip)
    # auth = ('admin', '2wsx#EDC')
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    BMC_Data = None
    BIOS_Data = None
    Check_Pwd = GET(url='https://'+ip+'/redfish/v1/Systems', auth=auth)

    if Check_Pwd[0] == 200:
        try:
            # print(GetGUID(ip, pwd=auth[1]))
            BMC_Data = GET(url=url+'BMC', auth=auth)
            BIOS_Data = GET(url=url+'BIOS', auth=auth)
            CPLD_Data = GET(url=url + 'CPLD_Motherboard', auth=auth) if GET(url=url + 'CPLD_Motherboard', auth=auth)[0] == 200 else 'Not support CPLD'
            # print(BMC_Data['Version'])
            BMC_FW = BMC_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']

            CPLD_Ver = CPLD_Data if CPLD_Data == 'Not support CPLD' else CPLD_Data[-1].json()['Version']
                   
            print(f"{BMC_FW}\n{BIOS_FW}\n{CPLD_Ver}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()['Oem']}\nBIOS Data: {BIOS_Data[-1].json()['Oem']}\nCPLD Data: {CPLD_Data[-1].json()['Version']}")
        
    else:
        print(f"Status code: {Check_Pwd[0]}\n{Check_Pwd[1]}")

if __name__=='__main__':
    AddSUT()
    # GetFWInfo('10.184.26.116')
    
    # for info in ['10.184.11.104', '10.184.21.204']:
    #     GetFWInfo(info)
    #     print('\n')

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'