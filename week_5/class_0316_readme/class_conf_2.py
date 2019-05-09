#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_conf_2.py
  @time: 2019/03/18
  
  """
#你这个类要提供什么功能？？？  我可以用你个类，去读取一个配置文件当中的数据。
#前提：打开配置文件
#读取想要的数据：sections??options??字符串？整数？布尔值？float值。
#要想定义一个类，要先要想好哪些参数是随时变化的，就比如这个配置文件夹
#首先要参数化文件名，然后再在每一个方法里面参数section  option
#因为文件名和文件里面的section option都是可变的，对于都是可变的，那么就要考虑参数化

#导入CondfigParser模块
from configparser import ConfigParser
# cp=ConfigParser()  实例化类
#定义一个类
class MyConfig:
    """这是一个打开配置文件的类"""

    def __init__(self,file_path,encoding='utf-8'):
        #初始化类，打开配置文件
        self.cp=ConfigParser()
        self.cp.read(file_path,encoding)

        #获取int类型的数据
    def get_intValue(self,section,option):
        return self.cp.getint(section,option)

       #获取str类型的数据
    def get_strValue(self,section,option):
        return self.cp.get(section,option)

       #获取bool类型的数据
    def get_boolValue(self,section,option):
        return self.cp.getboolean(section,option)

      #获取float类型的数据
    def get_floatValue(self,section,option):
        return self.cp.getfloat(section,option)

     #获取所有的section
    def get_sections(self):
         return self.cp.sections()

    #获取section 下面所有option
    def get_options(self,section):
        return self.cp.options(section)


if __name__ == '__main__':
    t=MyConfig('db.cfg')
    port=t.get_intValue('mysql_db_test','port')#section是配置文件里面的section名字，不是文件名
    db=t.get_strValue("mysql_db_test","db")
    excel=t.get_boolValue("mysql_db_test","excel")
    salary=t.get_floatValue("mysql_db_test","salary")
    sections=t.get_sections()
    options=t.get_options("mysql_db_test")
    print(port)
    print(db)
    print(excel)
    print(salary)
    print(sections)
    print(options)





