from selenium import webdriver
import unittest
from mqq.log import TestLog

log = TestLog().get_log()


class testcals(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.base = Screen(self.driver)  # 实例化自定义类commlib.baselib
        self.img = '这是一个图片'

    def login(self):
        url_login = "http://www.baidu.com"
        self.driver.get(url_login)

    def test_01_run_mail(self):
        try:
            self.login()
            log.info(self.img)
        except Exception as msg:
            log.error("异常原因 [ %s ]" % msg)
            log.error(self.img)
            raise

    def test_02_case(self):

        log.error("首页error 日志")
        log.debug("订单页debug 日志")
        log.info("活动页info 日志")
        log.critical("支付critical 日志")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()