#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: operator.py
  @time: 2019/02/19
  
  """
#1:算术运算符  + - * / %取余运算  //取整数

# a=0.1
# b=0.3
# c=0.2
# print(round(a+b-c+a,1))#python是动态语言 精确度不定
# round(目标数字，精确的小数位数)  如果要精确浮点数运算值

# 判断奇数偶数  就会用到% x%2==0


#2:赋值运算符 =  += -=
# x=3
# x+=2#等同于 x=x+2
# x-=4#等同于 x=x-4
# print(x)



#3:比较运算符  ==  >  >=  <   <=  !=
#运算结果是：布尔值  True  False

# x='get'
# y='GET'
# print('get'=='GET')  字母是区分大小写
# print('get'.upper()=='GET')

# x=5
# y=2
# print(x==y)


#4:逻辑运算符   and or not  优先级 not>and>or
#运算结果是：布尔值  True  False
# and 两边为真才为真 一假则假
# or 只要又一边为真就为真  一真为真
# a=5
# b=0
# 非空非零数据 True  空 0 False
# print(a and b)
# print(a>5 and not b==0)


#5:成员运算符  in not in  字符串  元祖  列表  字典   可迭代数据类型
#运算结果是：布尔值  True  False

d={'age':20,"name":'七月'}#默认判断的时候  拿到的是字典key
print(20 in d.values())
print(d.keys())