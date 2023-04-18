from OpenSSL import crypto

# 產生 RSA key
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

# 將 key 存成 pem 檔
with open("key.pem", "wb") as f:
    f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
