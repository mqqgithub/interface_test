import os
import configparser
from common import getpathInfo

# 调用实例化，还记得这个类返回的路径为C:\Users\songlihui\PycharmProjects\dkxinterfaceTest
path = getpathInfo.get_current_path()

# 这句话是在path路径下再加一级，最后变成C:\Users\songlihui\PycharmProjects\dkxinterfaceTest\config.ini
config_path = os.path.join(path, 'config.ini')

# 调用外部的读取配置文件的类创建config对象
config = configparser.ConfigParser()

# 调用父类的方法读取配置文件内容
config.read(config_path, encoding='utf-8')

class ReadConfig:

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))


