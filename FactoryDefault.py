from Library.Common_Func import Check_PWD
from Library.SMCIPMITool import SMCIPMITool
from time import sleep
from subprocess import CalledProcessError

def timeout(ip):
    if ip.split('.')[0] == '10':
        print(f'Waiting 130s for BMC to recover')
        return 130 
    else:
        print(f'Waiting 160s for BMC to recover')
        return 160

def Check_Mel(SMC_Tool):
    response = SMC_Tool.Execute('mel list')
    if 'unauthorized' in response.splitlines()[0]:
        print('Wait 30s and try again')
        sleep(30)
        pwd2 = Check_PWD(ip, Uni_pwd)[1]
        response = SMCIPMITool(ip, pwd2, rakp=False).Execute('mel list')
    elif 'Cannot connect to' in response:
        print('Wait 30s and try again')
        sleep(30)
        response = SMC_Tool.Execute('mel list')
    Pass_Check = [check for check in response.splitlines() if 'IPMI configuration was restored to default successfully' in check]
    if len(Pass_Check) == 0: print(response)
    return len(Pass_Check) > 0

def FactoryDefault(ip, Uni_pwd):
    """- ipmi fd 2 = raw 30 40"""
    # commands = ['30 40', '30 41', '30 42', '30 48 0', 'ipmi fd 1', '30 48 1', 'ipmi fd 2', 'ipmi fd 3']
    commands = ['ipmi fd 1', '30 48 1']
    print(f'Server IP: {ip}')
    for cmd in commands:
        try:
            error = []
            pwd = Check_PWD(ip, Uni_pwd)[1] 
            # print(pwd) #Debug
            SMC_Tool = SMCIPMITool(ip, pwd, rakp=False)
            print('Start executing '+cmd)
            exe = SMC_Tool.Execute(cmd) if 'ipmi' in cmd else SMC_Tool.raw(cmd)
            print(exe)
            if 'Error' in exe: error.append(exe)
            elif "Can't login" in exe: error.append(exe)

            print('Execute PASS') if not error else print('Execute FAIL')
            sleep(timeout(ip))
            print('MEL PASS') if Check_Mel(SMC_Tool) else print('MEL FAIL')
        except CalledProcessError as e:
            print(f'CalledProcessError: {e}')
            continue

if __name__=='__main__':
    ip = '10.184.23.61'
    Uni_pwd = 'MKQBSKZCNJ'
    FactoryDefault(ip, Uni_pwd)