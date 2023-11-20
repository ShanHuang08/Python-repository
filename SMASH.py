import paramiko
from paramiko import SSHClient, ssh_exception, AutoAddPolicy
import subprocess
from time import sleep

BMC_IP = '10.140.178.255'
OS_IP = '10.184.21.100'
SUT_Name = 'SUT info.txt'
ssh_port = 22
def LDAPLogin():
    print(f"Server: {BMC_IP}")
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
    print(f"Server: {BMC_IP}")
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
    print(f"Server: {BMC_IP}")
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


def ssh_os():
    print(f"Server: {OS_IP}")
    account = 'root'
    pwd = '111111'
    commands = ['cat /etc/system-release', 'rpm -q ipmitool', 'rpm -q tar', 'rpm -q unzip', 'rpm -q tcpdump', 'ipmitool lan print', 'ls -l']
    try:
        file = open(SUT_Name,'w')
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=OS_IP, username=account, password=pwd, port=ssh_port)
        for cmd in commands:
            print(f"Execute: {cmd}")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            for result in stdout.readlines():
                # print(result) #str
                file.write(result)
        file.close()
        ssh.close()
        subprocess.run('notepad '+SUT_Name, shell=True)
        # print(f'SSH run {account} Success')
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")

if __name__=='__main__':
    # LDAPLogin()
    # ADLogin()
    # ssh_bmc()
    # ssh_updoad()
    ssh_os()
