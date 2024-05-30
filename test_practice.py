from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import ASCII_to_raw, Get_Dict, Email_Format, hex_to_dec, hex_to_unicode, Modify_Frus
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
    Find_via_FW_Type(types, mbd) if types.strip() else Find_via_MBDs(mbd)
    

if __name__=='__main__':
    ip = '10.184.19.180'
    uni_pwd = 'NLTAFRJLHJ'
    smc, smc_in = SMC_tools()

    # Search_FW_Num('', 'x13saw-f')
    smc.raw_30_48_1()
    # smc.Raw_Factory_Default()
    # smc_in.Check_BS()
    # Modify_Frus(ip, uni_pwd, 'BM, BDN')
    # smc.smc_commands('ipmi power status')
    # ASCII_to_raw('')
    # Email_Format('UHtapQij@EfPnkRUp.c'),
    # ssh_os('10.140.175.82', 'X12STL-IF.txt')
    


