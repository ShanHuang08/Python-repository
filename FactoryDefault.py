from Library.Common_Func import Check_PWD
from Library.SMCIPMITool import SMCIPMITool
from time import sleep

def timeout(ip):
    return 130 if ip.split('.')[0] == '10' else 160

def Check_Mel(SMC_Tool):
    response = SMC_Tool.Execute('mel list')
    if 'unauthorized' in response.splitlines()[0]:
        pwd2 = Check_PWD(ip, Uni_pwd)[1]
        SMC_Tool2 = SMCIPMITool(ip, pwd2)
        response = SMC_Tool2.Execute('mel list')
    Pass_Check = ['PASS' for i in response.splitlines() if 'IPMI configuration was restored to default successfully' in i]
    if len(Pass_Check) == 0: print(response)
    return len(Pass_Check) > 0

def FactoryDefault(ip, Uni_pwd):
    # commands = ['30 40', '30 41', '30 42', '30 48 0', 'ipmi fd 1', '30 48 1', 'ipmi fd 2', 'ipmi fd 3']
    commands = ['ipmi fd 3']
    for cmd in commands:
        error = []
        pwd = Check_PWD(ip, Uni_pwd)[1] 
        print(pwd) #Debug
        SMC_Tool = SMCIPMITool(ip, pwd)
        print('Start executing '+cmd)
        if 'ipmi' in cmd:
            exe = SMC_Tool.Execute(cmd)
            print(exe)
            if 'Error' in exe: error.append('Fail')
        else:
            raw = SMC_Tool.raw(cmd)
            print(raw)
            if 'Error' in raw: error.append('Fail')
        sleep(timeout(ip))
        print('Execute PASS') if not error else print('Execute FAIL')
        print('MEL PASS') if Check_Mel(SMC_Tool) else print('MEL FAIL')

if __name__=='__main__':
    ip = '10.184.30.24'
    Uni_pwd = 'BOFSXVCBCT'
    FactoryDefault(ip, Uni_pwd)