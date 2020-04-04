# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;
import unittest
import HTMLReport
from common.log import Log

log = Log()


class Test04(unittest.TestCase):
    def setUp(self):
        print('test04_start...')

    def test0401(self):
        print('test04_doing...')
        log.info("************************")
        self.assertEqual(1, 2, msg='相等吗')

    def test0402(self):
        print('test04_doing...')
        log.info("************************")
        self.assertEqual(1, 1, msg='相等吗')

    @unittest.skip("ff")
    def test0403(self):
        print('test04_doing...')
        log.info("************************")
        self.assertEqual(1, 1, msg='相等吗')

    def tearDown(self):
        print('test04_end...')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    runner = HTMLReport.TestRunner(title="功能测试+a")