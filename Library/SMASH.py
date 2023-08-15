from paramiko import SSHClient, ssh_exception, AutoAddPolicy
import socket

def SMASH(ip):
    accounts = ['Admin', 'Operator', 'User']
    pwd = '123456'
    for account in accounts:
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(hostname=ip, username=account, password=pwd, port=22)
            ssh.exec_command('show')
            ssh.close()
            print(f'SMASH run {account} Success')
        except ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except socket.gaierror as e:
            print(f"socket.gaierror occurred: {str(e)}")