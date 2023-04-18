import paramiko
from time import sleep    

def login_with_user_pw(hostname, user, pw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=port, username=user, password=pw)
    ssh.exec_command('show')
    ssh.close()

if __name__=='__main__':
    hostname = '10.184.20.0'
    port='22'
    users = ['ADMIN', 'Operator', 'User']
    pw = '123456'
    for i in users:
        login_with_user_pw(hostname, i, pw)
        print(f'{i} is done')
        sleep(3)