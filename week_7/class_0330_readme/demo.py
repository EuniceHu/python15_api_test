#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: demo.py
  @time: 2019/04/02
  
  """
# a=['3']
# b=a
# c=a[:]
#
# a.append(10)
# print(a)
# print(b)
# print(c)

import json

a={'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
b='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'


print(json.loads(b))
print(type(a))
print(type(b))
