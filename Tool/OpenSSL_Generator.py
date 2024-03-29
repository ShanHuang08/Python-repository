from OpenSSL import crypto
from datetime import datetime, timedelta
import subprocess

MySSLFolder='"C:\\Users\\Stephenhuang\\Desktop\SSL Certificate Key"'

def Today():
    date_time=datetime.now()
    date_time=str(date_time)
    return date_time[0:4]+date_time[5:7]+date_time[8:10] 

not_before = datetime.utcnow()
not_after = not_before + timedelta(days=3650)

# 產生 private key
k = crypto.PKey()
k.generate_key(crypto.TYPE_RSA, 2048)

# 產生 certificate
cert = crypto.X509()
cert.set_version(3)
cert.get_subject().CN = "IPMI"
cert.get_subject().OU = "Software"
cert.get_subject().O = "Super Micro Computer"
cert.get_subject().L = "San Jose"
cert.get_subject().ST = "California"
cert.get_subject().C = "US"
cert.get_subject().emailAddress = "support@supermicro.com"
cert.set_serial_number(0)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(int((not_after - not_before).total_seconds()))
cert.set_issuer(cert.get_subject())
cert.set_pubkey(k)
cert.sign(k, 'sha256')

# 將 key 與 certificate 寫入檔案

Now = Today()
open("key_"+Now+".pem", "wb").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
open("cert_"+Now+".pem", "wb").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

subprocess.run(f"move key_{Now}.pem {MySSLFolder}", shell=True)
subprocess.run(f"move cert_{Now}.pem {MySSLFolder}", shell=True)
subprocess.run(f"explorer {MySSLFolder}", shell=True)