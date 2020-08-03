'''
r=requests.get(url,params,**kwargs)
url: 需要爬取的网站地址。
params: 翻译过来就是参数， url中的额外参数，字典或者字节流格式，可选。
**kwargs : 12个控制访问的参数
**kwargs有以下的参数，对于requests.get,其第一个参数被提出来了。

params：字典或字节序列， 作为参数增加到url中,使用这个参数可以把一些键值对以?key1=value1&key2=value2的模式增加到url中

例如：kv = {'key1':' values', 'key2': 'values'}
r = requests.get('http:www.python123.io/ws', params=kw)

data：字典，字节序或文件对象，重点作为向服务器提供或提交资源是提交，，作为request的内容，与params不同的是，data提交的数据并不放在url链接里， 而是放在url链接对应位置的地方作为数据来存储。，它也可以接受一个字符串对象。
json：json格式的数据， json合适在相关的html，http相关的web开发中非常常见， 也是http最经常使用的数据格式， 他是作为内容部分可以向服务器提交。
例如：kv = {'key1': 'value1'}
r = requests.post('http://python123.io/ws', json=kv)

headers：字典是http的相关语，对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何我们想模拟的浏览器来对url发起访问。


例子： hd = {'user-agent': 'Chrome/10'}
r = requests.post('http://python123.io/ws', headers=hd)

cookies：字典或CookieJar，指的是从http中解析cookie
auth：元组，用来支持http认证功能
files：字典， 是用来向服务器传输文件时使用的字段。


例子：fs = {'files': open('data.txt', 'rb')}
r = requests.post('http://python123.io/ws', files=fs)

timeout: 用于设定超时时间， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一个timeout的异常。
proxies：字典， 用来设置访问代理服务器。
allow_redirects: 开关， 表示是否允许对url进行重定向， 默认为True。
stream: 开关， 指是否对获取内容进行立即下载， 默认为True。
verify：开关， 用于认证SSL证书， 默认为True。
cert：  用于设置保存本地SSL证书路径

其中response对象有以下属性：
r.status_code	     http请求的返回状态，若为200则表示请求成功。
r.text	             http响应内容的字符串形式，即返回的页面内容
r.encoding	         从http header 中猜测的相应内容编码方式
r.apparent_encoding	 从内容中分析出的响应内容编码方式（备选编码方式）
r.content	         http响应内容的二进制形式

'''

import requests
import json
# get参数传递方式一     参数直接放在url中
r = requests.get('http://127.0.0.1:8888/login?name=xiaoming&pwd=111')
result = r.json()  # 返回的值是json的
print(r)
print(result)
print(result['code'])
print(r.status_code)
print("*"*10)

data = {'name': 'xiaoming', 'pwd': '111'}
# data = "name=xiaoming&pwd=111"
# get参数传递方式二
r = requests.get('http://127.0.0.1:8888/login', params=data)
print(r)
print(type(r.json()))
print(r.content)
print("*"*10)

# post字典方式传参  data /json
'''
data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
data为str时，如果不指定content-type，默认为text/plain
json为dict时，如果不指定content-type，默认为application/json
json为str时，如果不指定content-type，默认为application/json
用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，
用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式

<json> = json.dumps(<dict>)  返回是json字符串
<dict> = json.loads(<json>)  返回是一个字段对象
'''
r = requests.post('http://127.0.0.1:8888/login', data=data)
print(r.json())
# post以json方式传参
dat = json.dumps(data)
r = requests.post('http://127.0.0.1:8888/login', json=dat)
print(r.json())
print("*"*10)
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

# str(unicode)--->encode(utf-8)--->bytes()--->decode(utf-8)--->str(unicode)
