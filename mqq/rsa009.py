from pprint import pprint
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
'''

# rsa算法生成实例
def get_key():
    rsa = RSA.generate(1024, Random.new().read)
    # master的秘钥对的生成
    private_pem = rsa.exportKey()
    public_pem = rsa.publickey().exportKey()

    return {
        "public_key": public_pem.decode(),
        "private_key": private_pem.decode()
    }
'''

# 生成的公钥私钥对
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCQR9a+lcNMyyRwfSGMsaslV+k7Oihb7KKxj+C0NesMElV8190r
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
4SsYHXT6Rp4IN3O0P0kaU9wC3dX6pq9XpKvtorof5hs=
-----END RSA PRIVATE KEY-----"""

public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQR9a+lcNMyyRwfSGMsaslV+k7Oihb7KKxj+C0
NesMElV8190r+Jj/UcoDP9nV4RXu435x76b3wUAU6weGOOuSIuuVZAGrqOViHg2fTTZPzcdtODAN
2ccDtvk+vm6mLlGQ5pYmc9CtIJv7c0cV+C3jFsvrz3QZg0F5ve+iTHk+YQIDAQAB
-----END PUBLIC KEY-----
"""


print("公钥加密")
def rsa_encode(message, public_key):
    rsakey = RSA.importKey(public_key)  # 导入读取到的公钥
    cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
    cipher_text = base64.b64encode(
        cipher.encrypt(message.encode(encoding="utf-8")))
    # 公钥每次加密的结果不一样跟对数据的padding（填充）有关
    return cipher_text.decode()


print("公钥解密")
def rsa_decode(cipher_text, private_key):
    rsakey = RSA.importKey(private_key)  # 导入读取到的私钥
    cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")
    return text.decode()

print( "签名")
def rsa_sign(cipher_text, private_key):
    rsakey = RSA.importKey(private_key)  # 导入读取到的私钥
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(cipher_text.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    #print(signature)
    return signature

#B使用A的公钥进行验签
print ("验签")
def sign_verify(signature):
    rsakey = RSA.importKey(public_key)  # 导入读取到的公钥
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    is_verify = verifier.verify(digest, base64.b64decode(signature))
    #print(is_verify)
    return is_verify

if __name__ == '__main__':
    message = "你好，世界！"
    cipher = rsa_encode(message, public_key)
    print("加密后：", cipher)
    # 输出是一行，天长了，折行显示
    # vyuQHYhjYrPZK6pJMbbcjb1Q7JTLyRDPIoV7z6OkMQsuBNk0++C
    # tb3dzo0EvjUhaSOZnE9LjODgEqeTR7I459cDp8izmb970BnKj74
    # 6SBtGunK24nudW86ek0JXdYsF5T/IPaphU8d56rdjW+wZv7OfSL
    # m2HgXLXCI6NbJuJXhg=
    msg = rsa_decode(cipher, private_key)
    print("解密后", msg)
    signature = rsa_sign(msg, private_key)
    is_verify = sign_verify(signature)
    print("验签结果：", is_verify)

