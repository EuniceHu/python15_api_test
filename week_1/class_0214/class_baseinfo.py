#-*- coding:utf-8 _*-
"""
  @author:10701
  @file: class_baseinfo.py
  @time: 2019/02/15
  
  """


#标识符---取名字
#项目名  包名 文件名 函数名 变量名 类名
# 标识符的规范
# 1》数字 字母 下划线 组成
# 2》不能以数字开头
# 3》字母和数字之间可以用下划线隔开 方便阅读
# 4》见名知意
# 5》不能以关键字命名

# print('hello world')# 函数 输出内容到控制台
#
# a=input('请输入一个数据：')
# print(a)

#注释
#单行注释 ctrl+/
"""
多行注释
"""

#变量   x=1 y=1 如果你要使用某个变量的时候 一定要确保它已经被定义 否则会报错
# a=4
# print(a)

#Python 里面的数据类型

# 数字 布尔值 字符串 列表 元祖 字典 集合等各种类型的数据

#1：数字：整型 int 浮点型 float
#type(数据)
# print(type(300.0))
# 2:布尔值 True 1/非空数据 False 0/空数据
# 学习if 语句的时候会复习

# 3：字符串 str string
# 成对的单引号 双引号 以及三引号括起来的内容都是字符串
# a='0.004'
# b="我爱学习"
# c="""
#      sadess,
#      我爱学xi,
#      hhhhh
#    """
# print(type(a))
# print(c)
# 如果你的字符串换里面必须包含单引号  最外层用双引号
# e="你好，我的名字是：'hhhh'"
# print(e)
# 如果你的字符串换里面必须包含双引号  最外层用单引号
# d='你好，我的名字是："hhhh"'
# print(d)

#空字符串----for  循环
# s=''
#  len(数据) 统计数据的长度
# print(len(s))
# print(type(s))

#字符串的长度：字符串里面的任意单个字符都是一个元素
#单个字符  汉字  数字   字母  符号
h='我爱北京天安门'
# print(len(h))

#索引 index  从0开始编号 0 1 2 3
    #反向编号 -1 -2 -3 -4
# 单个取值：变量名(字符串)[索引值]
print(h[4])

#切片：字符串名[索引头：索引尾：步长]  取头不取尾
#步长不写默认为1
# print(h[4:7:1])#4 5 6  最终取到的是4 5 6 索引在的位置
#用反向编码来取值 倒序输出
# print(h[::-1])#反向取值
print(h[:4])


# ------------------自己--------------------

#字符串 str
# a='hello python15'
# 1:常规用法：字符串的取值和切片
# 1）字符串里面元素：单个字符算一个元素（数字 字母 符号 中文）
# 2）统计字符串的长度：len(a)
# print(len(a))
# 3)如何取值：字符串取值是根据索引来的 索引是什么呢？是字符串元素的编号
# 编号是从0开始的  取值方式：变量名[索引]
# 4）切片:用法 变量名[m:n:k] m开始取值的索引位置 n取值结束的位置，取值不包含  k步长
# 取左不取右，取到n-1
# print(a[0:13:1])#0 1 2 3 4 5 6 7  8 9 10 11 12
# print(a[0:13:3])#0 3 6 9 12
# #请把a字符串里面年号为偶数的元素打印出来
# print(a[0:13:2])
# print(a[::2])
# #请把a字符串利用切片实现倒序输出
# print(a[::-1])
# # 取最后一个元素
# print(a[-1])
#
# #字符串的拼接 +
# s_1='hello'
# s_2='你好'
# a=20#转换成字符串 str()强制转化
# print(s_1+s_2+str(a))
# print(s_1+s_2,a)



# # 函数
# b='hEllo pPythOn15y'
# #切换大小写 upper变成大写 lower变成小写
# print(b.upper().lower())
# print(b.isupper())
# print(b.swapcase())#大小写互换


#replace 替换方法
# s=b.replace('l','@',1)
# print(s)

#find 查找元素  没有找到就返回-1 只考虑正序  不考虑反序

# print(b.find('13y')) #单个字符如果找到了，返回的是遇到的第一个元素的索引的值
# #子字符串 长度大于1 如果找到了 就返回子字符串所在第一个元素的位置
#
# print(b.count('o'))
# print(b.index('h'))
#
# #布尔值  True False
#
# print(b[1].islower())
# print(b[1].isupper())
# print('@'.join(b))
#
# print(b.split('l'))#切割  返回的是列表  切片返回的是字符串




















