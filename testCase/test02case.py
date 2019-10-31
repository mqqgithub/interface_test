import json
import unittest
from common.configHttp import RunMain
import paramunittest
from common import geturlParams, readExcel
import urllib.parse

# import pythoncom
# pythoncom.CoInitialize()
# 调用我们的geturlParams获取我们拼接的URL
url = geturlParams.geturlParams().get_Url()
login_xls = readExcel.readExcel().get_xls('user02Case.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin02(unittest.TestCase):
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
        self.result = int(str(result))

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test02case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], self.result)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(ss['code'], self.result)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(ss['code'], self.result)


if __name__ == "__main__":
    unittest.main(verbosity=2)