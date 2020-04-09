# 主机启动java -jar selenium-server-standalone-2.45.0.jar -role hub
# 分布式测试机启动 java -jar selenium-server-standalone-2.45.0.jar -role node -port 5555
# 分布式测试机启动 java -jar selenium-server-standalone-2.45.0.jar -role node -port 6666


from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://127.0.0.1:5555/wd/hub': 'chrome',
         'http://127.0.0.1:6666/wd/hub': 'chrome'}
# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY', 'browserName': browser,
                                          'version': '', 'javascriptEnabled': True})
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()
    driver.quit()


