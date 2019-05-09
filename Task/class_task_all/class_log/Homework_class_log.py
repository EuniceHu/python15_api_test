#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_class_log.py
  @time: 2019/03/20
  
  """
#写一个日志类

#结合配置文件 完成 输出的格式 输出的级别的配置

import logging
#导入读配置文件的类
from week_6.class_0319_readme.read_config import ReadConfig


class MyLog:
    """这是一个日志类"""

    def __init__(self,log_name,log_path):#level
        self.log_name=log_name
        self.log_path=log_path
        # self.level=level

    def my_log(self,msg,level):
        # 一：新建一个日志收集器：getLogger() 新建一个收集器
        logger=logging.getLogger(self.log_name)
        logger.setLevel(level)

        # 二：指定输出的格式
        fmt = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息:%(message)s')

        # 三：新建指定的输出渠道  指定的输出渠道Handler
        # 第一种
        ch = logging.StreamHandler()
        ch.setLevel(level)  # 设定输出信息的级别
        ch.setFormatter(fmt)

        # 第二种 指定输出文本渠道

        file_logging = logging.FileHandler(self.log_path, encoding='utf-8')
        file_logging.setLevel(level)
        file_logging.setFormatter(fmt)

        #四：对接

        logger.addHandler(ch)
        logger.addHandler(file_logging)

        if level=='DEBUG':
            logger.debug(msg)

        elif level=='INFO':
            logger.info(msg)

        elif level == 'WARNING':
            logger.warning(msg)

        elif level == 'ERROR':
            logger.error(msg)

        elif level == 'CRITICAL':
            logger.critical(msg)


        #移除，防止日志重复
        logger.removeHandler(ch)
        logger.removeHandler(file_logging)


    def debug(self,msg):
        self.my_log(msg,'Debug')#调用函数

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')



if __name__ == '__main__':
    mf = ReadConfig("demo.cfg")
    level = mf.get_strValue("LOG", "level")
    t=MyLog('py_0321','py_0321.log')
    t.info('ERROR日志')


