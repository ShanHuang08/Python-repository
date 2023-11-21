from random import choice, randint, sample
import string
from Library.Redfish_requests import *

al='abcdefghijklmnopqrstuvwxyz'
digit='1234567890'
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

def StringGenerator(Num:str):
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



def Check_PWD(ip, unique):
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        pwd = input('Input unique password: ')
        return ('ADMIN', unique)