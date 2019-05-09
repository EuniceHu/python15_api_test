# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-03-29 11:29
import configparser

class ConfigProcess(object):

    def __init__(self,filename,encoding = 'utf-8'):
        self.conf =configparser.ConfigParser()
        self.conf.read(filename,encoding=encoding)



    def getStr_value(self,section,option):
        '''获取 字符串 类型的参数值'''
        return self.conf.get(section,option)


    def getInt_value(self,section,option):
        '''获取 数字 类型的参数值'''
        return self.conf.getint(section,option)


    def getFloat_value(self,section,option):
        '''获取 浮点 类型的参数值'''
        return self.conf.getfloat(section,option)


    def getBoolean_value(self,section,option):
        '''获取 布尔值 类型的参数值'''
        return self.conf.getboolean(section,option)


    def getTuple_value(self,section,option):
        '''获取 元组tuple 类型的参数值'''
        return eval(self.conf.get(section,option))


    def getList_value(self,section,option):
        '''获取  列表list 类型的参数值'''
        return eval(self.conf.get(section,option))


    def getDict_value(self,section,option):
        '''获取 字典dict 类型的参数值'''
        return eval(self.conf.get(section,option))


    def getSet_value(self,section,option):
        '''获取 集合set 类型的参数值'''
        return eval(self.conf.get(section,option))


    def getSections(self):
        '''获取当前配置文件所 section 并以list形式返回'''
        return self.conf.sections()

    def getOptions(self,section):
        '''获取当前 section 下的所有opstion 并以list形式返回'''
        return self.conf.options(section)

    def get_option_itmes(self,section):
        '''获取当前 section 下所有opstion的所有键=值（以元组）信息 并以list形式返回'''
        return self.conf.items(section)



if __name__ == '__main__':
    conf = ConfigProcess('./conf/config.cfg')
    print(conf.getSections())
    print(conf.getOptions('oracle_db'))
    print(conf.get_option_itmes('oracle_db'))

    print(conf.getStr_value('jdbc_mysql','host'))