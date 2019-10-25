import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class login(unittest.TestCase):


    def setUp(self):
        #options = webdriver.ChromeOptions()
        #options.add_argument("disable-infobars")
        #self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test001(self):
        self.driver.get("https://www.baidu.com")
        self.assertEqual(self.driver.title, u"百度一下，你就知道")
        self.assertEqual(self.driver.current_url, "https://www.baidu.com/")
    def test002(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        WebDriverWait(self.driver, 10).until(EC.title_contains(u"selenium"))
        '''判断title，返回布尔值'''
        self.assertEqual(self.driver.title, u"selenium_百度搜索")

if __name__=="__main__":
    unittest.main(verbosity=2)



'''unittest.main(verbosity=2)
这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息 
并且 你在命令行里加入不同的参数可以起到一样的效果'''