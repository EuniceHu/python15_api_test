#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: if.py
  @time: 2019/02/18
  
  """
#算术运算符  + - * / %取余运算
# print(1+2)
# print(1*2)
# 取数运算干啥？？？判断一个数是奇数还是偶数
# 用过+ 字符串的拼接  列表的合并

# 赋值运算符 =  += -=
# a=1 #1存在内存里面 a相当于1的引用
# a=3
# a+=4#a=a+4
# print(a)

# 比较运算符  ==  >  >=  <   <=  !=
#运算结果是：布尔值  True  False
# print(3==4)
# print(3<4)

# print('get'=='GET')  字母是区分大小写
# print('get'.upper()=='GET')


# 逻辑运算符   and or not  优先级 not>and>or
#运算结果是：布尔值  True  False
#


# print(a>0 and b>0)# 且 与 必须是左右两边同时满足才为真
# print(a>0 or b>0)# 或 左右两边只有一边满足即可
# print(a>0 and b>0 and c>0)
# print(a>0 and b>0 or c>0)

# 成员运算符  in not in
#运算结果是：布尔值  True  False
# s='hello'
# print('h'in s)

# t=[1,'hello',666,9.09]
# print('h'in t[1])

#
# d={'name':'hhh','age':23}  #根据key来判断
# print('age' in d)

# 练习：从控制台获取一个成绩 根据成绩判断
# 如果> 80 优秀 > 70良好 >= 60及格 <60不及格
# 数据范围是0~100
score=input("请输入你的成绩：")#利用input从控制台输出的数据都是字符串类型
if score.isdigit():
    score=int(score)
    if score>100 and score<0:
        print('数据范围在0-100之间')
    elif score>80:
        print('优秀')
    elif score>70:
        print('良好')
    elif score>=60:
        print("及格")
    else:
        print("不及格")
else:
    print('数据输入有误')



number=23
guess=int(input("请输入一个整数"))
if guess==number:
    print("恭喜你猜对啦！")