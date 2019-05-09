#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: if.py
  @time: 2019/02/19
  
  """
# 1：非常简单的条件语句
# if 条件：if 后面的条件运算结果是布尔值  逻辑/比较/成员  各类数据类型
#    if代码   只有当if后面的条件成立的时候才会执行

# python 非零非空数据 都是True
#        零空数据 False
#
# s=[] 空数据代表False 不执行
# if  s:
#     print('我今年18岁！')

# 2：第二个条件语句
# if..else..
# age=55
# if age>=18:
#     print('成年')
#     if age>40:
#         print('中年人')
#     else:
#         print('青少年')
#
# else:
#     print('小学生')


# 3：多重判断语句：if..elif...elif...else
# if 必须要有的 else elif 可有可无  但是else一定是放在最后的
# # 但是如果一定有elif以及else的个数不限定
# 1:elif的个数不限定
# 2：分支顺序一定是if...elif...else

# score=int(input("请输入成绩："))
# if score>90:
#     print("great")
# elif score>80:
#     print("good")
# elif score>70:
#     print("well")
# elif score>60:
#     print("pass")
# else:
#     print("不及格")
