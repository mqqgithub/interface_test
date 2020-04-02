# https://www.cnblogs.com/kaibindirver/p/7492963.html
import os
import time
import unittest
import common.HTMLTestRunner as HTMLTestRunner
from common import getpathInfo
from common.log import Log
from common.config_email import Email
import multiprocessing

# from apscheduler.schedulers.blocking import BlockingScheduler
# import pythoncom


# 创建一个发邮件的对象
# send_mail = send_email()

# 获取当前的文件路径
path = getpathInfo.get_base_path()
print(path)
# 测试结果文件夹路径
report_path = os.path.join(path, 'result')

# 是否发送email
# on_off = readConfig.ReadConfig().get_email('on_off')
log = Log()


class AllTest:

    def __init__(self):

        # 初始化一些参数和数据
        global REPORTER_PATH

        # result/report.html文件路径
        report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
        REPORTER_PATH = report_path + "\\" + report_time + "report.html"
        # 配置执行哪些测试文件的配置文件路径
        self.caseListFile = os.path.join(path, "caselist.txt")

        # 真正的测试断言文件路径
        self.caseFile = os.path.join(path, "testCase")
        # 要执行的case放到一个list中
        self.caseList = []
        # 将resultPath的值输入到日志，方便定位查看问题
        log.info('resultPath:  '+REPORTER_PATH)
        log.info('caseListFile:  '+self.caseListFile)
        log.info('caseList:  '+str(self.caseList))

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        # 打开要执行的case文件
        fb = open(self.caseListFile)
        # 循环读取每一行的值
        for value in fb.readlines():
            # 值转换为字符串
            data = str(value)
            # 如果data非空且不以#开头
            if data != '' and not data.startswith("#"):
                # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        # 通过set_case_list()拿到caselist元素组
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        # 从caselist元素组中循环取出case
        for case in self.caseList:
            # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            case_name = case.split("/")[-1]
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            # 将discover存入suite_module元素组
            suite_module.append(discover)

        # 判断suite_module元素组是否存在元素
        if len(suite_module) > 0:
            # 如果存在，循环取出元素组内容，命名为suite
            for suite in suite_module:
                # 从discover中取出test_name，使用addTest添加到测试集
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        print("******print test_suite******")
        return test_suite

    def run(self, suite):
        try:

            # 调用set_case_suite获取test_suite
            suit = self.set_case_suite()
            # 判断test_suite是否为空
            if suit is not None:
                # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                fp = open(REPORTER_PATH, 'wb')
                proclist = []
                # 调用HTMLTestRunner
                for i in suit:
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                    proc = multiprocessing.Process(target=runner.run, args=(i,))
                    proclist.append(proc)
                print('线程数量=%d' % len(proclist))
                for pro in proclist:
                    pro.start()
                for pro in proclist:
                    pro.join()
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            log.info(str(ex))

        finally:
            print("*********TEST END*********")
            log.info("*********TEST END*********")
            fp.close()

        log.info("发送邮件开始")
        Email.send_email(REPORTER_PATH)
        log.info("发送邮件成功")
# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()


if __name__ == '__main__':
    start_time = time.time()
    suit = AllTest().set_case_suite()
    AllTest().run(suit)
    end_time = time.time()
    log.info('总时长=%.4f' % (end_time - start_time))
    # tests = AllTest()
    # tests.run()
'''
1、生成的测试报告有问题
2、时间没有减少太多
'''

