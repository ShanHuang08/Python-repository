from OpenSSL import crypto

# 產生 RSA key
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

# 將 key 存成 pem 檔
with open("key.pem", "wb") as f:
    f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))



# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\OneDrive - Super Micro Computer, Inc\文件\Python\test.py", line 1, in <module>
#     from OpenSSL import crypto
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\OpenSSL\__init__.py", line 8, in <module>
#     from OpenSSL import crypto, SSL
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\OpenSSL\crypto.py", line 12, in <module>
#     from cryptography import x509
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\cryptography\x509\__init__.py", line 8, in <module>
#     from cryptography.x509.base import (
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\cryptography\x509\base.py", line 18, in <module>
#     from cryptography.x509.extensions import Extension, ExtensionType
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\cryptography\x509\extensions.py", line 20, in <module>
#     from cryptography.hazmat.primitives import constant_time, serialization
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\cryptography\hazmat\primitives\constant_time.py", line 11, in <module>
#     from cryptography.hazmat.bindings._constant_time import lib
# ModuleNotFoundError: No module named 'cryptography.hazmat.bindings._constant_time'

