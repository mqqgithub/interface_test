'''
1、商户自己生成rsa的公玥、私钥
2、商户私钥加密biz_content
3、商户用私钥加签名
4、商户上传公钥到商户会员页面
5、商户发请求给kjt
6、kjt用商户公钥解密，验签
7、kjt返回信息不加密，只加签名
8、商户收到kjt返回信息验签（可以不用验签）
'''
#自己生成的公钥上传到商户平台
import rsa
import json

with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
    print("type(f.read()", type(f.read()))
    print("type(pubkey)", type(pubkey))
print(pubkey)
with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
print(privkey)

# 明文
message = 'hello'
msg = {
        "member_id":"200000056550",
        "bank_code":"PBOC",
        "biz_product_code":"30101",
        "amount":"10",
        "out_trade_no":"$param(网关接口外部订单号out_trade_no)",
        "notify_url":"http://10.255.4.54:8002/AlphaTest/gateway/asyncNotify.do"
       }
msg1 = json.dumps(msg)
msg1 = message
# 公钥加密
crypto = rsa.encrypt(msg1.encode(), pubkey)
print(msg1)
print(crypto)

# 私钥解密
msg = rsa.decrypt(crypto, privkey).decode()
print("私钥解密", msg)

# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')
print(signature)
# 公钥验证
s = rsa.verify(message.encode(), signature, pubkey)
print(s)
