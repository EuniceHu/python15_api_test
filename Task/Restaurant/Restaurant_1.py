#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Restaurant_1.py
  @time: 2019/03/10
  
  """

# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性：
# restaurant_name 和 cooking_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。




class Restaurant:
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type

    def describe_restaurant(self):
        print('餐馆的名字叫：{}，主要是做：{}'.format(self.restaurant_name,self.cooking_type))

    def open_restaurant(self):
        print('餐馆正在营业')

if __name__ == '__main__':
    t=Restaurant('井格','四川火锅')
    t.describe_restaurant()
    t.open_restaurant()