from random import choice, randint, sample
import string
from Library.Redfish_requests import *
from Library.dictionary import *
import subprocess
from Library.SMCIPMITool import SMCIPMITool
import re
from time import sleep
from paramiko import SSHClient, ssh_exception, AutoAddPolicy

al='abcdefghijklmnopqrstuvwxyz'
digit='1234567890'
al_digit = 'abcdefghijklmnopqrstuvwxyz1234567890'
def KeyGenerator():

    result=''
    for i in range(2):
        List=[]
        for i in range(3):
            TextList=[
                choice(al.upper())+choice(digit)+choice(al),
                choice(al)+choice(digit)+choice(al.upper()),
                choice(digit)+choice(al.upper())+choice(al)]
            List.append(TextList[randint(0,2)])
        # print(List)
        for j in List:
            result+=j
        result=result+'\n'
    return result

def AI_Optimize():
    result = ''
    for i in range(2):
        sub_result = ''.join([f'{choice(al.upper())}{choice(digit)}{choice(al)}' for k in range(3)])
        result += f'{sub_result}\n'
    return result

def AI_StringGenerator():
    Num = 32
    multiple = 1
    while Num > 5*multiple:
        multiple+=1

    result = ''
    for Start in range(multiple):
        if Start % 2 != 0:  # 奇數，產生英文字母
            for _ in range(5): 
                result += choice(string.digits)
        else:  # 偶數，產生數字
            for _ in range(5):
                result += choice(string.ascii_lowercase)
    print(result[0:Num])

def StringGenerator(Num):
    """
    Input str number
    """
    Start = 1
    result = ''
    Num = int(Num)
    while Num > (5 * Start)-1:    
        if Start %2 != 0:
            # print("Num是英文")  #0-4, 10-14
            for i in range(5):
                result+=choice(al)
        else:
            # print("Num是數字") #5-9, 15-16(沒有符合loop條件)
            for i in range(5):
                result+=choice(digit)
        Start+=1

    if Start %2 != 0:
        # print("Num是英文")
        for i in range(5-((5*Start)-Num)): 
            result+=choice(al)
    else:
        # print("Num是數字")
        for i in range(5-((5*Start)-Num)):
            result+=choice(digit) 

    # print(f"Start={Start}")
    # print(len(result))
    
    print(result)

def StrReverse(Strin):
    return Strin[::-1]

def get_a_random_ip():
    return ".".join(str(randint(173, 255)) for _ in range(4))

def generate_special_char():
    return sample(',;&*!(){[}]#%+\'"<>=$|^?', 1)[0]


def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0

def Check_PWD(ip, unique):
    """
    - Utilize `Redfish` checking current password
    - If `GET fail` return `unique password`
    
    """
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

def AI_ASCII_to_raw(url: str) -> str:
    return ' '.join([f"0x{hex(ord(r))[2:]}" for r in url])

def ASCII_to_raw(url:str):
    print(url)
    ASCII_code = [ord(r) for r in url]
    # result = ' '.join(f'0x{hex(i)[2:]}' for i in ASCII_code)
    result = ' '.join(f'{hex(i)[2:]}' for i in ASCII_code)
    # result = ''
    # for i in ASCII_code:
    #     result+=f"0x{hex(int(i))[2:]}" + ' '   
    return print(result)

def CN_Generator(num):
    num = int(num)
    text = ''
    swicher = bool
    for _ in range(num):
        random_al_digit = choice(al_digit)
        if random_al_digit in '1234567890':
            digit = random_al_digit
            text+=digit
        else:
            if swicher:
                text+=random_al_digit.upper()
                swicher = False
            else:
                text+=random_al_digit.lower()
                swicher = True

    print(f'CN={text},CN=Users,DC=ad,DC=satc,DC=com\n{text}') 

def Email_Format(text):
    first_text_cut = text.split('@')[0]
    length = text.split('.')
    second_text_cut = text.split('@')[1].split('.')[0] if len(length) > 0 else None
    Third_text_cut = text.split('@')[1].split('.')[1] if len(length) > 1 else None
    forth_text_cut = text.split('@')[1].split('.')[2] if len(length) > 2 else None

    print(f"Local-part: {first_text_cut}") 
    print(f"Local-part length is {len(first_text_cut)}\n") #length == 64 

    if len(length) > 0:
        print(f"Domain 1st label: {second_text_cut}")
        print(f"Domain 1st label length is {len(second_text_cut)}\n") # length == 63
    if len(length) > 1:
        print(f"Domain 2nd label: {Third_text_cut}")
        print(f"Domain 2nd label length is {len(Third_text_cut)}\n") # length == 63
    if len(length) > 2:
        print(f"Domain 3rd label: {forth_text_cut}")
        print(f"Domain 3rd label length is {len(forth_text_cut)}\n") # length == 5


