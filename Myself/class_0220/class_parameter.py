#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_parameter.py
  @time: 2019/02/20
  
  """
# def count_number(z=0,x=101,k=5):#形参
#     count=0
#     for i in range(z,x,k):#=1
#         count+=i#count=count+i
#     print('计算结果是：{}'.format(count))
#     return count#隐式的添加

# count_number(0,101,2)实参
# count_number(1,101,2)#实参为主
# count_number(z=0,x=101,k=2)



#1:函数的参数个数大于等于0个都行
# 2:为什么要加参数，还是要提高代码的复用性，
# 参数要通过函数的参数列表传递进来


# 参数的类型：位置参数  默认参数  动态参数 关键字参数
# 1：位置参数：是有顺序的  我们通过函数传参的时候 是按顺序赋值
#形参  实参
# 指定参数赋值  声明赋值  变量名要跟形参一致
# 调用参数的时候  有几个位置参数 就要传几个位置参数
# count_number(z=0,x=101,k=2)

#2：默认参数：我们给形参指定一个默认值
#有实参就用实参 没参数才用默认参数值
# 位置参数 应该在默认参数之前


# 3：动态参数  *args   不定长参数  想传几个 就传几个 参数之间用逗号隔开
# 可以传任意多个参数，不限制数据类型，参数之间用逗号隔开
# 参数到了函数内部 就变成了元祖
# args 默认写这个 一定要有星号

def robot_cat(*args):
    print(args)
    for item in args:
        print("我是哆啦A梦，比如有：{}".format(item))
# robot_cat("任意门",'暴富','变美','变瘦')

a=[['变美','变瘦'],['hh','jj']]
robot_cat(*a)
# 脱外套 只脱一层


# 3：关键字参数  **kwargs   key  value的形式  key word arguments
# 1:key value 的形式参数之间用逗号隔开
# 2：参数到了函数内部 就变成字典

# def anyway(**kwargs):
#     print(kwargs)
# anyway(a=1,b=2,c=3)