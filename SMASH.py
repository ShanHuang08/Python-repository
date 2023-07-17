import paramiko
import socket

BMC_IP = '10.184.22.196'
accounts = ['Admin', 'Operator', 'User']
pwd = '123456'
for account in accounts:
    print(f'Login {account}')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=BMC_IP, username=account, password=pwd)
        ssh.exec_command('show')
        ssh.close()
        print(f'SMASH run {account} Success')
    except paramiko.ssh_exception.SSHException as e:
        print(f"SSHException occurred: {str(e)}")
    except socket.gaierror as e:
        print(f"socket.gaierror occurred: {str(e)}")