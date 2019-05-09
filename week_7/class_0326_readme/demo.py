#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: demo.py
  @time: 2019/03/26
  
  """
# import json
# a='登录成功'
# b=json.loads(a)
# print(type(b))


def add(a,mylist=[]):
    if not mylist:
        mylist=[]
    mylist.append(a)
    return mylist
print(add.__defaults__)
print(add(4))
print(add.__defaults__)
print(add(5))
print(add.__defaults__)
print(add(6,['a']))#mylist=['a']
print(add.__defaults__)
print(add(7))