import json
import unittest
from common.configHttp import RunMain
import paramunittest
from common import geturlParams, read_excel
import urllib.parse
# import pythoncom
# pythoncom.CoInitialize()

# 调用我们的geturlParams获取我们拼接的URL
url = geturlParams.geturlParams().get_Url()
login_xls = read_excel.ReadExcel.get_xls('userCase.xlsx', 'login')
# login_xls是一个列表，每行值也是一个列表，列表中的列表
# print('输入参数值', login_xls)


# 加载列表中的值
@paramunittest.parametrized(*login_xls)
class testUserLogin01(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:用例名字
        :param path ：文件路径
        :param query：
        :param method：post/get
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

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
        print(self.case_name+"测试开始前准备")

    def test01case(self):
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

        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))

        # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        info = RunMain().run_main(self.method, url, data1)

        # 将响应转换为字典格式
        ss = json.loads(info)

        # 如果case_name是login，说明合法，返回的code应该为200
        if self.case_name == 'login':
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'], 10001)


if __name__ == "__main__":
    unittest.main(verbosity=2)
