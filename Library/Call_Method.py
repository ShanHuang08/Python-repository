from random import choice, randint, sample
import string
from Library.Redfish_requests import *
from Library.dictionary import *
import subprocess
import sys

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
    command = 'ping -n 3 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0

def Check_PWD(ip, unique):
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
        print('SUT is disconnected')
        sys.exit()

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
    return result

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

def Get_Dict(DictName, Path):
    key_list = Path.split('.')
    current = DictName
    for cp in key_list: 
        if isinstance(current, dict):       
            current = current[cp]
    return current