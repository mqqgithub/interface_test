# https://blog.csdn.net/XnCSD/article/details/87977288
# https://www.cnblogs.com/deeper/p/7404190.html
# 导入logger模块
import logging
import os
import sys

# level 参数是一个过滤器，所有等级低于此设定的消息都会被忽略掉
# format 参数设置输出日志记录的格式，参数的具体格式设置参考 LogRecord attributes
# datefmt 设置输出时间的格式，参数格式接受 time.strftime() 的格式
# filename 指定输出的日志文件
# stream （控制台输出）使用一个特殊的流对象初始化 StreamHandler,注意：filename 和 stream 不能同时指定，否则会抛出 ValueError 异常
logging.basicConfig(filename='logs.log',
                    # stream=sys.stdout,
                    level=logging.DEBUG,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加日志记录级别
msg = '日志'
logging.critical('logging critical msg：%s', msg)
logging.error('logging error msg：%s', msg)
logging.warning('logging warning msg：%s', msg)
logging.info('logging info msg：%s', msg)
logging.debug('logging debug msg：%s', msg)

# error显示错误详细信息如下
'''
try:
    int('a')
except ValueError:
    logging.error('type error', exc_info=True)
'''

#############################################################################
# 可以通过 logging.getLogger(name=None) 创建一个指定名称的 Logger 对象（logging 系统默认的 logger 名称为 root)
# 与第一节中的区别仅在于 logger 的名称，其他设置的效果相同
logger = logging.getLogger('testLogger')
logger.setLevel(logging.DEBUG)
# 消息格式化
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

# 日志文件输出
fh = logging.FileHandler('example.log')
fh.setFormatter(formatter)
logger.addHandler(fh)   # 给logger对象添加 handler

# 系统输出
# StreamHandler
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
logger.addHandler(sh)

logger.critical('logger critical message.')
logger.error('logger error message')
logger.warning('logger warning message')
logger.info('logger info message')
logger.debug('logger debug message')

