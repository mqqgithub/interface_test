from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import json

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
            res.append(pubobj.encrypt(msg[offset:offset+default_length]))
        else:
            res.append(pubobj.encrypt(msg[offset:]))
        offset += default_length
    byte_data = b''.join(res)
    #使用base64算法将二进制流转成字符串方便进行放入需要的参数里面进行传递
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
#字典字符串
msg1 = {"ApplyId":"20180504002","ChannelId":"O00420000001","LoanId":"9996401-5077812265125477811","LoanAmount":"5000.00","LoanPeriod":6,"LoanCardNo":"6225768313133272","BankId":"BANKLIST/ZHAOHANG"}
msg = json.dumps(msg1)
#加密字符串
with open('private.pem') as f:
    '''读取公钥并加密'''
    key = f.read()
    print("public.pem", key)
    result = rsa_long_encrypt(key, msg)
    print("加密文", result.decode('utf-8'))
#解密字符串
with open('private.pem') as f:
    '''读取私钥并解密'''
    key1 = f.read()
    data = rsa_long_encrypt(key, msg)
    result1 = rsa_long_decrypt(key1, data)
    print("解密文", result1.decode('utf-8'))