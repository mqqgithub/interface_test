

#使用sorted函数进行排序
#ascll 0`9  A~Z  a~z
'''
sorted(iterable,key,reverse)，sorted一共有iterable,key,reverse这三个参数;
其中iterable表示可以迭代的对象，例如可以是dict.items()、dict.keys()等
key是一个函数，用来选取参与比较的元素，reverse则是用来指定排序是倒序还是顺序，reverse=true则是倒序，
reverse=false时则是顺序，默认时reverse=false。
'''
#初始化字典
dict_data = {"c": 9, "b": 5, "a": 11, "B": 2, "w": 6}
#对字典按键（key）进行排序（默认由小到大）
test_data_0 = sorted(dict_data.keys())
#输出结果
print(test_data_0)
test_data_1 = sorted(dict_data.items(), key=lambda x: x[0])
#输出结果
print(test_data_1)
'''*********************
#对字典按值（value）进行排序（默认由小到大）
test_data_2=sorted(dict_data.items(),key=lambda x:x[1])
#输出结果
print(test_data_2) #[('8', 2), ('10', 5), ('7', 6), ('6', 9), ('3', 11)]
test_data_3=sorted(dict_data.items(),key=lambda x:x[1],reverse=True)
#输出结果
print(test_data_3) #[('3', 11), ('6', 9), ('7', 6), ('10', 5), ('8', 2)]
'''
'''**************************************
import operator
#初始化字典
dict_data={6:9,10:5,3:11,8:2,7:6}
#按键（key）进行排序
test_data_4=sorted(dict_data.items(),key=operator.itemgetter(0))
test_data_5=sorted(dict_data.items(),key=operator.itemgetter(0),reverse=True)
print(test_data_4) #[(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]
print(test_data_5) #[(10, 5), (8, 2), (7, 6), (6, 9), (3, 11)]
#按值（value）进行排序
test_data_6=sorted(dict_data.items(),key=operator.itemgetter(1))
test_data_7=sorted(dict_data.items(),key=operator.itemgetter(1),reverse=True)
print(test_data_6) #[(8, 2), (10, 5), (7, 6), (6, 9), (3, 11)]
print(test_data_7) #[(3, 11), (6, 9), (7, 6), (10, 5), (8, 2)]
'''
''''*********************************'''
'''
附：operator库常用函数说明
操作
语法
函数

相加        a + b          add(a, b)
字符串拼接  seq1 + seq2    concat(seq1, seq2)
包含测试    obj in seq     contains(seq, obj)
普通除法    a / b          truediv(a, b)
取整除法    a // b         floordiv(a, b)
按位与      a & b          and_(a, b)
按位异或    a ^ b          xor(a, b)
按位取反    ~ a            invert(a)
按位或      a | b          or_(a, b)
指数运算    a ** b         pow(a, b)
识别        a is b         is_(a, b)
识别        a is not b      is_not(a, b)
索引赋值    obj[k] = v      setitem(obj, k, v)
索引删除    del obj[k]      delitem(obj, k)
索引        obj[k]          getitem(obj, k)
左移        a << b          lshift(a, b)
取模        a % b           mod(a, b)
乘法        a * b           mul(a, b)
负数        -a              neg(a)
非运算      not a           not_(a)
正数        + a             pos(a)
右移运算    a >> b          rshift(a, b)
切片赋值    seq[i:j] = values     setitem(seq, slice(i, j), values)
切片删除    del seq[i:j]          delitem(seq, slice(i, j))
切片        seq[i: j]             getitem(seq, slice(i, j))
字符串格式化 s % obj               mod(s, obj)
减法        a - b sub(a, b)
真值测试    obj truth(obj)
小于        a < b lt(a, b)
小于等于    a <= b le(a, b)
等于        a == b eq(a, b)
不等于      a != b ne(a, b)
大于等于    a >= b ge(a, b)
大于        a > b gt(a, b)
'''

