from paramiko import SSHClient, ssh_exception, AutoAddPolicy
from time import sleep

def SMASH(ip):
    accounts = ['Admin', 'Operator', 'User']
    pwd = '123456'
    for account in accounts:
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(hostname=ip, username=account, password=pwd, port=22)
            ssh.exec_command('exit')
            ssh.close()
            sleep(3)
            print(f'SMASH run {account} Success')
        except ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except TimeoutError as e:
            print(f"Connection timed out: {e}")