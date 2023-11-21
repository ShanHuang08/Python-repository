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

def ssh_reboot(ip, cmd):
    account = 'root'
    pwd = '111111'
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=ip, username=account, password=pwd, port=22)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = [out for out in stdout.readlines()]
        ssh.close()
        if cmd == 'reboot':
            sleep(10)      
        return result
    except ssh_exception.SSHException as e:
        print(f"SSHException occurred: {e}")
    except ssh_exception.NoValidConnectionsError as e:
        print(f'{e}, SSh port is closed!')
    except TimeoutError as e:
        print(f"Connection timed out: {e}")