from paramiko import SSHClient, ssh_exception, AutoAddPolicy
import socket

BMC_IP = '10.184.19.36'
account = 'ADMIN'
pwd = 'ADMIN'

try:
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=BMC_IP, username=account, password=pwd)
    ssh.exec_command('show')
    ssh.close()
    print(f'SSH run {account} Success')
except ssh_exception.SSHException as e:
    print(f"SSHException occurred: {str(e)}")
except ssh_exception.NoValidConnectionsError as e:
    print(f'{str(e)}, SSh port is closed!')
except socket.gaierror as e:
    print(f"socket.gaierror occurred: {str(e)}")