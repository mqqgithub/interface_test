from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import json
import rsa
import time


def content_sign(dict_map):
    """SHA1withRsa算法"""
    d = sorted(dict_map.items(), key=lambda x: x[0])
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
    with open('private.pem', 'rb') as privatefile:
        # 私钥的绝对路径
        keydata = privatefile.read()
    privatekey = rsa.PrivateKey.load_pkcs1(keydata)
    signature = rsa.sign(content.encode('utf-8'), privatekey, 'SHA-1')
    sign = base64.b64encode(signature).decode('utf-8')
    return sign


biz_content = {"amount": 100,
               "pay_type": "KJ-UY",
               "merType": "1",
               "tradeName": "充值{}".format(int(time.time())),
               "bank_no": "1031000",
               "back_notify_url": "http://192.168.0.170:8005/online",
               'front_notify_url': 'http://192.168.0.225:8888/dist/view/chongzhi/',
               "out_trade_no": "out_trade_no",
               "remark": "0"
               }
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))),
merchant_no = 'M1001431901xxx'
method = 'jypay.pay.eacq.merchant.pay'
version = '1.0'
dict_map = {'biz_content': json.dumps(biz_content), 'merchant_no': merchant_no, 'method': method, 'version': version,
            'timestamp': timestamp[0]}
dict_map['sign'] = content_sign(dict_map)
