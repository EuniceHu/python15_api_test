#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: def.py
  @time: 2019/02/21
  
  """
#函数的定义：为了实现某个功能而写的代码段
#如果这个功能是需要重复使用的，提高代码复用性
#函数的语法：
# def 函数名(参数1，参数2，参数3)：小写字母  不同的字母之间用下划线隔开
     #'''解释文档'''
     #函数体
     #return

#参数：位置参数  默认参数  动态参数 *args  关键字参数**kwargs
# 参数个数：0到无数个
# 函数体  具体要实现什么功能
# return 是否有返回值

# def say_hello():
#     print('早上好！！！')
#     return [1,2,3],{'name':777},'hero'
# #当调用函数的时候 return会返回return后面的值
# res=say_hello()#函数的调用  函数名()
# print('函数返回的值是：',res)
# 请对say_hello()这个函数的结果，进行遍历
# for i in res:
#     print(i)


# def say_hello():
#     print("hello")
#     return None
# res=say_hello()
# print("函数返回的值是：",type(res))


# def say_hello():
#     print('早上好！！！')
#     return [1,2,3],{'name':777},'hero'
# x,y,z=say_hello()  x,y,z分别赋值  挨个接收函数的值
# print(x)
# print(y)
# print(z)


# 一：
# 1：函数里面没有return 它会隐形给添加一个return
# 2:函数里面有return 但是return后面啥都没有 等同于return None
# 3:函数里面有return return后面加的是None 最终结果还是返回None

# 二：
# 1：return后面只有一个值的时候，是什么类型就会返回什么类型的数据
# 比如return后面是整数  那么返回的数据是整数
#如果是字符串，那么返回的就是字符串


# 三：如果return后面有多个值的时候，是以元祖的类型返回
# 四：return表示函数的结束  return后面的代码都不会执行
