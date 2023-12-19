import re
from datetime import datetime
from lxml import etree
from Library.Redfish_requests import *
from Library.Call_Method import StrReverse, StringGenerator


reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

import Library.dictionary as dic
dic.RawCommands

TagName = ['child8', 'child9']
TagValue = ['Newtest', 'test9']
def enumerate_practice():
    TestDict = {}
    for index, value in enumerate(TagName):
        print(index, value)
        TestDict[index] = value
        if index == len(TagName)-1:
            print(type(index), type(value))
            # <class 'int'> <class 'str'>
    print(TestDict)

# enumerate_practice()
# print(int('40', 16))

def raw_byte_array():
    value = input('Input 30 68 0A return code: ')
    excepted = input('Input IP address: ')
    value = value.strip()
    Value_NoSpace = ''.join(value.split())
    Transfer_value = bytearray.fromhex(Value_NoSpace).decode()
    if Transfer_value == excepted:
        print(f"Both values match")
    else:
        print(f"{Transfer_value} != {excepted}")

def AI_ASCII_to_raw(url: str) -> str:
    return ' '.join([f"0x{hex(ord(r))[2:]}" for r in url])

def ASCII_to_raw(url:str):
    ASCII_code = [ord(r) for r in url]
    result = ' '.join(f'0x{hex(i)[2:]}' for i in ASCII_code)
    # result = ''
    # for i in ASCII_code:
    #     result+=f"0x{hex(int(i))[2:]}" + ' '   
    print(result) 
    return result


from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD
ip='10.135.172.111'
def Check_Fru1():
    pwd=Check_PWD(ip=ip, unique='XFFXGWHUVY')[1]
    SMC_tool = SMCIPMITool(ip, pwd)
    fru1 = SMC_tool.Execute('ipmi fru1')
    for out in fru1.splitlines():
        if any(j in out for j in ['BPN','BS','BP','BV']):
            print(out)       
# Check_Fru1()
def smc_command():
    pwd=Check_PWD(ip=ip, unique='XFFXGWHUVY')[1]
    SMC_tool = SMCIPMITool(ip, pwd)
    output = SMC_tool.Execute('redfish firmwareInventory info')
    print(output)
# smc_command()

# 定義波峰波谷再切割 再比
def pick_peaks(arr):
    pos = []
    peaks = []
    min_pos = []
    min_num = ''
    max_pos = []
    max_num = ''
    # 跟左邊右邊比就好 所以左右邊都要有數字
    if len(arr) == 0 or max(arr) == min(arr):
        return {'pos':[], 'peaks':[]}
    else:
        for i in range(len(arr)):
            min_count = 0
            max_count = 0
            if i-1 >= 0 and i+1 != len(arr):
                for j in range(i-1, i+2, 2):
                    if arr[i] < arr[j]: min_count+=1
                    if arr[i] > arr[j]: max_count+=1
                if min_count == 2:
                    min_pos.append(i)
                    min_num += str(arr[i]) + ', '   
                if max_count == 2: 
                    max_pos.append(i)
                    max_num += str(arr[i]) + ', '
        # 分割Lists
        Lists = []
        for i in range(len(min_pos)):
            if i == 0:
                Lists.append(arr[0:min_pos[i]+1])
                Lists.append(arr[min_pos[i]:min_pos[i+1]+1])
            elif i == len(min_pos)-1:
                Lists.append(arr[min_pos[i]:])
            else:
                Lists.append(arr[min_pos[i]:min_pos[i+1]+1])
        
        for List in Lists:
            print(List)



    print(f'波谷位置= {min_pos}\n波谷: {min_num}') #波谷定義: 這個數字比兩邊數字都小
    print(f'波峰位置= {max_pos}\n波峰: {max_num}') #波峰定義: 這個數字比兩邊數字都大
    print(arr[0:1+1], arr[1:5+1], arr[5:9+1], arr[9:len(arr)])

    return {'pos':pos, 'peaks':peaks}

print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))

# [3,2] [2,3,6,4,1] [1,2,3,2,1] [1,2,2,2,1]
# 4-1, 9-2, 13-3

# [2,1,3,1,2,2,2,2,1], {"pos":[2,4], "peaks":[3,2]}

# [2,1] [1,3,1] [1,2,2,2,1]
# 2-0, 3-1, 6-2

# [2,1,3,1,2,2,2,2], {"pos":[2], "peaks":[3]}
# [2,1] [1,3,1] [1,2,2,2]
# 2-0, 3-1, 6-2


test = [1,2,3,6,4,1,2,3,2,1] #要拆開來
ans = {"pos":[3,7], "peaks":[6,3]}
# [1,2,3,6,4,1] [1,2,3,2,1]
# 3-0, 8-1

test2 = [1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]
ans2 = {"pos":[2,7,14,20], "peaks":[5,6,5,5]}
# [1,2,5,4,3,2] [2,3,6,4,1] [1,2,3,3,4,5,3,2,1] [1,2,3,5,5,4,3]
# 2-0, 8-1, 16-2, 23-3

test3 = [18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]
ans3 = {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]}
# [18, 18, 10, -3, -4, 15, 15, -1] [-1, 13, 17, 11, 4] [4, 18, -4] [-4, 19, 4] [4, 18, 10, -4] [-4, 8, 13, 9] [9, 16, 18, 6, 7]
# 5-0, 10-1, 14-2, 17-3, 20-4, 25-5, 29-6

