from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import Check_PWD, ASCII_to_raw, Get_Dict, Email_Format, smc_command, hex_to_dec, hex_to_unicode, GetPath, raw_Factory_Default, Check_BS, Modify_Frus
# from SUT_IP import FW_Type

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

def Search_FW_Type(types, mbd):
    types = types.upper()
    try: 
        if isinstance(FW_Type[types], list):
            for dics in FW_Type[types]:
                if mbd in dics['MBDs']:
                    print(f"{types}\nFW type: {dics['info'][0]}\n{dics['info'][-1]}")
        else:
            print(f"{types}\nFW type: {FW_Type[types]['info'][0]}\n{FW_Type[types]['info'][-1]}")

    except KeyError: print(f"Branch {types} is not found!")



 
if __name__=='__main__':
    ip = '10.184.16.227'
    uni_pwd = 'HIIVAZLVKX'
    # uni_pwd = 'ADMIN'

    Search_FW_Type('F201MS', 'X12STH')
    # SMCIPMITool(ip, uni_pwd).raw_30_48_1()
    # raw_Factory_Default(ip, uni_pwd)
    # smc_command(ip, uni_pwd, 'ipmi raw 30 2a')
    # Check_BS(ip, uni_pwd)
    # Modify_Frus(ip, uni_pwd, 'BM, BDN')
    

