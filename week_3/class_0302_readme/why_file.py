#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: why_file.py
  @time: 2019/03/04
  
  """
def add(a,b):
    print(a+b)


# file=open('python16.txt','r')
# # resp=file.readline()#读取一行内容，返回字符串形式的数据
# resp=file.readlines()#读取所有行，以列表的形式返回
# # 每一行数据是列表一个字符串元素
# print(resp)
#
#
# for item in resp:
#     item=item.strip("\n")#对字符串特殊符号给剔除掉
#     data=item.split(',')
#     print(data)
#     add(int(data[0]),int(data[1]))


import requests


file=open('python17.txt','w',encoding="UTF-8")
resp=requests.get('http://www.baidu.com')
file.write(resp.text)


#1:存储测试数据
#2：可以写入我们结果
#3：写日志 logging

