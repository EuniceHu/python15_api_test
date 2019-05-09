#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: parameter.py
  @time: 2019/02/23
  
  """
#参数：位置参数  默认参数  动态参数 *args  关键字参数**kwargs


# def add(x,y):#调用函数的时候传参   形参/位置参数
#     '''加法，求任何两个值的和，并返回计算结果'''
#     return x+y
# 位置参数
# res=add(9,6)#调用函数的时候传的参数--实参--默认按顺序赋值的
# res=add(y=9,x=6)#指定赋值  不关注顺序  指定什么就是什么
# print('之和是{}'.format(res))


# 默认参数  在定义函数的时候，给某个参数设置默认值
#位置参数必须在默认参数之前
# 有几个位置参数 就必须传几个参数

# def add(x,z,y=9):#调用函数的时候传参   形参/位置参数   y=9就相当于默认参数
#     '''加法，求任何两个值的和，并返回计算结果
#         ：arg x 第一个参数
#         ：arg x 第一个参数
#      '''
#       print('x的值是：',x)
#       print('x的值是：',x)
#       return x+y+z
#
# res=add(10,z=20)
# print('之和是{}'.format(res))
#

# 动态参数 *args  arguments  复数  指定多个---不定长参数
def add(*args):#参数传递到函数内部  会把所有的参数存储到一个元祖
    print('数据类型：',type(args))
    # print(args)
    sum=0#求和的初始值
    for i in args:
        sum+=i
    print('求和的值：',sum)
add(5,6,7,8,9)



# 关键字参数**kwargs  key word auguments
# 参数传递进去后变成一个字典 kwargs
# 必须要指明 key value
# def student_info(**kwargs):
#     print(kwargs)
# student_info(name='hh',age=28,money=100)
# student_info('caryon',22)----错误的示范