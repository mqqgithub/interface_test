import flask
import json
from flask import request
import pytest

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
'''
# 创建一个实例，服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据  http://127.0.0.1:8888/login?name=xiaoming&pwd=11199
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 判断用户名、密码都不为空
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            resu = {'code': 200, 'message': '登录成功'}
            # json是把字符串格式转为字典，dumps是将字典转换字符串
            # json.dumps序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii = False：
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code': -1, 'message': '账号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')

'''
http://127.0.0.1:8888/login?name=xiaoming&pwd=11199   
浏览器中输入查看返回值 {"code": -1, "message": "账号密码错误"}

app.run()用法参考https://blog.csdn.net/g_sangsk/article/details/80754240
'''