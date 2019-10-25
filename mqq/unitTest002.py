
'''
 执行文件夹下面的所有test。。开始得的模块
'''

# coding:utf-8
import unittest
import os
import common.HTMLTestRunner as HTMLTestRunner

# python2.7要是报编码问题，就加这三行，python3不用加
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

# 用例路径
Path = os.getcwd()
case_path = os.path.join(os.path.dirname(Path), "testCase")
# 报告存放路径
report_path = os.path.join(os.path.dirname(Path), "result")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print("****************")
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用all_case函数返回值
    runner.run(all_case())
    # 关闭文件
    fp.close()
    print("over")