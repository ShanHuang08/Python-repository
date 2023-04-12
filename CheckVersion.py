import subprocess, os

def Check_ipaddr(ip):
    command = 'ping ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    # print(List)
    Text=''
    for line in List:
        if "TTL=" in line:
            Text+=line

    if len(Text) > 0:
        return True
    else:
        return False


def GetDirectory(OriginalDir, Dircom):
    Path = os.getcwd()
    os.chdir(OriginalDir)
    Path = os.getcwd()

    SearchDir=subprocess.run(Dircom , shell=True, capture_output=True, universal_newlines=True, cwd=Path)

    if SearchDir.returncode == 0:
        Directory = SearchDir.stdout
    else:
        raise ValueError(SearchDir.stderr)

    AIList = Directory.split('\n')
    TextLine=''
    for line in AIList:
        if "sum" in line and "<DIR>" in line:
            # print(line)
            TextLine+=line
        elif "SMC" in line and "<DIR>" in line:
            TextLine+=line

    if len(TextLine.split()) == 0:
        raise ValueError('No Diractory found')

    return TextLine.split()[-1]


def CheckVersion(ip, check_pwd, SumLocation, SMCLocation):
    if check_pwd.lower() == 'y':
        pwd = input('Input Unique Password: ')
    else:
        pwd = 'ADMIN'

    sumcom = 'sum.exe -i '+ip+' -u ADMIN -p '+pwd+' -c ' 
    cmd1 = sumcom + 'getbiosinfo --showall'
    cmd2 = sumcom + 'getbmcinfo'
    cmd3 = sumcom + 'getcpldinfo'
    cmds = cmd1+' && '+cmd2+' && '+cmd3
    sumproc = subprocess.run(cmds, shell=True, capture_output=True, universal_newlines=True, cwd=SumLocation)
    
    if sumproc.stdout != '':
        print(sumproc.stdout)
    else:
        print(sumproc.stderr)
    
    smccom = 'SMCIPMITOOL.exe '+ip+' ADMIN '+pwd+' redfish version'
    smcproc = subprocess.run(smccom, shell=True, capture_output=True, universal_newlines=True, cwd=SMCLocation)

    if smcproc.stdout != '':
        print(f'Redfish version: {smcproc.stdout}')
    else:
        print(smcproc.stderr)
    return

if __name__=='__main__':
    ip = input('ip address: ')
    check_pwd = input('Login via Unique Password (y/n)')
    OriginalDir = 'C:\\Users\\Stephenhuang\\'
    Check_ipaddr(ip)
    if Check_ipaddr(ip):
        SumFolder = GetDirectory(OriginalDir, Dircom='dir sum*')
        SMCFolder = GetDirectory(OriginalDir, Dircom='dir SMC*')
        SumLocation = OriginalDir + SumFolder
        SMCLocation = OriginalDir + SMCFolder
        CheckVersion(ip, check_pwd, SumLocation, SMCLocation)
    raise ValueError('Invalid ip address')
