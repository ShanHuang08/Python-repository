from Library.SMASH import ssh_reboot
os_ip = '10.184.22.137'

def Check_Host_Interface():
    stdout = ssh_reboot(ip=os_ip, cmd='ip add') 
    testList = []
    for i in stdout:
        if '169.254.3' in i:
            testList.append('Enable')

    if len(testList) > 0:
        print('Host interface Enable')
    else:
        print('Host interface Disable')


Check_Host_Interface()