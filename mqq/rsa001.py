# pip install   rsa

import rsa

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)
#print(pubkey.save_pkcs1())
#print(privkey.save_pkcs1())
# 保存密钥   decode() Unicode编码为utf-8 （硬盘文件）
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())

# 导入密钥  encode() utf-8解码为Unicode  （内存）
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
print(pubkey)
with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
print(privkey)


# 明文
message = 'hello'

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)

# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

# 公钥验证
rsa.verify(message.encode(), signature, pubkey)


