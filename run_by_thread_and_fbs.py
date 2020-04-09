from threading import Thread
from selenium import webdriver
from time import sleep, ctime


def test_baidu(host, browser):
    """测试用例"""
    print('start:%s' % ctime())
    print(host, browser)
    dc = {'browserName': browser}
    driver = webdriver.Remote(command_executor=host, desired_capabilities=dc)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.close()


if __name__ == '__main__':
    lists = {'http://192.168.170.78:4444/wd/hub': 'chrome',
             'http://192.168.170.78:5555/wd/hub': 'chrome',
             'http://192.168.170.78:6666/wd/hub': 'chrome'
             }
    threads = []
    files = range(len(lists))

    # 创建线程
    for host, browser in lists.items():
        t = Thread(target=test_baidu, args=(host, browser))
        threads.append(t)

    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:%s' % ctime())
