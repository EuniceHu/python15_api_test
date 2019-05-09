#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/16 10:11

#你这个类要提供什么功能？？？  我可以用你个类，去读取一个配置文件当中的数据。
#前提：打开配置文件
#读取想要的数据：sections??options??字符串？整数？布尔值？float值。
from configparser import ConfigParser
#cf = ConfigParser()


class myConfig:

    def __init__(self,conf_filePath,encoding="utf-8"):
        #打开配置文件
        self.cf = ConfigParser()
        self.cf.read(conf_filePath,encoding)

    #获取整数
    def get_intValue(self,section,option):
        return self.cf.getint(section,option)

    def get_boolValue(self,section,option):
        return self.cf.getboolean(section,option)

    def get_strValue(self,section,option):
        return self.cf.get(section,option)

    def get_floatValue(self,section,option):
        return self.cf.getfloat(section,option)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self,section):
        return self.cf.options(section)

mf = myConfig("demo.cfg")
db_name = mf.get_strValue("db","db_name")
print(db_name)

db_port = mf.get_intValue("db","db_port")
print(db_port)

print(mf.get_sections())
print(mf.get_options("db"))


#总结
#1、为什么要用配置文件？接口自动化 - 配置数据库参数/配置用例的运行模式/服务器地址
#2、配置文件的表达。文件格式：.cfg/.conf
    #编写格式：section\option\value   section - 区域/块 格式：[section名字]
    #在section之下：option=value
    #可以有多个section.换行区分。
#3、读取配置数据。用的模块：configparser的ConfigParser类。
    #1）实例化ConfigParser类  cf = ConfigParser()
    #2）加载配置文件：cf.read(文件名称,编码方式)
    #3）获取配置数据：获取sections:cf.sections()
                      #获取options:cf.options()
                      #获取value: str/int/bool/float
                                   #get(section,option)
                                   #getint(section,option)
                                   #getboolean(section,option)
                                   #getfloat(section,option)

#4、写一个自己的类。实现配置文件数据读取的功能。
    # 能够利用你自己的类，来进行配置文件操作。
    #1、我实现了什么功能？打开一个配置文件，然后读取各种数据。
    #2、我是怎么实现的？利用ConfigParser类提供的功能，来实现自己的各种功能、封装。
    #初始化 --- 整个类当中，公用的属性赋值。
    #各种功能：先把功能函数列出来。再去填充内容。



