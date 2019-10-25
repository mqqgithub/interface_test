import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5 as SIGN_PKCS

PUB_KEY = RSA.importKey(open('public.pem', 'r').read())
PRI_KEY = RSA.importKey(open('private.pem', 'r').read())



def split_data(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


def encrypt(params):
    raw = params.encode('utf-8')
    cipher = PKCS1_v1_5.new(PUB_KEY)
    # 加密超长字节117个字节一加密
    content = b''.join([cipher.encrypt(x) for x in chunks(raw, 117)])
    return base64.b64encode(content)

def decrypt(data):
    raw = data.encode('utf-8')
    decrypt = PKCS1_v1_5.new(PRI_KEY).decrypt
    # 解密超长字符128一解密
    content = b''.join(decrypt(x, object()) for x in chunks(raw, 128))
    return content.decode()

def signer(data):
    signstr = data.encode('utf-8')
    sign = SIGN_PKCS.new(PRI_KEY).sign(SHA.new(signstr))
    return base64.b64encode(sign)

def verify_sign(unsign, raw_sign):
    """
     unsign: 签名
     raw_sign: 待验证签名
    """
    assert SIGN_PKCS.new(PUB_KEY).verify(SHA.new(unsign.encode('utf-8')), raw_sign)

if __name__=='__main__':
    msg = "hello"

