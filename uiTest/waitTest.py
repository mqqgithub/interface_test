'''在UI自动化测试中，必然会遇到环境不稳定，网络慢的情况，这时如果不做任何处理的话，代码会由于没有找到元素而报错。这时我们就要用到wait，而在Selenium中，我们可以用到一共三种等待，每一种等待都有自己的优点或缺点，如果选择最优的等待方式。
time（固定等待）
在开发自动化框架过程中，最忌讳使用python自带模块的time的sleep方式进行等待，虽然可以自定义等待时间，但当网络条件良好时，依旧按照预设定的时间继续等待，导致整个项目的自动化时间无限延长。不建议使用。（注：脚本调试过程时，还是可以使用的，方便快捷）
implicitly_wait（隐式等待）

隐式等待实际是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间结束，然后执行下一步。这样的隐式等待会有个坑，我们都知道js一般都是放在我们的body的最后进行加载，实际这是页面上的元素都已经加载完毕，我们却还在等待全部页面加载结束。隐式等待对整个driver周期都起作用，在最开始设置一次就可以了。不要当作固定等待使用，到哪都来一下隐式等待。

WebDriverWait（显示等待）

WebDriverWait是selenium提供得到显示等待模块引入路径

from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait参数

driver: 传入WebDriver实例，即我们上例中的driver
timeout: 超时时间，等待的最长时间
poll_frequency: 调用until或until_not中的方法的间隔时间，默认是0
.5
秒
ignored_exceptions: 忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，
则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有NoSuchElementException。
这个模块中，一共只有两种方法until与until_not

method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
message: 如果超时，抛出TimeoutException，将message传入异常
until

当某元素出现或什么条件成立则继续执行

until_not

当某元素消失或什么条件不成立则继续执行

两个方法的method，必须是含有__call__的可执行方法。所以我们引用selenium提供的一个模块
'''
from selenium.webdriver.support import expected_conditions as Ec


'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
locator = (By.ID, 'kw')
driver.get(base_url)

WebDriverWait(driver, 10).until(EC.title_is(u"百度一下，你就知道"))
'''判断title,返回布尔值'''

WebDriverWait(driver, 10).until(EC.title_contains(u"百度一下"))
'''判断title，返回布尔值'''

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))
'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'su')))
'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.ID, value='kw')))
'''判断元素是否可见，如果可见就返回这个元素'''

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mnav')))
'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.mnav')))
'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='u1']/a[8]"), u'设置'))
'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#su'), u'百度一下'))
'''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
# 注意这里并没有一个frame可以切换进去

WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#swfEveryCookieWrap')))
'''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
# 注意#swfEveryCookieWrap在此页面中是一个隐藏的元素

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='u1']/a[8]"))).click()
'''判断某个元素中是否可见并且是enable的，代表可点击'''
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()

# WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
'''等待某个元素从dom树中移除'''
# 这里没有找到合适的例子

WebDriverWait(driver, 10).until(EC.element_to_be_selected(driver.find_element(By.XPATH, "//*[@id='nr']/option[1]")))
'''判断某个元素是否被选中了,一般用在下拉列表'''

WebDriverWait(driver, 10).until(
    EC.element_selection_state_to_be(driver.find_element(By.XPATH, "//*[@id='nr']/option[1]"), True))
'''判断某个元素的选中状态是否符合预期'''

WebDriverWait(driver, 10).until(EC.element_located_selection_state_to_be((By.XPATH, "//*[@id='nr']/option[1]"), True))
'''判断某个元素的选中状态是否符合预期'''
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()

instance = WebDriverWait(driver, 10).until(EC.alert_is_present())
'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
print
instance.text
instance.accept()

复制代码
复制代码
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://ui.imdsx.cn/uitester/")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

driver.maximize_window()  # 将窗口放大
driver.execute_script('window.scrollTo(0,0);')
e = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(('id', 'i1')))  # 等什么出现则继续执行
e.send_keys(1111)
复制代码
from selenium.webdriver.common.by import By

e = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.ID, 'i1')))
WebDriverWait(driver, 10, 1)
10: 超长时间。1：步长，代表每1秒查询一次
WebDriverWait(driver, 10).until_not()
等什么消失继续执行
复制代码
UI自动化的弊端
1.
维护成本大（产量不高）
a.代码没做任何的解耦
b.没有框架的思想，纯粹在堆代码（pageobject）
根据项目的每个页面，抽象出类，每个功能点抽象出这个类的函数
c.web开发会变更html接口，或进行修改
css_selector的定位方式，尽量减轻层级定位的使用次数
2.
代码爱报错
WebDriverWait每隔几秒钟扫描一次，如果超时了，则报timeout的错误
css_selector的定位方式，尽量减轻层级定位的使用次数
复制代码