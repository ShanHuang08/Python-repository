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
    return len(Text) > 0


def GetDirectory(OriginalDir, Dircom):
    Path = os.getcwd()
    os.chdir(OriginalDir)
    Path = os.getcwd()

    SearchDir=subprocess.run(Dircom , shell=True, capture_output=True, universal_newlines=True, cwd=Path)

    if SearchDir.returncode == 0:
        Directory = SearchDir.stdout
    else:
        raise ValueError(SearchDir.stderr)
        
    # print(Directory.splitlines())
    # print(Directory.split('\n'))

    DirList = Directory.split('\n')
    TextLine=''
    for line in DirList:
        if ("sum" in line or "SMC" in line) and "<DIR>" in line:
            # print(line)
            TextLine+=line

    if len(TextLine.split()) == 0:
        raise ValueError(f'{Dircom} No Diractory found')

    return TextLine.split()[-1]


def CheckVersion(ip, check_pwd, SumLocation, SMCLocation):
    if check_pwd.lower() == 'y':
        pwd = input('Input Unique Password: ')
    else:
        pwd = 'ADMIN'
    filename = ip+' CheckVersion.txt'
    file = open(filename, 'w')
    try:
        sumcom = 'sum.exe -i '+ip+' -u ADMIN -p '+pwd+' -c ' 
        cmd1 = sumcom + 'getbiosinfo --showall'
        cmd2 = sumcom + 'getbmcinfo'
        cmd3 = sumcom + 'getcpldinfo'
        cmds = cmd1+' && '+cmd2+' && '+cmd3
        sumproc = subprocess.run(cmds, shell=True, capture_output=True, universal_newlines=True, cwd=SumLocation)
        
        if sumproc.stdout != '':
            # print(sumproc.stdout)
            file.write(sumproc.stdout + '\n')
        else:
            print(sumproc.stderr)
        
        smccom = 'SMCIPMITOOL.exe '+ip+' ADMIN '+pwd+' redfish version'
        smcproc = subprocess.run(smccom, shell=True, capture_output=True, universal_newlines=True, cwd=SMCLocation)

        if smcproc.stdout != '':
            # print(f'Redfish version: {smcproc.stdout}')
            file.write(f'Redfish version: {smcproc.stdout}')
        else:
            print(smcproc.stderr)
        
        print(f'{filename} 寫入完成, 路徑: {OriginalDir}')
    except Exception as e:
        print(f'{filename} 檔案寫入失敗: {e}')
    file.close()
    return

def DMIinfo(ip, check_pwd, SumLocation):
    if check_pwd.lower() == 'y':
        pwd = input('Input Unique Password: ')
    else:
        pwd = 'ADMIN'
    filename = ip+' DMI.txt'
    file = open(filename,'w')
    try:
        dmicom = 'sum.exe -i '+ip+' -u ADMIN -p '+pwd+' -c getdmiinfo'
        dmiproc = subprocess.run(dmicom, shell=True, capture_output=True, universal_newlines=True, cwd=SumLocation)

        if dmiproc.stdout != '':
            file.write(dmiproc.stdout)
        else:
            print(dmiproc.stderr)
        
        print(f'{filename} 寫入完成, 路徑: {OriginalDir}')
    except Exception as e:
        print(f'{filename} 檔案寫入失敗: {e}')
    file.close()
    return

if __name__=='__main__':
    ip = input('ip address: ')
    check_pwd = input('Login via Unique Password (y/n)')
    OriginalDir = 'C:\\Users\\Stephenhuang\\' #sum跟SMCIPMITOOL都放在同一個資料夾之下
    Check_ipaddr(ip)
    if Check_ipaddr(ip):
        SumFolder = GetDirectory(OriginalDir, Dircom='dir sum*')
        SMCFolder = GetDirectory(OriginalDir, Dircom='dir SMC*')
        SumLocation = OriginalDir + SumFolder
        SMCLocation = OriginalDir + SMCFolder
        CheckVersion(ip, check_pwd, SumLocation, SMCLocation)
        DMIinfo(ip, check_pwd, SumLocation)
        subprocess.run('explorer '+OriginalDir, shell=True)
    else:
        raise ValueError('Invalid ip address')
