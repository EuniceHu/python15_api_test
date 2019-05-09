#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: args&kwargs.py
  @time: 2019/02/23
  
  """


# def add(*args):#函数的定义
#     print(args)#函数的调用



# def add(*args):#定义---表示可以传递任意多个参数
#     print('args的值：',args)
#     print('args的类型是：',type(args))
#
# add(1,2,3,4)
# add(*(1,2,3,4))
# t=[1,2,3,4,5]#args的值： ([1, 2, 3, 4, 5],)
# # 相当于传一个元素
# add(t)
# t=[1,2,3,4,5]#args的值： (1, 2, 3, 4, 5)
# add(*t)
# t=[[1,2],[3,4,5]]
# add(t)把t当成一个元素(整体)
# add(*t)#调用的时候--解包--脱外套(可以传多个参数进来)--脱一层  只能加一个* 只支持元祖和列表
# 把外套脱掉，里面有几个参数，就传几个参数


def add(*args):
    print('args的值是',args)
    print('args的类型是',type(args))

# add(1,2,3,4)
# add(*(1,2,3,4))
t=([1,2,3],[4,5])
add(t)
add(*t)







# def stu_info(**kwargs):
#     print(kwargs)
# d={'age':18,'name':'popo'}
# # stu_info(age=18,name='sad')
# stu_info(**d)
# stu_info(d)#这样会报错，需要加**
