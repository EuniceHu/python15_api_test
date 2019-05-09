#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_for&while.py
  @time: 2019/02/19
  
  """

# for循环的作用：1：遍历元素  2：可以控制循环次数
# for循环可用来遍历的数据类型：str tuple list dict---目前所学
#还有很多数据类型  只要是可迭代 就可以用for循环来遍历
#可迭代的数据类型：数据里面允许存在多个元素的或者是0个
#如果用整数  int类型 ：TypeError: 'int' object is not iterable

# for item in 5:
#     print(item)

#想办法：怎么利用函数去判断我的数据类型是可迭代的---自己去找

from collections import Iterable
# s=isinstance('abc',Iterable)
# print(s)
# l=isinstance('[1,2,3]',Iterable)
# print(l)
# i=isinstance(12,Iterable)
# print(i)
# t=isinstance((1,2,3),Iterable)
# print(t)
# d=isinstance({'name':'hh',"age":18},Iterable)
# print(d)
# d={'name':'katt','age':18,'money':'10w'}
# a=0
# for item in d.values():
#     a+=1
#     print('这是第{}次循环'.format(a))
#     print(item)
# print(d.keys())
# print(d.values())


#range函数：生成一个整数序列   可迭代的对象
#range(m,n,k)#m开头的数字  n结尾的数字  k步长  默认值为1 取左不取右
#如果range(m,n) k默认为1
#如果range(n) m默认为0
# res=range(1,10,3)#1,4,7
# print(list(res))#为了方便你们观察我们拿到的是什么？强转列表

# res=range(1,10)#
# print(set(res))

#题目  我要生成0~100的数字
# res=range(101)
# print(list(res))

# 1:写一段程序，分别求出0-100之间所有数之和
# sum=0#初始值 用来储存我们求的和
# for item in range(101):
#     sum=sum+item
# print(sum)

# 1:写一段程序，分别求出0-100之间所有奇数之和
# sum_1=0
# for i in range(1,101,2):
#     sum_1=sum_1+i
# print('奇数和：',sum_1)


# 2:写一段程序，分别求出0-100之间所有偶数之和
# sum_2=0
# for i in range(0,101,2):
#     sum_2=sum_2+i
# print('偶数和：',sum_2)


# 解法2：

# sum_1=0#初始值 用来储存我们奇数和
# sum_2=0#初始值 用来储存我们偶数和
# for i in range(101):
#     if i%2==0:#说明这个是偶数
#         sum_2=sum_2+i
#     else:
#         sum_1=sum_1+i
# print('奇数和：',sum_1)
# print('偶数和：',sum_2)



#嵌套循环:循环里面还有循环
# p=[[1,2,3],[4,5,6],[7,8,9]]
# #请依次将p里面的子列表里面的每个元素 并且打印出来
# for a in p:#[1,2,3]  外层循环
#     for b in a:#[1,2,3]  内层循环
#         print(b)



# p=[['*'],['*','*'],['*','*','*'],['*','*','*','*'],['*','*','*','*','*']]

for i in range(1,6):#1,2,3,4,5
    for j in range(1,i+1):#range(1,2) range(1,3)
        print('*',end='')
    print()

# while循环：
# while 条件表达式：
    # 循环体

#条件表达式：跟if是一样的
# 1：一般逻辑运算  比较运算  成员运算
# 2：非0 和非空的数据表示True 为0和为空的数据 表示False(非常重要)
# 3：可以直接用布尔值来代替表达式

# 运行模式：先判断while后面的条件  满足  就执行循环体  不满足的话  不执行
# 执行完毕之后  再次判断while后面的条件 满足 就执行循环体 不满足的话  不执行
# 如此反复

#怎么达到 不是绝对的True 也不是绝对的False
# 1:基本解决方法：break  中断循环  如果用的不好的话  就是执行一次
# 2:进阶使用：break+条件  条件就是规定他循环多少次
# 3:高级使用：必要的时候  脱离break 自由自在
#continue 继续下一次次循环




# a=0
# while a<10:
#     a+=1#a=10
#     print('a的值',a)
#     print('死循环{0}'.format(a))



# sum=0
# for i in range(1,101):#1,2,3,4,5.....100
#     sum=sum+i#1+2+3+4...+100
# print(sum)


# a=[5,6,7,9,10,23,45]
# print(a[::-1])

# count=0#记录满足条件的人数
# for i in range(1,11):  #range while做一遍
#     age=int(input('请问你今年多大了？'))#转了整数
#     if 10<=age<=12:
#         sex=input('填写一下你的性别？')
#         if sex=='f':
#             print('可以加入女子足球队！')
#             count+=1#满足条件就+1
#         else:
#             print('很遗憾，你不能加入足球队！')
#     else:
#         print('很遗憾，你不能加入足球队！')
# print('可以参加足球队的人数是{}个人'.format(count))




# a=0
# count=0
# while a<10:
#     a+=1
#     age=int(input('请问你今年多大了？'))
#     sex=input('填写一下你的性别')
#     if 10<=age<=12 and sex=='f':
#         print( '可以加入女子足球队')
#         count+=1
#     else:
#         print('很遗憾，你不能参加足球队！')
# print('加入足球队的人数为{}'.format(count))














# a=0
# count=0
# while a<10:
#     a+=1
#     age=int(input('请问你今年多大了？'))
#     if 10<=age<=12:
#         sex=input("请填写一下性别")
#         if  sex=='f':
#             print( '可以加入女子足球队')
#             count+=1
#         else:
#             print('很遗憾，你不能参加足球队！')
#     else:
#         print('很遗憾，你不能参加足球队')
# print('加入足球队的人数为{}'.format(count))

# p=int(input('请输入购买金额：'))
# if 50<=p<=100:
#     print('我们会给10%的折扣')
#     print('最终价格为：{}'.format(p*0.9))
# elif p>100:
#     print('我们会给20%的折扣')
#     print('最终价格为：{}'.format(p*0.8))
# else:
#     print('不好意思，没有折扣')


# a=[1,2,3,"this is a list"]
# b=[4,5,6,"这是第二个列表"]
# print(a+b)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[2:])
# L=[
#     ['Apple','Google','Microsoft'],
#     ['Java','python','Ruby','PHP'],
#     ['adam','bart','lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])
