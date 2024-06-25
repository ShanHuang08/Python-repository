from random import choice, randint, sample
import string
from Library.Redfish_requests import *
from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SMCIPMITool_Internal
# from Library.Common_Func import Check_PWD
from paramiko import SSHClient, ssh_exception, AutoAddPolicy
from SUT_IP import FW_Type

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
        
def ssh_inband(osip, ip):
    """
    Utilize `ipmitool` or `IPMICFG` to recover SUT via in-band
    """
    print(f"Server: {osip}")
    mask, gateway = ip_filter(ip)
    stdoutput = []
    Tool_used = False
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())      
        ssh.connect(hostname=osip, username='root', password='111111', port=22)
        for cmd in ['ipmitool', './IPMICFG-Linux.x86_64']:
            stdin, stdout1, stderr = ssh.exec_command(cmd)
            stdoutput += stdout1.readlines()
            stdoutput += stderr.readlines()
            # print(''.join(stdoutput))
            stdstrings = ' '.join(stdoutput)

            if not Tool_used:
                if 'command not found' not in stdstrings:
                    Tool_used = ipmitool_recover(ssh, ip, mask, gateway)
                elif 'IPMICFG Version' in stdstrings: #改成IPMICFG檔名 in stdstrings
                    Tool_used = IPMICFG_recover(ssh, ip, mask, gateway)
                else: print(f"Doesn't have {cmd} tools")  
                
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
        mask = '255.255.224.0' if One_Two == '10.184' else '255.255.0.0'
        if One_Two == '10.184':
            gateway = '10.184.7.254'
        elif One_Two == '10.140':
            gateway = '10.140.0.250'
        elif One_Two == '10.135':
            gateway = '10.135.0.253'
        return mask, gateway
    else: 
        return '255.255.0.0', '172.31.0.1'
    
def ipmitool_recover(ssh, ip, mask, gateway):
    """Only for `ssh_inband`"""
    print('Execute ipmitool') # Debug only
    for ssh_cmd in [f'ipmitool lan set 1 iparc static', f'ipmitool lan set 1 ipaddr {ip}', f'ipmitool lan set 1 netmask {mask}', 
                    f'ipmitool lan set 1 defgw ipaddr {gateway}', 'ipmitool lan print']:
        stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
        for result in stdout.readlines() + stderr.readlines():
            print(result)
    return True

def IPMICFG_recover(ssh, ip, mask, gateway):
    """Only for `ssh_inband`"""
    print('Execute IPMICFG') #Debug only
    for ssh_cmd in ['./IPMICFG -dhcp off', f'./IPMICFG -m {ip}', f'./IPMICFG -k {mask}', f'./IPMICFG -g {gateway}']:
        stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
        for result in stdout.readlines() + stderr.readlines():
            print(result)
    return True

def String_Split(inputs:str):
    inputs = ' '.join(inputs.lstrip().rstrip().split(' '))
    if ',' in inputs or '.' in inputs:
        inputs = ' '.join(inputs.split(','))
        inputs = ' '.join(inputs.split('.'))
    return [s.lstrip() for s in inputs.split(' ') if s != '']

def Check_Frus(SMC_Tool, Types:list, Values:list):
    fru1= SMC_Tool.Execute('ipmi fru1')
    for Type, value in zip(Types, Values):
        for output in fru1.splitlines():
            if Type in output:
                Actual_value = output.split('=')[-1].lstrip() # Remove left side space
                print(f"{Type} output: {Actual_value}")
                print(f'{Type} value match!') if Actual_value == value else print(f'{Type} value mismatch!')
                    
def Modify_Frus(ip, uni_pwd, input_type):
    print(f'Server IP: {ip}')
    SMC_Tool = SMCIPMITool_Internal(ip, uni_pwd)
    Types = String_Split(input_type)
    Values = [input(f"Input {inp} value: ") for inp in Types]

    for typ, value in zip(Types, Values):
        if value != '':
            output1 = SMC_Tool.Execute(f'ipmi fru1w {typ} {value} Supermicro82265990')
            output = SMC_Tool.Execute(f'ipmi fruw {typ} {value}')
            print(f'Fru1 {typ} modify success') if 'Error' not in output1 else print(f'Fru1 {typ} modify failed')
            print(f'Fru {typ} modify success') if 'Error' not in output else print(f'Fru {typ} modify failed')         
        else: print(f'{typ} value is empty!')
    # Check if Fru1 values are match
    Check_Frus(SMC_Tool, Types, Values)

def Find_via_FW_Type(types, mbd):
    types = types.strip().upper()
    mbd = mbd.strip().upper()
    possible = []
    try: 
        if isinstance(FW_Type[types], list):
            for dics in FW_Type[types]:
                if mbd in dics['MBDs']:
                    print(f"{types}\nFW num: {dics['info'][0]}\n{dics['info'][-1]}")
                    break
                else: 
                    possible.append(f"FW num: {dics['info'][0]}\n{dics['MBDs']}")
            # if mbd not in dics['MBDs']: # dics變數在for loop外面仍然可以使用, 返回最後一個值 (Only Python and JS)
            if len(possible) == len(FW_Type[types]):
                print(types + '\nPossible FW numbers:\n' +'\n'.join(pos for pos in possible) + '\n' + FW_Type[types][-1]['info'][-1])
        else: print(f"{types}\nFW num: {FW_Type[types]['info'][0]}\n{FW_Type[types]['info'][-1]}")
    except KeyError: print(f"Branch {types} is not found!")

def Find_via_MBDs(mbd):
    err_msg = [] #Record error output. Error output won't show up if MBD match on the later loop
    if mbd:
        mbd = mbd.upper()
        for key, value in FW_Type.items():
            if isinstance(value, dict):
                if mbd in value['MBDs']: 
                    print(f"{key}\nFW num: {FW_Type[key]['info'][0]}\n{FW_Type[key]['info'][-1]}")
                    exit()
                elif mbd not in value['MBDs'] and mbd[0:3] == value['MBDs'][0][0:3]: 
                    err_msg.append(f"{value['MBDs']}")
                    err_msg.append(f"Can't find {mbd} in {key}")

            elif isinstance(value, list):
                num = 0
                for val in value:
                    if mbd in val['MBDs']: 
                        print(f"{key}\nFW num: {FW_Type[key][num]['info'][0]}\n{FW_Type[key][num]['info'][-1]}")
                        exit()
                    elif mbd not in val['MBDs'] and mbd[0:3] == val['MBDs'][0][0:3]: 
                        err_msg.append(f"{val['MBDs']}")
                        num+=1
                        if num == len(value): 
                            err_msg.append(f"Can't find {mbd} in {key}")
        if err_msg: print('\n'.join(err_msg))
            
def Search_FW_Num(types, mbd):
    '''- EX: `('d301ms', '')`, `('', 'x13dsf-a')`'''
    Find_via_FW_Type(types, mbd) if types.strip() else Find_via_MBDs(mbd)

def Mount_isos():
    # PATCH https://10.184.13.65/redfish/v1/Managers/1/VirtualMedia/VirtualMedia1
    # {"Oem":{"Supermicro":{"AcceptSelfSigned":false}},"VerifyCertificate":false}

    # POST https://10.184.13.65/redfish/v1/Managers/1/VirtualMedia/VirtualMedia1/Actions/VirtualMedia.InsertMedia
    # {"Image":"http://10.184.10.1/static/att/iso/RHEL9.4.iso","Inserted":true}

    # PATCH https://10.184.13.65/redfish/v1/Managers/1/VirtualMedia/VirtualMedia1
    # {Inserted: false}
    pass