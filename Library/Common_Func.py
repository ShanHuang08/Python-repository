import subprocess
import re
from Library.Redfish_requests import GET

def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False

def Check_PWD(ip, unique):
    """
    - Utilize `Redfish` checking current password
    - If `GET fail` return `unique password`
    
    """
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()
    if Check_ipaddr(ip):
        Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=('ADMIN', 'ADMIN'))
        # if Check_Network == None:
        if isinstance(Check_Network, list):
            return ('ADMIN', 'ADMIN') if Check_Network[0] == 200 else ('ADMIN', unique)
        else:
            print('SUT is disconnected')
            exit()
        # return ('ADMIN', 'ADMIN') if Check_Network[0] == 200 else ('ADMIN', unique)
    else:
        print('Ping SUT failed')
        osip = input("Input OS IP (press ENTER if you doesn't know it): ")
        if osip:
            print("In-band recover function is under development!")
            exit()
        else:
            exit()

def is_only_dot(cmd:str):
    special_ch = '!@#$%^&*()_+<>?./:;'
    no_err = True
    for s in special_ch:
        if s in cmd: no_err = False
    return no_err