#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/16 9:43

from configparser import ConfigParser

#实例化类
cf = ConfigParser()

#1\读取conf文件:文件路径 、编码方式
#相对路径
#绝对路径
cf.read("demo.cfg",encoding="utf-8")

#2、读取所有section   列表
secs = cf.sections()
print(secs)

#3\获取某一个section下面的，所有options
print(cf.options(secs[0]))
#cf.options("db")

#4\获取某一个section下面，某一个option具体的值
#所有结果都是字符串。
print(cf.get("db","db_user"))

#获取int类型的值。cf.getInt
old = cf.get("db","db_port")
print(type(old))
port = cf.getint("db","db_port")
print(type(port))

#获取布尔值类型的数据
res = cf.getboolean("excel","res")
print(type(res))

#获取float类型的数据
pp = cf.getfloat("db","db_port")
print(type(pp))


sex = cf.get("person_info","sex")
print(sex)

print(eval(sex))


