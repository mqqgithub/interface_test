# https://www.cnblogs.com/zhuque/p/8320750.html
import logging
import time
import common.getpathInfo as path
import os


class TestLog(object):

    def __init__(self, logger_name='logger'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        self.log_time = time.strftime('%Y_%M_%D_')
        self.log_path = os.path.join(path.get_base_path(), 'result',  + 'test_log.log')
        fh = logging.FileHandler(self.log_path, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fmt = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def get_log(self):
        return self.logger





