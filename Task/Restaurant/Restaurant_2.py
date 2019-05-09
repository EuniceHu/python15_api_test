#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Restaurant_2.py
  @time: 2019/03/10
  
  """
# 2:写一个子类，继承1 这个父类，且添加函数：discount 打折扣用的
# pay_money 支付餐费用，重写 open_restaurant() ，并完成子类完成调用

from Task.Restaurant.Restaurant_1 import Restaurant
class Restaurant_1(Restaurant):

     @staticmethod
     def discount(a):
          a=a*0.8
          return a


     def pay_money(self):
          print('请支付费用')
     def open_restaurant(self):
          print('你好，请慢走，欢迎下次光临')

if __name__ == '__main__':
     t1=Restaurant_1('付小姐在成都','串串')
     t1.describe_restaurant()
     res=t1.discount(200)
     print('我们今天的菜品是打8折，折扣完的价钱为{}'.format(res))
     t1.pay_money()
     t1.open_restaurant()


