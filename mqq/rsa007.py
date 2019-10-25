from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
import base64
def RSA_sign(encrData):
    privateKey = '''MIICXAIBAAKBgQCQR9a+lcNMyyRwfSGMsaslV+k7Oihb7KKxj+C0NesMElV8190r
+Jj/UcoDP9nV4RXu435x76b3wUAU6weGOOuSIuuVZAGrqOViHg2fTTZPzcdtODAN
2ccDtvk+vm6mLlGQ5pYmc9CtIJv7c0cV+C3jFsvrz3QZg0F5ve+iTHk+YQIDAQAB
AoGANsshkeWccvifER1kdWMwBRGa4MRYeXin3NkwVCA58K6xyqTMORvDNwuftZY1
K1W9F6lL5wdFmMfKh2cux1mslJHBK9igS7ZbInb3J+UZXCxKCnu28Ot/5q9tH2hw
E6xR88pSqT1vlIwVzd61IDcSKNpt9ZKIak4DUg/mAghubOUCQQDm2Krwh5T5HUxX
3s2yahdPLn8BEKR0Jv8Ocb1cGTx5bgpWyth35kE3ryyfnDNIDYRHBw1SKht/sTTI
VP5mCK7nAkEAoAB3qkRne/GB3X5+NLMXCfIG/vqqLo60nKQcjuggZYSjou5fep3N
wsg7h+H8kzME4MCpiKJeTc8yQf64ckdndwJBAIMFpPgCLCa8X1FcTymdl39Ep6cm
GAEpBQjgu5ZjaHSPZWTfmr9qu8dsMIqi8GRL77EUqpXg+lyeapPt0bp94S8CQCdQ
VhbhHehHbBhnZ009n/CSpoNqRfyQlfJTJK08fhFTqP10wsMXGSK+HlqB/ZSRmaY7
0KxA8Rj/SyMKGnoB73sCQDHuYdSgBVb3vndiikBrjuGjwhRTtvgc+TUeoI6f0pqO
4SsYHXT6Rp4IN3O0P0kaU9wC3dX6pq9XpKvtorof5hs='''
    private_keyBytes = base64.b64decode(privateKey)
    print(private_keyBytes)
    print(type(private_keyBytes))
    priKey = RSA.importKey(private_keyBytes)
    print("priKey", priKey)

    #priKey = RSA.importKey(privateKey)
    signer = PKCS1_v1_5.new(priKey)
    print("signer", signer)
    hash_obj = MD5.new(encrData.encode('utf-8'))
    print(type(encrData.encode('utf-8')))
    signature = base64.b64encode(signer.sign(hash_obj))
    print(type(signature))
    print(signature)
    return signature
'''
几个注意事项：
1、密钥如果是读取自.pem文件，密钥会有开始行和结束行，叫做头标注信息和尾标注信息。常见的长这样：

-----BEGIN PRIVATE KEY-----
#密钥内容#
-----END PRIVATE KEY-----

此时直接priKey = RSA.importKey(privateKey)（见被注释掉的部分）即可，不用对私钥进行base64解码；
2、哈希算法可以采用MD5，也可以用别的比如SHA；
3、data是需要签名的数据，需要字节化后才能传进MD5.new()中。字节化有三种方法，示例中采用了第三种：

b'zifuchuang'
bytes('zifuchuang',encoding='utf-8')
'zifuchuang'.encode('utf-8')
'''
def verify(signature,encrData):
    publicKey = '''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQR9a+lcNMyyRwfSGMsaslV+k7Oihb7KKxj+C0
NesMElV8190r+Jj/UcoDP9nV4RXu435x76b3wUAU6weGOOuSIuuVZAGrqOViHg2fTTZPzcdtODAN
2ccDtvk+vm6mLlGQ5pYmc9CtIJv7c0cV+C3jFsvrz3QZg0F5ve+iTHk+YQIDAQAB'''
    public_keyBytes = base64.b64decode(publicKey)
    pubKey = RSA.importKey(public_keyBytes)
    #pubKey = RSA.importKey(publicKey)
    h = MD5.new(encrData.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    return verifier.verify(h, base64.b64decode(signature))
'''
注意事项： 
1、因为签名时我们对RSA_sign()返回的签名值进行过过base64编码，所以验签时需要解码； 
2、函数verifier.verify()返回的是bool值，在外层可以直接用作条件判断。
'''
if __name__=='__main__':
    str1 = 'hello'
    sign = RSA_sign(str1)
    TF = verify(sign, str1)
    print(TF)