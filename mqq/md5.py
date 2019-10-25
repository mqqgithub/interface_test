'''部分业务为了安全需要，需要对接口请求数据做签名校验，一般制定一下规则：

1、业务方接入系统，需申请业务ID以及加密秘钥，二者成对出现，并且为面向服务端的，不能在前端或者客户端传递。

2、所有值非空的参数必须参与签名

3、签名算法：

a. 对所有参数按参数名的字典升序排序
b. 将所有排好序的参数按照key1=value1&key2=value2&key3=value......的格式拼接成一个字符串，记为signStr
c. 在signStr后，继续添加 &key=加密密钥
d. 对signStr进行MD5签名

针对某一get接口做实例说明：
---------------------
作者：qianmo0417
来源：CSDN
原文：https://blog.csdn.net/qianmo0417/article/details/85785474
版权声明：本文为博主原创文章，转载请附上博文链接！'''


# !/usr/bin/env python#coding:utf-8
import hashlib
import json
import requests

# 测试的域名
domain = "http://******/***/vip2.ldo?"
# get 传递的非sign参数
url_params = {
    'type': 'orderList',
    'userId': '198049148',
    'country': 86,
    'typeGroup': '',
    'status': '',
    'rows': '20',
    'page': '1',
    'businessId': '2',
}
sign = "sign=###################"
# 删除空值的参数，以用来签名
for key in list(url_params.keys()):
    if not url_params.get(key):
        del url_params[key]
# 按照升序排列，得到的是一个列表，列表的元素为元组
url_params1 = sorted(url_params.items(), key=lambda d: d[0], reverse=False)

values = []
for li in url_params1:
    newsmbol = ('=',)
    # 元组中增加一个新元素
    li = li[:1] + newsmbol + li[1:]
    # 元组转化为字符串，整型不能转化，list包含数字，不能直接转化成字符串
    value = "".join('%s' % id for id in li)
    values.append(value)
# 列表复制不能用= 需要用copy 或者list[:]
values1 = values[:]
values1.append(sign)
sign1 = "&".join(values1)
# md5 调用库函数
sign2 = hashlib.md5(sign1.encode('utf-8')).hexdigest()
sign = 'sign=' + sign2
values.append(sign)
para = "&".join(values)
url = domain + para
print(url)

res = requests.get(url)
print('***---***---***')
print(res.content)
print('***---***---***')
print(res.headers)
print('***---***---***')
print(res.status_code)
if res.status_code == 200:
    print('请求成功')
print('***---***---***')
# json 格式打印
print(json.dumps(res.json(), indent=4))
print('***---***---***')
# 两种方法
if json.loads(res.text)['msg'] == 'success':
    print('True')
else:
    print('error')
if res.json()['msg'] == 'success':
    print('True')
else:
    print('error')
