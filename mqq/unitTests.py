'''
https://www.cnblogs.com/yufeihlf/p/5707929.html
unittest的重要属性：'TestCase'、 'TestSuite'、'TextTestRunner'、'main'、 'skip'、 'skipIf'、'skipUnless'

'''
import unittest
import paramunittest
import time
import os
import common.HTMLTestRunner as HTMLTestRunner

data1 = [{"user": "admin", "psw": "123", "result": "true"},
         {"user": "admin1", "psw": "1234", "result": "true"},
         {"user": "admin2", "psw": "1234", "result": "true"},
         {"user": "admin3", "psw": "1234", "result": "true"},
         {"user": "admin4", "psw": "1234", "result": "true"}]
data2 = [['admin1', 'psw', 'true'], ['admin2', 'psw', 'true']]
#加载可用参数
@paramunittest.parametrized(*data1)
class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result
    def setUp(self):
        print('测试前置条件--')
    def tearDown(self):
        print('测试结束收尾--')
    def testcase(self):#测试用例以test开头，执行顺序a-z，0-9
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        self.assertEqual(self.result, 'true')
        time.sleep(0.5)
        self.assertTrue(self.result == "true")


if __name__ == "__main__":
    #unittest.main(verbosity=2)

    path = os.path.split(os.path.relpath(__file__))[0]
    report_path = path.join(os.path.dirname(path), 'result', 'report.html')
    HTMLfile = open('report_path', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=HTMLfile, title='Test Report', description='Test Description')
    runner.run(testcase())
