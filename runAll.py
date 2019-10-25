import os
import common.HTMLTestRunner as HTMLTestRunner
from common import getpathInfo
import unittest

#from common.configEmail import send_email
#from apscheduler.schedulers.blocking import BlockingScheduler
#import pythoncom
import common.log

#send_mail = send_email()   #创建一个发邮件的对象
path = getpathInfo.get_Path()  #获取当前的文件路径
report_path = os.path.join(path, 'result')  #测试结果文件夹路径
#on_off = readConfig.ReadConfig().get_email('on_off')    #是否发送email
log = common.log.logger   #日志

class AllTest:#定义一个类AllTest
    def __init__(self):#初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, "report.html")#result/report.html文件路径
        self.caseListFile = os.path.join(path, "caselist.txt")#配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")#真正的测试断言文件路径
        self.caseList = []  #要执行的case放到一个list中
        log.info('resultPath:  '+resultPath)#将resultPath的值输入到日志，方便定位查看问题
        log.info('caseListFile:  '+self.caseListFile)#同理
        log.info('caseList:  '+str(self.caseList))#同理

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)  #打开要执行的case文件
        for value in fb.readlines():  #循环读取每一行的值
            data = str(value)         #值转换为字符串
            if data != '' and not data.startswith("#"):# 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))#读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close() #关闭文件

    def set_case_suite(self):
        """
        :return:
        """
        self.set_case_list() #通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()  #https://blog.csdn.net/fengguangke/article/details/81709215
        suite_module = []
        for case in self.caseList: #从caselist元素组中循环取出case
            case_name = case.split("/")[-1] #通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name+".py") #打印出取出来的名称，要执行的用例的名字
            #批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover) #将discover存入suite_module元素组
            print('suite_module:'+str(suite_module))
        if len(suite_module) > 0: #判断suite_module元素组是否存在元素
            for suite in suite_module: #如果存在，循环取出元素组内容，命名为suite
                for test_name in suite: #从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        print("******print test_suite******")
        print(test_suite)
        return test_suite#返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()#调用set_case_suite获取test_suite
            print('try')
            print(str(suit))
            if suit is not None:#判断test_suite是否为空
                print('if-suit')
                fp = open(resultPath, 'wb')#打开result/20181108/report.html测试报告文件，如果不存在就创建
                #调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            #log.info(str(ex))

        finally:
            print("*********TEST END*********")
            #log.info("*********TEST END*********")
            fp.close()
        #判断邮件发送的开关
        #if on_off == 'on':
        #    send_mail.outlook()
        #else:
        #    print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()

if __name__ == '__main__':
    #AllTest().run()
    tests = AllTest()
    tests.run()


