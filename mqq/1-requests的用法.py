'''

'''

import requests
import json
# get参数传递方式一 返回的是json格式的
r = requests.get('http://127.0.0.1:8888/login?name=xiaoming&pwd=111')
result = r.json() # 返回的是字典值
print(result['code'])

data = {'name': 'xiaoming', 'pwd': '111'}
# get参数传递方式二
r = requests.get('http://127.0.0.1:8888/login', params=data)
print(type(r.json()))


# post字典方式传参
r = requests.post('http://127.0.0.1:8888/login', data=data)
print(r.json())
# post以json方式传参
dat = json.dumps(data)
r = requests.post('http://127.0.0.1:8888/login', json=dat)
print(r.json())

# post加请求头
# r1 =  requests.session().post(url, data=body1, headers=h, verify=False)

# print(r.apparent_encoding) # 获取网页编码格式
# print(r.status_code)
# print(r.url)
# print(r.encoding)
# print(type(r.headers))
# print(r.raw)
# print(r.cookies)
# r.text返回的是字符串是Unicode
# print(type(r.text))

# r.content返回的是字节码Byte型 就是01,字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text是按照Unicode编码后的str，如果返回的响应信息中有中文，则会出现乱码，
# 此时用r.content.decode(utf-8)对字节进行utf-8解码就为Unicode的str可以正确展示,可见服务器返回的是进行过utf-8编码的字节流
# r.text返回的是处理过的Unicode型的数据，而使用r.content返回的是bytes型的原始数据。
# 也就是说，r.content相对于r.text来说节省了计算资源，r.content是把内容bytes返回.
# 而r.text是decode成Unicode. 如果headers没有charset字符集的化,text()会调用chardet来计算字符集。
# print(type(r.content))
# a = u'哈哈'
# print(type(a))
# b = a.encode('utf-8')  # 字节流Byte
# print(type(b))
# c = b.decode('utf-8')  # 字符串str
# print(type(c))

# str(unicode)--->encode(utf-8)--->bytes()--->decode(utf-8)--->tr(unicode)
