import subprocess

def CheckVersion(ip, check_pwd):
    if check_pwd.lower() == 'y':
        pwd = input('Input Unique Password: ')
    else:
        pwd = 'ADMIN'

    sumcom = 'sum.exe -i '+ip+' -u ADMIN -p '+pwd+' -c ' 
    cmd1 = sumcom + 'getbiosinfo --showall'
    cmd2 = sumcom + 'getbmcinfo'
    cmd3 = sumcom + 'get cpldinfo'
    cmds = cmd1+' && '+cmd2+' && '+cmd3
    sumproc = subprocess.run(cmds, shell=True, capture_output=True, universal_newlines=True, cwd='C:\\Users\\Stephenhuang\\sum*')
    
    if sumproc.stdout != '':
        print(sumproc.stdout)
    else:
        print(sumproc.stderr)
    
    smccom = 'SMCIPMITOOL.exe '+ip+' ADMIN '+pwd+' redfish ver'
    smcproc = subprocess.run(smccom, shell=True, capture_output=True, universal_newlines=True, cwd='C:\\Users\\Stephenhuang\\SMC*')

    if smcproc.stdout != '':
        print(smcproc.stdout)
    else:
        print(smcproc.stderr)

    return

if __name__=='__main__':
    ip = input('ip address: ')
    check_pwd = input('Need a Password (y/n)')
    CheckVersion(ip, check_pwd)
    pass


# cd("cd C:\\users")

# test1=subprocess.Popen('dirr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd='D:\\')

# print(test1.communicate())
# print(test1.stdout.read())
# print(test1.stderr.read())

# test2=subprocess.run('dir ga*', shell=True, capture_output=True, universal_newlines=True, cwd='C:\\Users\\Shan')

# print(test2.stdout)
# print(type(test2.stdout))
# print(test2.stderr)
# result=test2.stdout
# List=result.split('\n')
# print(List)

test2=subprocess.run('dir sdfds', shell=True, capture_output=True, universal_newlines=True, cwd='C:\\Users\\Shan')

if test2.returncode == 0:
    print(test2.stdout)
else:
    print(test2.stderr)


