import paramiko
from paramiko import SSHClient, ssh_exception, AutoAddPolicy

BMC_IP = '10.184.28.181'
ssh_port = 22
def LDAPLogin():
    accounts = ['Admin', 'Operator', 'User']
    pwd = '123456'
    for account in accounts:
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(hostname=BMC_IP, username=account, password=pwd, port=ssh_port)
            ssh.exec_command('show')
            ssh.close()
            print(f'SMASH run {account} Success')
        except ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except TimeoutError as e:
            print(f"Connection timed out: {e}")

def ADLogin():
    accounts = ['ad_spring@satc.com', 'ad_summer@satc.com', 'ad_autumn@satc.com', 'ad_winter@satc.com']
    pwd = 'Super123'
    for account in accounts:
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(hostname=BMC_IP, username=account, password=pwd, port=ssh_port)
            ssh.exec_command('show')
            ssh.close()
            print(f'AD account {account} Login Success')
        except ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except TimeoutError as e:
            print(f"Connection timed out: {e}")

def ssh_bmc():
    account = 'ADMIN'
    pwd = 'ADMIN'

    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=BMC_IP, username=account, password=pwd, port=ssh_port)
        ssh.exec_command('show')
        ssh.close()
        print(f'SSH run {account} Success')
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")

local_path = "D:/CentOS/Upload"
remote_path = "/root"
FileName = '/test1.txt'
def ssh_updoad():
    account = 'root'
    pwd = '111111'
 
    try:
        transport = paramiko.Transport((BMC_IP, ssh_port))
        transport.connect(username=account, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path+FileName, remote_path+FileName)
        print(f'{FileName[1:]}檔案上傳成功')
        sftp.close()
        transport.close()

    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")
    except Exception as e:
        print(f"檔案上傳失敗：{e}")

def ssh_os():
    account = 'root'
    pwd = '111111'
    commands = ['pwd', 'ls -l', 'cat /etc/system-release', 'cat '+FileName[1:], 'rpm -q ipmitool', 'ipmitool lan print']
    try:
        file = open('X13SET.txt','w')
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=BMC_IP, username=account, password=pwd, port=ssh_port)
        for cmd in commands:
            print(f"Execute: {cmd}")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            for result in stdout.readlines():
                # print(result) #str
                file.write(result)
        file.close()
        ssh.close()
        # print(f'SSH run {account} Success')
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")

if __name__=='__main__':
    print(f"Server: {BMC_IP}")
    # LDAPLogin()
    # ADLogin()
    # ssh_bmc()
    # ssh_updoad()
    ssh_os()
