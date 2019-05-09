#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Exception_handling.py
  @time: 2019/03/06
  
  """
# 一：异常的处理
# print(a)  NameError: name 'a' is not defined


# s=[1,2,3]
# print(s[4])   IndexError: list index out of range


# d={'name':'summer','hobby':'IT'}
# print(d['sex']) KeyError: 'sex'
# print(d['name'])

#常见类型的异常
# NameError: name 'a' is not defined
# IndexError: list index out of range
# KeyError: 'sex'

# try...except...最简单的异常处理
# try...except  具体的error类型  as  e:能够处理指定错误类型的异常


# try:
#     s=[1,2,3]
#     print(s[4])
#     print(a)
# except (IndexError,NameError) as e:
#       print('我要行使班主任的权利把你关起来')
#       print('saber一脸蒙蔽，我犯啥事了！')
#       print('丢丢说，你犯错误了，错误是：{}'.format(e))



# BaseException  Exception--->基本异常的处理方式


# try:
#     print(a)
#     s=[1,2,3]
#     print(s[4])
#     # print(a)
# except Exception as e:
#       print('我要行使班主任的权利把你关起来')
#       print('saber一脸蒙蔽，我犯啥事了！')
#       print('丢丢说，你犯错误了，错误是：{}'.format(e))



# try...except...finally--->单元测试，经常用

# file=open('test.txt','w')
# try:
#     s=[1,2,3]
#     print(s[4])
# except Exception as e:
#     print('error is :{}'.format(e))
#     # file.write(str(e))
# # finally:#不管try下面的代码是否报错  finally里面的代码都是会执行的！
# print(e)



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


# 二：上下文管理器

# with open('py15.txt','w+',encoding='utf-8') as file:
#     file.write('哈哈哈啊时时彩')
# print(file)

# 三：debug调试

# def add(a,b):
#     c=a+b
#     print(c)
#
# add(1,5)


#打断点，debug调试