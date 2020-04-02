#coding=utf-8
import unittest, time, os, multiprocessing
import common.HTMLTestRunner as HTMLTestRunner
#查找多有含有 thread 的文件，文件夹
def EEEcreatsuit():
    casedir=[]
    listaa=os.listdir('/interface_test')
    for xx in listaa:
        if "testCase" in xx:
            casedir.append(xx)
    suite=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(n,pattern ='test*.py',top_level_dir=n)
        print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            suite.append(testunit)
    print("===casedir:====",casedir)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("!!!suite:!!!",suite)
    return suite,casedir
#多线程运行测试套件，将结果写入 HTMLTestRunner 报告
def EEEEEmultiRunCase(suite,casedir):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = '/interface_test/report/'+now+'result.html'
    fp = open(filename, 'wb')
    proclist=[]
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
        proc = multiprocessing.Process(target=runner.run(i),args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    fp.close()


if __name__ == "__main__":
    runtmp=EEEcreatsuit()
    EEEEEmultiRunCase(runtmp[0],runtmp[1])