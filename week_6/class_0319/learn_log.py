# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 20:56
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_log.py

#日志：8 18 4万+时间+精神
#py5期 2年 7.5  14k+13新  妹纸

#日志：记录程序代码 操作  运维
#主要目的  我们要写一个我们自己的日志类
#logging python自带 来写日志模块
#log也有等级：debug --》info --》warning --》error--》critical/fatal
import logging
#日志：  收集 输出
#收集啥都收
# #输出的：有区别  只输出info级别以上（此处不包含info）
#收集-->日志收集器 root 默认
#输出-->输出渠道 1）控制台 console  2）指定文件 file 默认的是 console
#默认 输出只输出info级别以上（此处不包含info）

#新建日志收集器&输出渠道 &拼接 addHandler   my_logger-->handler 里面  取交集
#新建一个日志收集器：getLogger() 新建一个收集器
my_logger=logging.getLogger('py15')#名为py15的日志收集器
my_logger.setLevel('INFO')#设定收集的级别

#指定格式
fmt=logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息:%(message)s')

#新建指定的输出渠道：
#指定输出渠道 handler
ch=logging.StreamHandler()#指定输出到console控制台
ch.setLevel('ERROR')#设定输出信息的级别
ch.setFormatter(fmt)


##指定输出文本渠道 handler
file_handler=logging.FileHandler('py15.log',encoding='utf-8')
file_handler.setLevel('ERROR')#设定输出信息的级别
file_handler.setFormatter(fmt)

#配合关系
my_logger.addHandler(ch)
my_logger.addHandler(file_handler)

#收集日志
my_logger.debug('this is a debug msg')
my_logger.info('this is a info msg')
my_logger.warning('this is a warning msg')
my_logger.error('this is a error msg')
my_logger.critical('this is a critical msg1')
my_logger.critical('this is a critical msg2')


#写一个日志类
#结合配置文件 完成 输出的格式  输出的级别的配置

