import time
import json
import rsa
import base64

money = 1
out_trade_no = 1111111111
biz_content = {"amount": int(money) * 100,
               "pay_type": "KJ-UY",
               "merType": "1",
               "tradeName": "充值{}".format(int(time.time())),
               "bank_no": "1031000",
               "back_notify_url": "http://192.168.0.170:8005/online",
               'front_notify_url': 'http://192.168.0.225:8888/dist/view/chongzhi/',
               "out_trade_no": out_trade_no,
               "remark": "0"
               }
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))),
merchant_no = 'M1001431901xxx'
method = 'jypay.pay.eacq.merchant.pay'
version = '1.0'
dict_map = {'biz_content': json.dumps(biz_content),
            'merchant_no': merchant_no,
            'method': method,
            'version': version,
            'timestamp': timestamp[0]}


#排序加签名
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
'''
#with open('/home/python/tiantian/redpacket/redpacket/red_packet/apps/trade/keys/pkcs1.pem', 'rb') as privatefile:
    with open('private.pem', 'rb') as privatefile:

        # 私钥的绝对路径
        keydata = privatefile.read()
    privatekey = rsa.PrivateKey.load_pkcs1(keydata)
    signature = rsa.sign(content.encode('utf-8'), privatekey, 'SHA-1')
    sign = base64.b64encode(signature).decode('utf-8')
    return sign
'''
#dict_map['sign'] = content_sign(dict_map)
msg = content_sign(dict_map)

pubkey = '''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCBQu/vsaWUzUaMMGU1mD85C87kZP0zghs2akmD
42q5uCTXNPzAfccyfycLp9tgukl49p+QqgTJEiwx/Df8870YGN7qGG2r4EqRnHDfdu4945Hv+bjZ
X/2O7XSKCn7PePmXOIIpwTtvFhcC303yD6yOceqR9OYcSeg4/BY1Uasp4QIDAQAB'''
privkey = '''MIICXAIBAAKBgQCBQu/vsaWUzUaMMGU1mD85C87kZP0zghs2akmD42q5uCTXNPzA
fccyfycLp9tgukl49p+QqgTJEiwx/Df8870YGN7qGG2r4EqRnHDfdu4945Hv+bjZ
X/2O7XSKCn7PePmXOIIpwTtvFhcC303yD6yOceqR9OYcSeg4/BY1Uasp4QIDAQAB
AoGAPbVuBFkjulkRX+XOu3pWXG6Fs8V+l3N6eEzfkcYk8kq108OpEmA5k6LeShM1
iQUGBGiAnrh8Fl3FmYtWUz0tPUCs/9uyIB8Itg+meiiKqaNcT9NHmVzwREV8eilR
YnCzyXH9vJP2oMCMZo30/X6oYwh0mNWUgiAIDbpqD+7FyVECQQDDHupwBTOr3nu4
W5XWo4+dOwchKluWUcsOcSFFO8J1uD+tIMLE5uNEfaiir4b9TaLDncsKKJx2k3XY
aXX8zQg1AkEAqZeS3DGuqjltk+zBBbRrV9/ldB+ZcqFrxBqPVeE7t3XrmNbBrDUW
ZrAMpBiXxDTElDF0M1S1+tV2vL42uqqIfQJAF92gLzNzroH4AASzvx0iY8jkhln3
+drnS0zrFNzKXDu9DiADsrHK+oWkKsHtcO4eCm8ydnuhJ5/Bukar98/cQQJAKGub
8SdWPfQaDdur1bQ+sV8HzTmK1StsB/1clFduaDeOw4rL9kNg53CmUqYZ5gW9pKR0
0ZcrGHGwLyQW3z6t8QJBAKFwa2SrSOTF0pVa5qvUK42HPn4OBFwl0c8ef4KJvBlz
HD0oBFO6ewz+HaycpJudlGprwxCvK/Y6Z4/PpBIrU88='''



# 私钥签名
signature = rsa.sign(msg.encode(), privkey, 'SHA-1')

# 公钥验证
s = rsa.verify(msg.encode(), signature, pubkey)
print(s)








'''
dict_map.items() 返回列表，元素是元组

python3
C = [('e', 4, 2), ('a', 2, 1), ('c', 5, 4), ('b', 3, 3), ('d', 1, 5)]
print(sorted(C, key=lambda y: y[0]))
#输出[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[0]))
#[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[2]))
[('a', 2, 1), ('e', 4, 2), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5)]

key=lambda 元素: 元素[字段索引]
比如   print(sorted(C, key=lambda x: x[2]))   
x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序
'''
'''
安装pycrypto报错
python3.6.2版本安装pycrypto模块【不需要安装Visual Studio】
https://blog.csdn.net/weixin_41754309/article/details/80486936
'''