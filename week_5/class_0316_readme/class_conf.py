#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_conf.py
  @time: 2019/03/18
  
  """
from configparser import ConfigParser

#初始化类
cp=ConfigParser()
cp.read("db.cfg",encoding='utf-8')


#1:读取所有section列表
# res=cp.sections()
# print(res)


#2:读取某个section下面，所有option

# res1=cp.options(res[0])
# print(res1)
#
# res2=cp.options("mysql_db_test")
# print(res2)

#3：获取某一个section下面，某一个option具体的值

# res3=cp.get("mysql_db_test","port")
# print(res3)



#获取int类型的值 cp.getint
#
# old=cp.get("mysql_db_test","port")
# print(type(old))
#
# new=cp.getint("mysql_db_test","port")
# print(type(new))

#获取浮点类型的值

# res4=cp.getfloat("mysql_db_test","salary")
# print(res4)

#获取布尔值类型的值

# res5=cp.getboolean("mysql_db_test","excel")
# print(res5)
#
#
# sex=cp.get("mysql_db_test","sex")
# print(type(sex))
#
# print(type(eval(sex)))

#得到所有的section,以列表的形式返回

section=cp.sections()[0]
print(section)

#得到该section的所有option

option=cp.options(section)
print(option)

#得到section的所有键值对

items=cp.items(section)

print(items)
