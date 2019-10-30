'''
发送http请求
'''
import requests
import json
from common.log import logger

logger = logger
class RunMain():

    def send_post(self, url, data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入,data是字典类型
        result = requests.post(url=url, data=data).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, data=data)
        # ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，
        # 只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示
        # sort_keys：将数据根据keys的值进行排序。
        # indent：应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，
        # 否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    # method是get、post，url接口地址，data接口参数
    def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result

if __name__ == '__main__':
    # 通过写死参数，来验证我们写的请求是否正确
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '111'})
    print(result)
