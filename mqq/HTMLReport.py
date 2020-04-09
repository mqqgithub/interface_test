# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

import unittest
import HTMLReport

class Test(unittest.TestCase):

    def setUp(self):
        print('test start....')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')

    def tearDown(self):
        print('test over....')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test01"))
    suite.addTest(Test("test02"))
    print(suite)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()

