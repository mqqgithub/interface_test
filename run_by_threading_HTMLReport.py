import HTMLReport
import unittest
import os, time


# 测试用例文件路径
test_dir = os.path.join(os.getcwd(), 'testCase')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
print('descover  ', discover)

# 测试报告文件路径
report_path = os.path.join(os.getcwd(), 'report')
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_time + "report.html"
# fp = open(report_name, 'wb')
# 调用HTMLTestRunner


def run():
    runner = HTMLReport.TestRunner(title="测试报告", description='测试deafult报告',
                                   output_path=report_path, report_file_name=report_name, thread_count=2)
    runner.run(discover)


if __name__ == '__main__':
    run()

