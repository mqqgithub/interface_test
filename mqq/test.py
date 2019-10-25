import urllib.parse
import requests
from datetime import datetime
import random
import rsa
import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64


private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCLu4QoPlNizz1PoMRUWUlPyoAQ3FS8ZhYqb0CCO2GEMFZ2meAL
1da+UrhXkJrLhjFLpcUdOwDqjvHS7kVM8M7S0iV7LzN8955rBdAiJDzzGBpv5pKv
NrvJMvsVCmabZu8FQ9QjinhAO4W7AtL+XZGDgQTRGCjbXdg6Kjym+InjawIDAQAB
AoGAB0VAgR+NEy0ZUZVZ4dGrgN1WgIoWVp8xNBAJ2TzhvBEPzqf/Al6kB88iDFxX
0ZMv6XG8qeKyD4JUjtca///fowDfjBKVbayW2E7BgxPfc6Ac+6I9eQsCVonH54nO
qlHF/l2lP3Xl1TXmoCJX2G/EsEmtuUh3k3zm+a+49DHWGqECQQDCk5uZMjfU01eq
+ngAL/MIdpdsbHPraMtLV7zzcH3IsLwBgg7mZCkkSXWDDSaMKoQLukJR/MRHajWi
0HIYLtrzAkEAt9fFTOvHnKxg3EZJfhlZlMY/iTsn456Mr3MyuY4N+E7Ktmm4g9mZ
lpJz+MrjtWP9oPuolcKwzUYI1LM7bGuDqQJACTc0h2z5d/sKi+6RAHFE8YGsalY4
p02vU0I0kNMjIf486VVfn0nfKPjRuANHcBwTZPrNaVSvdzJwl+WHgd22QQJBAJ5f
Mad/IjlUwihgIGWR3vrsAcXtgQJ0DkwCmDsDJgO3lKep0Xs8FDSDO4ai+aDEX7Sz
tto0muxrHaZmNJXE1OkCQQCnAT9a55y0xcH4nXeqiaTuXreOhv+F4NgcrINB525M
8BTBAxiCnRtIhC3oCOWNqFr93oLzZeQOpj3RxsnYmoP8
-----END RSA PRIVATE KEY-----"""

public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCLu4QoPlNizz1PoMRUWUlPyoAQ3FS8ZhYqb0CC
O2GEMFZ2meAL1da+UrhXkJrLhjFLpcUdOwDqjvHS7kVM8M7S0iV7LzN8955rBdAiJDzzGBpv5pKv
NrvJMvsVCmabZu8FQ9QjinhAO4W7AtL+XZGDgQTRGCjbXdg6Kjym+InjawIDAQAB
-----END PUBLIC KEY-----
"""

#把当前的时间戳生成数字字符串
now = datetime.now() #初始化datetime类的时间
timestamp = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
request_no = datetime.strftime(now, '%Y%m%d%H%M%S')+"".join(random.choice("0123456789") for i in range(9))
out_trade_no = datetime.strftime(now, '%Y%m%d%H%M%S')+"".join(random.choice("0123456789") for i in range(9))

dat = {
    "charset":"UTF-8",
    "format":"JSON",
    "partner_id":"200000056550",
    "request_no":"$param(网关接口公共参数request_no)",
    "service":"entry_account_offline",
    "timestamp":"$param(网关接口公共参数timestamp)",
    "version":"1.0",
    "biz_content":{
        "member_id":"200000056550",
        "bank_code":"PBOC",
        "biz_product_code":"30101",
        "amount":"10",
        "out_trade_no":"$param(网关接口外部订单号out_trade_no)",
        "notify_url":"http://10.255.4.54:8002/AlphaTest/gateway/asyncNotify.do"
    }
}
#时间为当前时间
dat["timestamp"] = timestamp
#请求流水号是随机
dat["request_no"] = request_no
#订单号随机
dat["biz_content"]["out_trade_no"] = out_trade_no

print("请求参数", dat)

#对biz_content文件进行加密




'''
单次加密串的长度最大为(key_size/8 - 11)
加密的 plaintext 最大长度是 证书key位数/8 - 11, 例如1024 bit的证书，被加密的串最长 1024/8 - 11=117,
解决办法是 分块 加密，然后分块解密就行了，
因为 证书key固定的情况下，加密出来的串长度是固定的。
'''
#分段加密
def rsa_long_encrypt(pub_key_str, msg):
    msg = msg.encode('utf-8')
    length = len(msg)
    default_length = 117
    #公钥加密
    pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(pub_key_str))

    #长度不用分段
    if length < default_length:
        return base64.b64encode(pubobj.encrypt(msg))
    #需要分段
    offset = 0
    res = []
    while length - offset > 0:
        if length - offset > default_length:
            res.append(pubobj.encrypt(msg[offset:offset+default_length]))#切片
        else:
            res.append(pubobj.encrypt(msg[offset:]))
        offset += default_length
    byte_data = b''.join(res)
    print("mmm", type(base64.b64encode(byte_data)))
    return base64.b64encode(byte_data)
