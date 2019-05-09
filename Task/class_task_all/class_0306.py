#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_0306.py
  @time: 2019/03/06
  
  """
#从字符串’abcdba‘中找出第一个不重复的字符，方法不限

s='abcdba'
# for i in s:
#     if len(s.split(i))==2:
#         print('第一个不重复的字符是：{}'.format(i))
#         break

res=len(s.split('a'))
print(res)

res=len(s.split('c'))
print(res)

res=s.index('c')
print(res)

for i in s:
    if s.index(i)==2:
        print('第一个不重复的字符是：{}'.format(i))
        break