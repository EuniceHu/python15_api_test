# encoding=utf_8
# @Author  ： 豆子
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from douzi_0323.commons import filepath
from douzi_0323.commons.configsparse import ConfigsParse


class LogParse(object):
    def __init__(self):
        cp = ConfigsParse()
        # 定义一个日志收集器
        self.logger = logging.getLogger('logs')
        # 设置收集器的输出级别
        self.logger.setLevel(cp.get('root', 'level'))
        famatter = logging.Formatter(cp.get('famatter', 'famatter'))

        ch = logging.StreamHandler()
        ch.setLevel(cp.get('stream', 'level'))
        ch.setFormatter(famatter)

        log_dir = os.path.join(filepath.log_dir, cp.get('file', 'file'))
        fh = TimedRotatingFileHandler(filename=log_dir, encoding='utf-8', when='M', backupCount=3)
        fh.setLevel(cp.get('file', 'level'))
        fh.setFormatter(famatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def clear_handler(self):
        self.logger.handlers.clear()

    def debug(self, msg):
        self.logger.debug(msg)
        self.clear_handler()

    def info(self, msg):
        self.logger.info(msg)
        self.clear_handler()

    def error(self, msg):
        self.logger.error(msg, exc_info=True)
        self.clear_handler()

    def warning(self, msg):
        self.logger.warning(msg)
        self.clear_handler()


if __name__ == '__main__':
    LogParse().error('123')
