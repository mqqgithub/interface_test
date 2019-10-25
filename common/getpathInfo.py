'''
返回当前文件的路径
'''

import os

# 返回当前目录
def get_current_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path
# 返回根目录
def get_base_path():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return BASE_DIR

if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('返回当前目录,路径为：', get_current_path())
    print('返回根目录，路径为：', get_base_path())
'''
os.path.realpath(__file__)
1、返回值是当执行文件的绝对路径，包括文件名,加上[0]获取文件夹路径，去掉文件名
2、可以用os.getcwd()获取当前路径文件夹

os.path.split('PATH')
1.PATH指一个文件的全路径作为参数：
2.如果给出的是一个目录和文件名，则输出路径和文件名
3.如果给出的是一个目录名，则输出路径和为空文件名

report_path = os.path.join(path, 'result', 'report.html')
1、路径下一层文件夹

返回上层目录
ar_path = os.path.dirname(os.getcwd())

'''