def Get_Dict(DictVar, path):
    key_list = path.split('.')
    current = DictVar
    for cp in key_list: 
        if isinstance(current, dict):       
            current = current[cp]
    return current

def GetPath(path):
    key_list = path.split('.')
    current = Path 
    for cp in key_list:
        if isinstance(current, dict):
            current = current[cp]
    return current

def GetRedfish(path):
    key_list = path.split('.')
    current = redfish
    for cp in key_list:
        if isinstance(current, dict):
            current = current[cp]
    return current

def get_lani_id_list(ip, uni_pwd):
    pwd = Check_PWD(ip, uni_pwd)[1]
    lani_output = SMCIPMITool(ip, pwd).Execute('ipmi oem lani')
    # print(lani_output)
    regex = r"\d"
    result = re.findall(regex, lani_output)
    return result

def smc_command(ip, uni_pwd, cmd):
    pwd=Check_PWD(ip, uni_pwd)[1]
    output = SMCIPMITool(ip, pwd).Execute(cmd)
    print(output)

def hex_to_dec(digit:str):
    answer = []
    for dec in digit.split(' '):
        answer.append(str(int(dec, 16)))
    result = ' '.join(answer)
    print(result)

def AI_hex_to_dec(hex_str:str):
    answer = ' '.join(str(int(dec, 16)) for dec in hex_str.split(' '))
    print(answer)

def hex_to_unicode(digit:str):
    unicode_list = [chr(int(hexv, 16)) for hexv in digit.split(' ')]
    unicode_str = ''.join(unicode_list)
    print(unicode_str)

def AI_hex_to_unicode(hex_str):
    unicode_str = ''.join(chr(int(hex_v, 16)) for hex_v in hex_str.split(' '))
    print(unicode_str)
    return unicode_str

def raw_Factory_Default(ip, uni_pwd):
    print(f'Server IP: {ip}')
    auth = Check_PWD(ip, uni_pwd)
    timeout = 150 if ip.split('.')[0] == '10' else 160
    SMCIPMITool(ip, auth[1]).raw_30_41()
    sleep(timeout)
    SMCIPMITool(ip, uni_pwd).raw_30_48_1()

def ssh_inband(osip, ip):
    print(f"Server: {osip}")
    account = 'root'
    pwd = '111111'
    mask, gateway = ip_filter(ip)
    stdoutput = []
    Tool_used = False
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())      
        ssh.connect(hostname=osip, username=account, password=pwd, port=22)
        for cmd in ['ls IPMI*', 'ipmitool']:
            stdin, stdout1, stderr = ssh.exec_command(cmd)
            stdoutput += stdout1.readlines()
            stdoutput += stderr.readlines()
            print(''.join(stdoutput))

            stdstrings = ' '.join(stdoutput)
            if not Tool_used:
                if 'not' not in stdstrings:
                    if 'command not found' not in cmd:
                        Tool_used = ipmitool_recover(ssh, ip, mask, gateway)
                    else:
                        Tool_used = IPMICFG_recover(ssh, ip, mask, gateway)
                else:
                    if not Tool_used:
                        print(f"Doesn't have {cmd} tools")

        ssh.close()
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")
    
def ip_filter(ip):
    """
    return corresponding `netmask` and `gateway` IPs according to specific location 
    """
    One_Two = ip.split('.')[0]+'.'+ip.split('.')[1]
    if ip.split('.')[0] == '10':
        print('Bade ip') if One_Two == '10.184' else print('Zho ip')
        mask = '255.255.224.0' if One_Two == '10.184' else '255.255.0.0'
        gateway = '10.184.7.254' if One_Two == '10.184' else '10.140.0.0'
        return mask, gateway
    else: 
        print('US ip')
        return '255.255.0.0', '172.31.0.0'
    
def ipmitool_recover(ssh, ip, mask, gateway):
    for ssh_cmd in [f'ipmitool lan set 1 iparc static', f'ipmitool lan set 1 ipaddr {ip}', f'ipmitool lan set 1 netmask {mask}', f'ipmitool lan set 1 defgw ipaddr {gateway}', 'ipmitool lan print']:
        stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
        for result in stdout.readlines() + stderr.readlines():
            print(result+'\n')
    return True

def IPMICFG_recover(ssh, ip, mask, gateway):
    for ssh_cmd in ['./IPMICFG -dhcp off', f'./IPMICFG -m {ip}', f'./IPMICFG -k {mask}', f'./IPMICFG -g {gateway}']:
        stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
        for result in stdout.readlines() + stderr.readlines():
            print(result+'\n')
    return True