'''
有些post的请求参数是json格式的，这个前面第二篇post请求里面提到过，需要导入json模块处理。
一般常见的接口返回数据也是json格式的，我们在做判断时候，往往只需要提取其中几个关键的参数就行，这时候就需要json来解析返回的数据了。
Json简介：Json，全名 JavaScript Object Notation，是一种轻量级的数据交换格式,常用于http请求中
首先说下为什么要encode，python里面bool值是True和False,json里面bool值是true和false,并且区分大小写，这就尴尬了，明明都是bool值。
在python里面写的代码，传到json里，肯定识别不了，所以需要把python的代码经过encode后成为json可识别的数据类型。
dict类型经过json.dumps（）后变成str，True变成了true,False变成了fasle

'''

# a = u'哈哈'
# print(type(a))
# b = a.encode('utf-8')  # 字节流Byte
# print(type(b))
# c = b.decode('utf-8')  # 字符串str
# print(type(c))


# str(unicode)--->encode(utf-8)--->bytes()--->decode(utf-8)--->tr(unicode)