#分段解密
def rsa_long_decrypt(priv_key_str, msg):
    msg = base64.b64decode(msg)
    length = len(msg)
    default_length = 128

    #私钥解密
    priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(priv_key_str))
    #长度不用分段
    if length < default_length:
        return b''.join(priobj.decrypt(msg, b'xyz'))
    #需要分段
    offset = 0
    res = []
    while length - offset > 0:
        if length - offset > default_length:
            res.append(priobj.decrypt(msg[offset:offset+default_length], b'xyz'))
        else:
            res.append(priobj.decrypt(msg[offset:], b'xyz'))
        offset += default_length

    return b''.join(res)
#加签名排序
def content_sign(dict_map):
    """SHA1withRsa算法"""
    d = sorted(dict_map.items(), key=lambda x: x[0])

    print("d:", d)
    list_l = []
    for i in range(len(d)):
        k, v = d[i]
        if i == 0:
            str1 = k + "=" + v
            list_l.append(str1)
        else:
            str2 = "&" + str(k) + "=" + str(v)
            list_l.append(str2)
    content = ''.join([str(i) for i in list_l])
    print("**content**", content)
    return content
msg1 = dat["biz_content"]
msg = json.dumps(msg1)
print("加密前msg", msg)
#with open('private.pem') as f1:
#    '''读取公钥并加密'''
#    key = f1.read()
#    print("public.pem", key)
#    result = rsa_long_encrypt(key, msg)
#    print("加密文", result.decode('utf-8'))

result = rsa_long_encrypt(public_key, msg)
print("加密文", result.decode('utf-8'))
result1 = rsa_long_decrypt(private_key, result)
print("解密文", result1.decode('utf-8'))

#解密字符串
#with open('private.pem') as f2:
#    '''读取私钥并解密'''
#    key1 = f2.read()
#    data = rsa_long_encrypt(key, msg)
#    result1 = rsa_long_decrypt(key1, data)
#    print("解密文", result1.decode('utf-8'))



#赋值给
dat["biz_content"] = result.decode('utf-8')
print("加密后：", dat["biz_content"])

#签名值设置在公共字段sign中

print("dat字典值", dat)
msg2 = content_sign(dat)


# 私钥签名
print("私钥签名之前数据", msg2)
#with open('private.pem', 'r') as f:
#    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
#    signature = rsa.sign(msg2.encode(), privkey, 'SHA-1')
#    print("私钥签名", signature)
rsakey1 = RSA.importKey(private_key)  # 导入读取到的私钥
signer = Signature_pkcs1_v1_5.new(rsakey1)
digest = SHA.new()
digest.update(msg2.encode("utf8"))
sign = signer.sign(digest)
signature = base64.b64encode(sign)
# 公钥验证
#with open('public.pem', 'r') as f:
#    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
#   s = rsa.verify(msg2.encode(), signature, pubkey)
#    print("公钥验证",s)
rsakey2 = RSA.importKey(public_key)  # 导入读取到的公钥
verifier = Signature_pkcs1_v1_5.new(rsakey2)
digest = SHA.new()
digest.update(msg2.encode("utf8"))
is_verify = verifier.verify(digest, base64.b64decode(signature))
print("验签结果", is_verify)

dat['sign'] = signature
print("价加签后dat['sign']", dat['sign'])
dat['sign_type'] = "RSA"

print("进行urlencode")
import urllib

dat["timestamp"] = urllib.parse.quote(timestamp)
dat["biz_content"] = urllib.parse.quote(result.decode('utf-8'))

dat1 = urllib.parse.urlencode(dat)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#注：非Java程序无demo的情况，RSA证书签名验签算法使用“SHA1withRSA”，加密解密算法使用“RSA”，密钥长度1024。
#平台或商户生成RSA密钥对，公钥通过登录到快捷通商户官网进行上传（参考RSA公钥上传），私钥用于与快捷通系统交互数据传输中的加解密及签名、验签，请平台或商户妥善保管。
print(dat)
print(type(dat1))
print("url=====", dat1)
#   	https://c1gateway.kjtpay.com/recv.do
#       https://zgateway.kjtpay.com/recv.do
r = requests.post("https://c1gateway.kjtpay.com/recv.do", data=dat, headers=headers)

print(r)