#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: for&while.py
  @time: 2019/02/21
  
  """
# while循环&for循环&嵌套循环

#什么时候才会用到循环：重复的操作
#while循环
# 语法  while  条件表达式：同if---》本质：布尔值  逻辑 成员  比较  各种数据类型
        #循环体
#有一个风险：容易进入死循环
# 如果要避免进入死循环  怎么办？
# 1：while 后面不要是永真式 那么while后面表达式的值 是要有变化

# a=0#初始值为0
# while a<5:
#     a+=1
#     print("Python是世界上最美的语言！")


# 2:while 后面是永真式 那么可以用break continue组合的方法防止进入死循环
# break终止循环  continue 结束本轮循环 继续下一轮循环
# while 1:
#     print("hhhhh")
#     break#终止循环
# a=0#初始值为0
# while 1:
#     if a<3:#a=0,1,2
#      print("Python是世界上最美的语言！")
#      a+=1
#      continue
#     else:
#      break

#Python 里面的：
#False 与False等价的还有数字0 空字典 空列表 空字符串 空元组
#True 与True等价的还有数字1 其他非0数字 非空列表 非空字典 非空字符串 非空元组
# 有一个空列表s=[]  利用while 循环  循环5次  每次询问一个人的名字
#并且把名字加到列表里面去  列表名.append()

# a=0
# s = []
# while a<5:
#     e=input("请输入用户名：")
#     s.append(e)
#     a+=1
# print(s)


# s=[]
# while len(s)<5:
#     # e=input("请输入用户名")
#     s.append(input("请输入用户名"))
# print(s)

# 列表名.append(值)
# s=[]
# s.append(8)


# for循环  遍历循环：每个挨个去循环
# 语法：
# for 变量名 in 数据：
#     #循环体
# l=['angle','cindy','sunny','johin']
# for i in l:#按顺序依次访问l里面的元素，有几个元素就会循环几次
#     #在访问l里面的每一个元素的同时，会赋值给i
#     print('hhhhhhh')
#     print('i:{}'.format(i))

# 到底用哪个循环？
# 确定用循环次数 用for
# 不确定循环次数 而是要达到某个限制的条件后才停止 用while

#有一个空列表 s=[] 我们利用for循环 循环5次 每次询问一个人的名字
# 并且把名字加到列表里面去 利用for来完成这个表达
#温馨提示 列表增加元素 可以用这个方法 列表名.append(值)
# in 后面的数据类型可以是什么呢？字符串 字典 元祖 列表
# s=[]
# for i in '12345':
#     print(i)
#     a=input("姓名：")
#     s.append(a)
# print(s)

# s=[]
# # for i in range(5):
# #     s.append(input("姓名："))
# # print(s)


# d={'name':'ddd','age':24,'salary':'12k'}
# # for i in d.values():d.values() d.keys() d.i()字典里面的键值对会显示出来
# #     print(i)



#嵌套循环

# s=['summ','saber','sadess','fillico','megan','cherry','alien','coober']
# #要求 把s里面的元素都打印出来
# # 把i这个字符串里面的每一个元素打印出来
# for i in s:
#      print(i)#必须是可迭代的数据
#      for e in i:
#          print(e)
# #冒泡算法：

