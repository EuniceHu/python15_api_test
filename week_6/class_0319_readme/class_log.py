#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_log.py
  @time: 2019/03/20
  
  """
# log也有等级 ：debug-->info-->warning-->error-->critical/fatal
import logging

#日志：收集  输出  收集是什么样的都手机

#输出：只输出info级别以上的，不包括info

# 收集-->日志收集器  root 默认

#输出--->有输出的渠道 1）控制台 console 2）指定的文件 file 默认是console
#默认 输出：只输出info级别以上的，不包括info

#新建一个日志收集器 -->输出渠道--> 拼接addHandler  My_logger--》Handler 取交集

#一：新建一个日志收集器：getLogger() 新建一个收集器

My_logger=logging.getLogger('py15')#名字为py15的日志收集器
My_logger.setLevel('INFO')#设定收集的级别

#二：指定输出的格式

fmt=logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息:%(message)s')


#三：新建指定的输出渠道  指定的输出渠道Handler
#第一种
ch=logging.StreamHandler()
ch.setLevel('INFO')#设定输出信息的级别
ch.setFormatter(fmt)

#第二种 指定输出文本渠道

file_logging=logging.FileHandler('py15.log',encoding='utf-8')
file_logging.setLevel('ERROR')
file_logging.setFormatter(fmt)

#四：配合两者之间的关系

My_logger.addHandler(ch)
My_logger.addHandler(file_logging)


#收集日志 打印输出

My_logger.debug('this is a debug msg')
My_logger.info('this is a info msg')
My_logger.warning('this is a warning msg')
My_logger.error('this is a error msg')
My_logger.critical('this is a critical msg1')


