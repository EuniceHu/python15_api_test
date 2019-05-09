#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: do_mysql.py
  @time: 2019/04/22
  
  """
import pymysql
import configparser
from week_9.class_0419.common import contants
class DoMysql:
    """
    完成与Mysql数据库的一个交互
    """

    #实例化的过程就是建立连接的过程，直接写到初始化里面，建立连接的时候，去fetch_one

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.db_file)
        host = self.config.get("mysql_db_test", "host")
        user = self.config.get("mysql_db_test", "user")
        password = self.config.get("mysql_db_test", "password")
        port = self.config.getint("mysql_db_test", "port")
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        self.cursor=self.mysql.cursor()

        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        # port = 3306
        #创建连接
        # self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        # self.cursor=self.mysql.cursor()



    def fetch_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()


    def fetch_all(self,sql):
       self.cursor.execute(sql)
       return self.cursor.fetchall()

    def close(self):
        self.cursor.close()#关闭游标，关闭查询接口
        self.mysql.close()#关闭连接


if __name__ == '__main__':
    mysql = DoMysql()
    result=mysql.fetch_one('select mobilephone from future.member where mobilephone = "13037680161";')
    print(result)
    mysql.close()
