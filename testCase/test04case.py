# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;
import unittest
import HTMLReport


class Test04(unittest.TestCase):
    def setUp(self):
        print('test04_start...')

    def test04(self):
        print('test04_doing...')

    def tearDown(self):
        print('test04_end...')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    runner = HTMLReport.TestRunner(title="功能测试+a")