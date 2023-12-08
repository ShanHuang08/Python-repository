from Library.Call_Method import Check_PWD
from Library.SMCIPMITool import SMCIPMITool
from time import sleep

def timeout(ip):
    return 150 if ip.split('.')[0] == '10' else 160

def Check_Mel(SMC_Tool):
    response = SMC_Tool.Execute('mel list 10')
    if 'unauthorized' in response.splitlines()[0]:
        pwd2 = Check_PWD(ip=ip, unique=Uni_pwd)[1]
        SMC_Tool2 = SMCIPMITool(ip, pwd2)
        response = SMC_Tool2.Execute('mel list')
    Pass_Check = ['PASS' for i in response.splitlines() if 'MEL-0056' in i]
    if len(Pass_Check) == 0:
        print(response)
    return len(Pass_Check) > 0

def FactoryDefault():
    commands = ['30 40', '30 41', '30 42', '30 48 0', 'ipmi fd 1', '30 48 1', 'ipmi fd 2', 'ipmi fd 3']
    for cmd in commands:
        pwd = Check_PWD(ip=ip, unique=Uni_pwd)[1] 
        SMC_Tool = SMCIPMITool(ip=ip, pwd=pwd)
        print('Start executing '+cmd)
        if 'ipmi' in cmd:
            exe = SMC_Tool.Execute(cmd)
            print(exe)
        else:
            raw = SMC_Tool.raw(cmd)
            print(raw)
        sleep(timeout(ip))
        print('MEL-0056 has found\nPASS') if Check_Mel(SMC_Tool) else print('FAIL')

if __name__=='__main__':
    ip = '10.184.16.44'
    Uni_pwd = 'FPNKDBUBWY'
    FactoryDefault()