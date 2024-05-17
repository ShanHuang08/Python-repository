from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import Check_PWD, ASCII_to_raw, Get_Dict, Email_Format, smc_command, hex_to_dec, hex_to_unicode, GetPath, raw_Factory_Default, Check_BS, Modify_Frus
from SUT_IP import FW_Type

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
    

# lani = get_lani_id_list(ip, uni_pwd)
# print(lani)

def Search_FW_Type(type):
    try: print(f"{type}\nFW type: {FW_Type[type]['info'][0]}\n{FW_Type[type]['info'][-1]}")
    except KeyError: print(f"Branch {type} is not found!")



 
if __name__=='__main__':
    ip = '10.184.27.169'
    uni_pwd = 'ZLGBDYZQTO'
    # uni_pwd = 'ADMIN'

    
    # Search_FW_Type('F401MS')
    # SMCIPMITool(ip, uni_pwd).raw_30_48_1()
    # raw_Factory_Default(ip, uni_pwd)
    # smc_command(ip, uni_pwd, 'ipmi raw 30 2a')
    # Check_BS(ip, uni_pwd)
    Modify_Frus(ip, uni_pwd, 'BM, BDN')
    

