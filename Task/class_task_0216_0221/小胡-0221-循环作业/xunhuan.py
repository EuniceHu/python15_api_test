#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: xunhuan.py
  @time: 2019/02/22
  
  """
# 1：人和机器进行猜拳游戏写一段程序，首先选择角色：
# 1 曹操 2张飞 3 刘备，然后选择的角色进行猜拳：
# 1剪刀 2石头 3布 玩家输入一个1-3的数字
# ；然后电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果（ 1剪刀 2石头 3布 ） ，
# 双方出拳完毕后：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
# 然后提示用户是否继续？按y继续，按n退出。
# 最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束


import random
role_dict={'1':'曹操','2':'张飞','3':'刘备'}
fist_dict={'1': '剪刀', '2': '石头','3': '布'}

#选择角色
while True:
        role_num=input('请选择你要的角色：1 曹操 2张飞 3 刘备')
        if role_num in role_dict.keys():
            role_name=role_dict[role_num]
            print(role_name)
            break
        else:
            print('角色选择只能输入1 2 3')
            continue
#选择出拳

while True:
    human_fist_num=input('请出拳：1剪刀 2石头 3布')
    if human_fist_num in fist_dict.keys():
        human_fist_value=fist_dict[human_fist_num]
        print('{}出的拳为{}'.format(role_name,human_fist_value))
        print(human_fist_value)
        break
    else:
        print('出拳只能输入1 2 3')
        continue





# w=0#赢的次数
# L=0#输的次数
# p=0#平局的次数
# import random
# while True:
#     role = input("请选择你的角色：1 曹操 2张飞 3刘备:")#玩家
#     i = random.randint(1, 3)#电脑
#     h = int(input("请出拳：1剪刀 2石头 3布:"))
#     if i==h:
#        print('平局')
#        p+=1
#     elif (i==1 and h==2)or(i==2 and h==3)or(i==3 and h==1):
#         print('恭喜玩家{}赢了！'.format(role))
#         w+=1
#     else:
#         print('玩家{}输了！再来一局吧！'.format(role))
#         L+=1
#     print("游戏是否要继续！按y继续，按n退出")
#     c=input("请输入Y或者N：")
#     if c=='Y':
#         print("游戏马上开始！")
#         continue
#     else:
#         print("退出游戏！")
#     break
# print('玩家{}赢了{}次'.format(role,w))
# print('玩家{}输了{}次'.format(role,L))
# print('平局{}次'.format(p))

# 2：完成1-10的整数数字相加，并打印最后的结果

# sum=0
# a=0
# while a<10:
#     a+=1#1,2,3,4,5,6,7,8,9,10
#     sum=sum+a
# print('1-10的整数数字之和是{}'.format(sum))


# 3.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，m
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
# count=0
# a=0
# while a<10:
#     a+=1
#     age=int(input("请输入你的年龄："))
#     if 10<=age<=12:
#         sex=input("请输入你的性别：")
#         if sex=='f':
#             print("恭喜你！可以加入女子足球队！")
#             count+=1
#         else:
#             print("无法参加女子足球队")
#     else:
#         print("无法参加女子足球队！")
# print('满足条件的人数为{}'.format(count))


# 4:利用Python代码画出直角三角形以及等边三角形，如下所示：

# 第一：while
# a=0
# while a<5:
#     a+=1
#     print('*'*a)

# 第二 ：for
# for i  in range(1,6):#1,2,3,4,5
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()


# 等边三角形
# for i in (1,2,3,4,5):
#     print(' '*(5-i),end='')
#     print(' *'*i)




# 5：输出99乘法表
# for m in range(1,10):
#     for n in range(1,m+1):
#         print('{}*{}={}'.format(m,n,m*n),end=',')
#     print()



# 6：经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：
# 冒泡排序：小的排前面，大的排后面。两两比较 n-1次 最多比较
#相邻两个数进行比较
# 1 4 7 34  2 89
# 1 4 7 2  34 89
# 1 4 2 7  34 89
# 1 2 4 7  34 89
# a=[1,7,4,89,34,2]
# n=len(a)
# # print(n)
# for i in range(0,n-1):#i=0,1,2,3,4,5
#     for j in range(0,n-1-i):#j=(01234,0123,012,01,0)
#         if a[j]>a[j+1]:#a[0]>a[1],a[1]>a[2],a[2]>a[3],a[3]>a[4],a[4]>a[5]
#             a[j],a[j+1]=a[j+1],a[j]#把a[j+1]的值赋给a[j]
#         print(a[j])
# # print(a)



# a=[2,7,4]
# for i in range(len(a)):# i=0,1,2
#     for j in range(len(a)-i-1):#j=0,1  1  0
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# a=[1,7,4,89,34,2]
# for j in range(len(a)-1):#控制循环次数n-1次循环
#     for i in range(len(a)-1):#0,1,2,3,4,5
#         '''下面的for循环作用是完成每一次相邻两个数据的比较并且完成数值的交换'''
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)


# 7：有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？
# 分别是什么？abc a!=b!=c
# count=0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if (a!=b)and(b!=c)and(a!=c):
#                 print('互不相同且无重复的数字是：{}{}{}'.format(a,b,c))
#                 count+=1
# print("一共可以组成{}个无重复数字".format(count))






# a=2
# b=4
# a,b=b,a
# print('a:',a)
# print('b:',b)#a与b的值互换 交换值 赋值运算




