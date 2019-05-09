#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_dict.py
  @time: 2019/02/15
  
  """
#字典 关键字 dict dictionary 符号{}
#1：特征
#1.1.大括号括起来的数据，都是字典
#1.2.空字典 d={}
#1.3.字典里面元素存储的方式key:value的形式  键值对
#key  不可变 唯一 int str tuple float
#value 数据类型不限 整数  浮点数  字符串 布尔值 True/1 False/0 元祖 列表 字典
#key:value键值对 用逗号区分开来的
#1.4 元素与元素之间是用逗号隔开的，看元素的长度 len
#1.5 取值方式：无序的数据
#根据Key取值  字典名[key]

d={
    'name':'好好','hobby':'学python','age':18,
   'score':{'en':123,'math':87,'ch':'A'},
   'friend':['hhh','ruyi'],
   'good_man':True,
   2:'hello',
   0.002:'python',
   True:'aaa',
   (1,2,3):'hhh'
   }

print(d['friend'])
#字典嵌套取值
print(d['score']['en'])#只能key取值
print(d['friend'][0])
print(len(d))

#1.6.支持增删改
#增加 d[key] key不存在字典里面 就是新增
d['salary']='20k'
print(d)

#修改 d[key] key存在字典里面 就是修改
d['name']='悠悠'
print(d)

#删除 根据key去删除
# d.pop('friend')
# print(d)

#随机删除 ---了解即可
# d.popitem()
# print(d)

print(d.keys())#获取字典的所有key
print(d.values())#获取字典的所有value

#下次上课重点：
#if  else 循环语句

