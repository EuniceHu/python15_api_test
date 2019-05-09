# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-03-31 17:32
import logging
import os
import time

from function.commons.base import Base
from function.commons.config_process import ConfigProcess


class Logger():

    def __init__(self,log_type='console'):
        config = ConfigProcess(Base.get_cur_dir(__file__)+'/../../conf/log.cfg')
        getLevel = config.getStr_value('logs','getLevel')
        # putLevel = config.getStr_value('logs', 'outLevel')
        fmt = config.getStr_value('logs','fmt')

        if log_type == 'console':
            logging.basicConfig(level=getLevel,format=fmt,datefmt='%Y-%m-%d %H:%M:%S')

        elif log_type == 'file':
            log_path = Base.get_cur_dir(__file__)+'/../../logs'
            if not os.path.exists(log_path):
                os.mkdir(log_path)

            now_time = time.strftime('%Y-%m-%d')
            file_name = R'{}/logback.{}.logs'.format(log_path,now_time)

            file_handler = logging.FileHandler(filename=file_name,encoding='utf-8',mode='a')
            logging.basicConfig(level=getLevel,format=fmt,
                                datefmt='%Y-%m-%d %H:%M:%S',handlers=[file_handler])


    def getLoger(self):
        logger = logging.getLogger()
        return  logger


if __name__ == '__main__':
    logger = Logger('file').getLoger()
    logger.info('我是info级别的BUG')
    logger.warning('我是WARNING级别的BUG')
    logger.error('我是ERROR级别的BUG')
    #
    # log_path = os.path.dirname(__file__)+'/../../logs/'
    # logs = open(log_path+'app2019-04-19.logs')
    # print(log_path+'app2019-04-19.logs')
    # print(logs.read())
    # logs.close()
    # os.mkdir(r'D:\python\futureloan_api\logs/log2')
    # print(log_path)