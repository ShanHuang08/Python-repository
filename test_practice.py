from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import ASCII_to_raw, Get_Dict, Email_Format, hex_to_dec, hex_to_unicode, Modify_Frus
# from Library.Common_Func import Check_PWD
from ssh_connect import ssh_os
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
    
def SMC_tools():
    smc, smc_in = SMCIPMITool(ip, uni_pwd), SMCIPMITool_Internal(ip, uni_pwd)
    return smc, smc_in

# lani = get_lani_id_list(ip, uni_pwd)
# print(lani)

def Search_FW_Type(types, mbd):
    types = types.upper()
    mbd = mbd.upper()
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


        

if __name__=='__main__':
    ip = '10.140.177.51'
    uni_pwd = 'GXBGWWDHHK'
    smc, smc_in = SMC_tools()

    # Search_FW_Type('F201MS', 'x12stl')
    # smc.raw_30_48_1()
    # smc.Raw_Factory_Default()
    # smc_in.Check_BS()
    # Modify_Frus(ip, uni_pwd, 'BM, BDN')
    # smc.smc_commands('ipmi power status')
    # ASCII_to_raw('')
    # Email_Format('UHtapQij@EfPnkRUp.c'),
    # ssh_os('10.140.175.82', 'X12STL-IF.txt')
    


