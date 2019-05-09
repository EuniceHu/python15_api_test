#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: dict.py
  @time: 2019/02/16
  
  """
#字典 dict--dictionary{}
# 1:空字典 d={}
# print(type(d))
# 2:字典 key value 键值对 不同的键值对之间用逗号隔开
#key  不可变 唯一 int str tuple float   不能重复的
# 一般都是用字符串
#value 可以是任意类型 数据类型不限 整数  浮点数  字符串 布尔值 True/1 False/0 元祖 列表 字典
#key:value键值对 用逗号区分开来的

#3：字典取值：字典名[key]
#根据Key取值

# d={
#    'name':'好好',
#    'hobby':'学python',
#    'age':18,
#    'score':{'en':123,'math':87,'ch':'A'},
#    'friend':['hhh','ruyi'],
#    'good_man':True,
#    2:'hello',
#    0.002:'python',
#    True:'aaa',
#    (1,2,3):'hhh'
#    }
#
# print(d['score'])
#
# #4：嵌套取值  层级定位
#
# print(d['score']['math'])
# print(d['friend'][1])


# d={1:'我',
#    0.002:'爱',
#    True:'家',
#    'age':'22',
#    (1,2,3):'tuple'}
#5：字典也是可变无序数据类型
#
# d['name']='小啦啦啦'
# print(d)

d={
   "name":'哈哈',
   "salary":'9k',
   "friends":["小小","小王","小张"],
   'age':'22',
   (1,2,3):'tuple'
}
# 1.6.支持增删改
# 增加 d[key] key不存在字典里面 就是新增
# d["salary"]='30k'
# d['salary']='20k'
# print(d)

#
# 修改 d[key] key存在字典里面 就是修改
# d["name"]="kaka"
# print(d)
# d['name']='悠悠'
# print(d)

# 删除 根据key去删除
# d.pop('age')
# print(d)
# d.pop('friend')
# print(d)

#随机删除 ---了解即可
# d.popitem()
# print(d)
#
print(d.keys())
print(d.values())
# print(d.keys())#获取字典的所有key
# print(d.values())#获取字典的所有value

# 运算符


#d={
#    'name':'华华',
#    'hobby':'学Python',
#    'age':18,
#    'score':{'en':120,'math':99.99,'ch':'A'},
#    'friend':['bay max','小CC','如意'],
#    True:'good_man',
#    0.02:'python',
#    False:'这个value对应的key是布尔值',
#    (1,2,3):'我就是元组大大！！！',
#    0:'这是真爱呀',
#    1:'socre is 99.9'
#    }
#
# print(d)

# name='hhh'
# age='22'#int str float
# sex='女'#0 女生 1 男生 注解
# salary='9000'#int str float
# hobby='游泳'
# height='170.45'#浮点数




# d=input("请输入要一个日期：")
# # print(d)
# year=int(d[:4])
# month=int(d[4:6])
# day=int(d[6:])
# print('{}年{}月{}日'.format(year,month,day))








