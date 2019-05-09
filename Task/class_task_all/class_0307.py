#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_0307.py
  @time: 2019/03/08
  
  """

# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
#  其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


# class Restaurant:
#     def __init__(self):
#         self.restaurant_name="盛百味"
#         self.cooking_type="北京菜"
#
#     def describe_restaurant(self):#方法
#         return self.restaurant_name,self.cooking_type
#
#     def open_restaurant(self):#方法
#         print('餐馆正在营业')
#
# t=Restaurant()#一个对象
# print(t.restaurant_name)#对象调用属性
# print(t.cooking_type)
# t1=Restaurant().describe_restaurant()
# print('这家饭馆的名字叫：{}，主要是做：{}'.format(t1[0],t1[1]))
# Restaurant().open_restaurant()



# 2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，
# 还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user()的方法，它向用户发出个性化的问候

class User:
    #属性
    first_name='hhaha'
    last_name='juju'
    def describe_user(self):
        '''打印用户的信息摘要'''
        print('我的名字是{}{}'.format(self.first_name,self.last_name))
    def greet_user(self,name,content='早上好'):
        print('{},{}'.format(name,content))




if __name__ == '__main__':
    t=User()
    t.describe_user()
    t.greet_user('小新新')





# class User:
#     def __init__(self,first_name,last_name,age):
#        self.first_name=first_name
#        self.last_name=last_name
#        self.age=age
#        print(self.first_name)
#        print(self.last_name)
#        print(self.age)
#     def describe_user(self):
#         print('用户第一个名字是'+self.first_name)
#         print('用户最后一个名字是' + self.last_name)
#         print('用户的年龄为'+str(self.age))
#     def greet_user(self):
#         print("祝你节日快乐！")
#
# t=User('L','n','28')
# t.describe_user()
# t.greet_user()









# 3：思考问题：
#为什么会有对象方法 类方法 静态方法？我什么时候写什么类型的方法呢？
#什么时候用？
#写成不同的方法类型 有啥用呢？对我来说有啥用?
#他们有什么区别呢？ #自己总结一波。