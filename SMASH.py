from paramiko import SSHClient, ssh_exception, AutoAddPolicy
import socket

BMC_IP = '10.184.26.174'
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
        except socket.gaierror as e:
            print(f"socket.gaierror occurred: {str(e)}")

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
        except socket.gaierror as e:
            print(f"socket.gaierror occurred: {str(e)}")

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
    except socket.gaierror as e:
        print(f"socket.gaierror occurred: {str(e)}")

def ssh_os():
    account = 'root'
    pwd = '111111'

    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=BMC_IP, username=account, password=pwd, port=ssh_port)
        stdin, stdout, stderr = ssh.exec_command('ip addr')
        result = stdout.read()
        print(result)
        ssh.close()
        print(f'SSH run {account} Success')
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{str(e)}, SSh port is closed!')
    except socket.gaierror as e:
        print(f"socket.gaierror occurred: {str(e)}")

if __name__=='__main__':
    print(f"Server: {BMC_IP}")
    # LDAPLogin()
    # ADLogin()
    ssh_bmc()
    # ssh_os()
