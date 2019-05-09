#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_for.py
  @time: 2019/02/18
  
  """

s='python15' #8
L=[1,0.2,'桃子','旅行者','haha']#5
d={'name':'katt','age':18,'money':'10w'}#3
t=(1,5,6,'hi','how are you')#5

#练习题：
# 请利用for循环，依次打印字典d里面的value值

# b=d['name']
# print(b)
#
# for v in d:
#     print(d[v])
#
# for a in d.values():
#     print(a)


#for循环有什么关系呢
#什么是循环：单曲循环？
#for 循环


# a=0
# for item in s:#遍历  利用for循环 依次访问s里面的每一个元素 赋值给item这个变量
#     a+=1#赋值运算
#     print('{0}我要唱歌'.format(a))
#     # print(item)
#     print('----------')

#1:是不是可以访问指定的数据里面的元素？
# 2：还可以利用遍历，去控制循环次数


p=[[1,2,3],[4,5,6],[7,8,9]]
#请依次将p里面的子列表里面的每个元素 并且打印出来
for a in p:#[1,2,3]
    for b in a:#[1,2,3]
        print(b)


# for循环：有限次数的循环
# while循环：可以无限次数循环---死循环  同时  如果加以好好利用  用条件  有条件控制的循环





# list_1=[[1,2,3,4],[5,6,7,8]]
# for i in range(len(list_1)):
#     for j in range(len(list_1[i])):
#         print(list_1[i][j])




tuple_1=(1,2,3,4)
for i in range(len(tuple_1)):
    print(tuple_1[i])

