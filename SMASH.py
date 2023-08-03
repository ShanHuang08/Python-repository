import paramiko
import socket

BMC_IP = '10.184.13.213'
def LDAPLogin():
    accounts = ['Admin', 'Operator', 'User']
    pwd = '123456'
    for account in accounts:
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

def ADLogin():
    accounts = ['ad_spring@satc.com', 'ad_summer@satc.com', 'ad_autumn@satc.com', 'ad_winter@satc.com']
    pwd = 'Super123'
    for account in accounts:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=BMC_IP, username=account, password=pwd)
            ssh.exec_command('show')
            ssh.close()
            print(f'AD account {account} Login Success')
        except paramiko.ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except socket.gaierror as e:
            print(f"socket.gaierror occurred: {str(e)}")

if __name__=='__main__':
    LDAPLogin()
    # ADLogin()
