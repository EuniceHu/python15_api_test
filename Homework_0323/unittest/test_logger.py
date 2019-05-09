import logging
from class_homework.unittest.test_config import Config
from class_homework.unittest import test_path

class Logger:

    def logger(self,level,msg):
        mylog=logging.getLogger('测试使用')
        mylog.setLevel('DEBUG')

        formatter=logging.Formatter(Config(test_path.config_path).rawconfig_get('LOGGER','formatter'))

        sh=logging.StreamHandler()
        sh.setLevel(Config(test_path.config_path).config_get('LOGGER','streamlevel'))
        sh.setFormatter(formatter)

        ch=logging.FileHandler('日志.txt',encoding='utf-8')
        ch.setLevel(Config(test_path.config_path).config_get('LOGGER','filelevel'))
        ch.setFormatter(formatter)

        mylog.addHandler(sh)
        mylog.addHandler(ch)


        if level=='DEBUG':
            mylog.debug(msg)

        elif level=='INFO':
            mylog.info(msg)

        elif level=='WARNING':
            mylog.warning(msg)

        elif level=='ERROR':
            mylog.error(msg)

        elif level=='CRITICAL':
            mylog.critical(msg)

        mylog.removeHandler(ch)
        mylog.removeHandler(sh)

    def debug(self,msg):
        self.logger('DEBUG',msg)

    def info(self,msg):
        self.logger('INFO',msg)

    def warning(self,msg):
        self.logger('WARNING',msg)

    def error(self,msg):
        self.logger('ERROR',msg)

    def critical(self,msg):
        self.logger('CRITICAL',msg)



if __name__ == '__main__':
    mylog=Logger()
    mylog.debug('嘤嘤嘤')

    mylog.info('测试用')

    mylog.error('出错了')