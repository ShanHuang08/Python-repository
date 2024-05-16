from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import Check_PWD, ASCII_to_raw, Get_Dict, Email_Format, smc_command, hex_to_dec, hex_to_unicode, GetPath, raw_Factory_Default, ip_filter
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
    
def Check_Fru1(ip, uni_pwd):
    print(f'Server IP: {ip}')
    pwd = Check_PWD(ip, uni_pwd)[1]
    SMC_tool = SMCIPMITool_Internal(ip, pwd)
    fru1 = SMC_tool.Execute('ipmi fru1')
    for output in fru1.splitlines():
        # if any(fru in output for fru in ['BPN','BS','BP','BV']):
        if 'BS' in output:
            print(output)
            SN_number = output.split('=')[-1]
            if len(SN_number) < 10:
                text = input('Input BS: ')
                bs1 = SMC_tool.Execute('ipmi fru1w BS '+ text + ' Supermicro82265990')
                bs = SMC_tool.Execute('ipmi fruw BS ' + text)
                print(bs1+'\n'+bs)
            else: print('BS is match')

        if 'BM' in output:
            if 'Supermicro' != output.split('=')[-1].lstrip():
                print(f"BM doesn't match\nStart override")
                bm1 = SMC_tool.Execute('ipmi fru1w BM Supermicro Supermicro82265990')
                bm = SMC_tool.Execute('ipmi fruw BM Supermicro')
                print(bm1+'\n'+bm)
            else: print(f"{output}\nBM is match")


# lani = get_lani_id_list(ip, uni_pwd)
# print(lani)

def Search_FW_Type(type):
    try: print(f"{type}\nFW type: {FW_Type[type]['info'][0]}\n{FW_Type[type]['info'][-1]}")
    except KeyError: print(f"Branch {type} is not found!")
    
 
if __name__=='__main__':
    ip = '172.31.35.195'
    uni_pwd = 'ALTWNBOQAN'
    # uni_pwd = 'ADMIN'


    # Search_FW_Type('F401MS')
    # SMCIPMITool(ip, uni_pwd).raw_30_48_1()
    # Check_Fru1(ip, uni_pwd)   
    # raw_Factory_Default(ip, uni_pwd)
    # smc_command(ip, uni_pwd, 'ipmi raw 30 2a')
    # StringGenerator(64)
    

