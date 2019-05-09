# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_异常处理.py

#1：什么是异常？
#2：为什么要处理异常？
#3：怎么处理？

# print(a)#NameError: name 'a' is not defined

# s=[1,2,3]
# print(s[4])#IndexError: list index out of range

# d={'name':'summer','hobby':'it'}
# print(d['sex'])#KeyError: 'sex'
# print(d['name'])

# NameError: name 'a' is not defined
# IndexError: list index out of range
# KeyError: 'sex'

#try...except...  最简单的异常处理
#try...except 具体的error类型  as e:# 能够处理指定错误类型的异常
# try:#丢丢
#     s=[1,2,3]
#     print(s[4])
#     print(a)
# except (IndexError,NameError) as e:
#     print('我要行使班主任的权利把你关起来')
#     print('saber一脸蒙蔽，我犯啥事了！')
#     print('丢丢说，你犯错误了，错误是：{}'.format(e))

#BaseException  Exception---》从这里开始掌握
# try:#丢丢
#     # print(a)
#     s=[1,2,3]
#     print(s[4])
# except BaseException as e:
#     print('我要行使班主任的权利把你关起来')
#     print('saber一脸蒙蔽，我犯啥事了！')
#     print('丢丢说，你犯错误了，错误是：{}'.format(e))

#try...except....finally--->单元测试的 再给大家讲
# file=open('test.txt','w')
# try:
#     s=[1,2,3]
#     print(s[4])
# except Exception as e:
#     print('error is :{}'.format(e))
#     # file.write(str(e))
# finally:#不管try下面的代码是否报错  finally里面的代码都是会执行的！
#     print(e)

#try..except..else...
# try:
#     s=[1,2,3]
#     print(s[4])
# except Exception as e:
#     print('error is :{}'.format(e))
# else:#如果try 未出现任何异常 那么就会执行else里面的代码
#     print(s)
#     print(s)
#     print(s)
#     print(s)
#     print(s)
# print(s)
# print(s)
# print(s)
# print(s)
