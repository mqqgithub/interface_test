import json
import unittest
import urllib.parse
import paramunittest
from common.configHttp import RunMain
from common import geturlParams, read_excel

# import pythoncom
# pythoncom.CoInitialize()

# 调用我们的geturlParams获取我们拼接的URL
url = geturlParams.geturlParams().get_Url()
login_xls = read_excel.ReadExcel.get_xls('user03Case.xlsx', 'login')


# *login_xls 是一个列表，也可以是元组、字典
@paramunittest.parametrized(*login_xls)
class testUserLogin03(unittest.TestCase):
    # 注意这里接受参数的时候，必须要定义setParameters这个方法，并且只能是这个名称。
    # 括号后面的参数分别接受传入的参数名称。前面定义的是字典，那参数就跟前面字典的key保持一致
    def setParameters(self, case_name, path, query, method, result):
        """
        set params
        :param case_name:  用例名字
        :param path ： 文件路径
        :param query： 用户名密码参数
        :param method： http请求方法
        :param result   返回结果
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.result = str(result)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        print(self.case_name+"测试开始前准备")

    def test03case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        s1 = json.loads(info)  # 将响应转换为字典格式
        s2 = json.loads(self.result)
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(s1, s2)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(s1, s2)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(s1, s2)


if __name__ == "__main__":
    # verbosity=2  显示详情
    unittest.main(verbosity=2)
