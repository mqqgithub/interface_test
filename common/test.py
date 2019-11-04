# 导入logger模块
import logging
import os
import sys

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

