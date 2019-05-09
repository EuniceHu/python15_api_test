#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: homework_0316.py
  @time: 2019/03/18
  
  """
from configparser import ConfigParser
# cf=ConfigParser()  实例化类


class Myconfig:
    '''实现配置文件的数据读取'''

    def __init__(self,conf_filepath,encoding='utf-8'):
        #打开配置文件
        self.cf=ConfigParser()
        self.cf.read(conf_filepath,encoding)
        #获取int类型的值
    def get_intValue(self,section,option):
        return self.cf.getint(section,option)
        # 获取float类型的值
    def get_floatValue(self,section,option):
        return self.cf.getfloat(section,option)

    # 获取bool类型的值
    def get_boolValue(self,section,option):
        return self.cf.getboolean(section,option)


    # 获取str类型的值
    def get_strValue(self,section,option):
        return self.cf.get(section,option)

    # 读取所有section列表
    def get_sections(self):
        return self.cf.sections()

    # 获取某一个section下面的，所有options
    def get_options(self,section):
        return self.cf.options(section)

if __name__ == '__main__':
    mf=Myconfig('demo.cfg')
    db_name=mf.get_strValue('db','db_name')
    db_port=mf.get_intValue('db','db_port')
    res=mf.get_boolValue('excel','res')
    salary=mf.get_floatValue('person_info','salary')
    print(db_name)
    print(db_port)
    print(res)
    print(salary)
    print(mf.get_sections())
    print(mf.get_options("db"))
