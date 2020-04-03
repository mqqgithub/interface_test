# coding=utf-8
import unittest, time, os, multiprocessing
import common.HTMLTestRunner as HTMLTestRunner
# 查找多有含有 thread 的文件，文件夹
def EEEcreatsuit():
    casedir=[]
    listaa=os.listdir('/interface_test')
    print(listaa)
    print('--------casedir---------')
    for xx in listaa:
        if "testCase" in xx:
            casedir.append(xx)

    suite=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(str(n),pattern ='test04*.py',top_level_dir=n)
        print(discover)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        suite.append(testunit)
    print("===casedir:====", casedir)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("!!!suite:!!!", suite)
    return suite
#多线程运行测试套件，将结果写入 HTMLTestRunner 报告
def htmlrun(filename,testut):
    fp = open(filename, 'ab+')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(testut)
    fp.close()
def EEEEEmultiRunCase(suite):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = '/interface_test/report/'+now+'result.html'
    #fp = open(filename, 'wb')
    proclist=[]
    s=0
    for i in suite:
        #runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
        proc = multiprocessing.Process(target=htmlrun,args=(filename, i,))
        proclist.append(proc)
        s=s+1
    for pr in proclist:
        pr.start()
    for pr in proclist:
        pr.join()
    #fp.close()


if __name__ == "__main__":
    runtmp=EEEcreatsuit()
    #print(runtmp)
    EEEEEmultiRunCase(runtmp)
