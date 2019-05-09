#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: list_Builtin.py
  @time: 2019/02/26
  
  """
#增删改查

# L=[0.02,100,'hello',(1,2,3),['python',0.02]]
#增加
#1)两个列表相加  两个列表的元素 会合成一个列表里面
# s=[4,5,6]
# L=s+L
# print(L)
#2）append() 给列表里面增加元素 增加最后面
# L.append('柠檬班')#一次只能添加一个元素
# print(L)


#3）insert()给列表里面增加元素 可以增加到指定位置
# L.insert(0,'柠檬')
# print(L)


#4)extend 扩展列表  效果与+等效
# s=[6,66,666]
# L.extend(s)
# print(L)


#改
# L=[0.02,0.02,100,'hello',(1,2,3),['python',0.02]]
# L[0]='花花'#赋值运算
# print(L)

#删除 pop() 默认删除最后一个元素
# res=L.pop()
# print(L)
# print('被删除的元素：',res)

# L.clear()#所有元素都清空
# L.remove(0.02)#删除指定的值
# print(L)

#查：利用索引取值  以及切片取值

#range函数
# range(m,n,k )#生成指定范围的证书序列
#切片很相似 取头不取尾
#m 索引头  n索引尾  k步长   k默认值为1
#传一个参数 默认索引头为0 从0开始
# res=list(range(1,6,1))#1 2 3 4 5
# print(res)

# res=list(range(10))
# print(res)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# res=list(range(0))
# print(res)
# []
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]
# for i  in  range(len(L)-1):
#     print(L[i])


# for i in range(len(L)-1,-1,-1):#range(3,-1,-1)  3 2 1 0
#     print(L[i])



L=[100,'hello',(1,2,3),['python',0.02],'hello']
# res=L.count(L[0])
# res=L.copy()#深copy浅copy
# res=L.index('hello',2)
# L.reverse()#列表翻转
# a=[1,7,4,89,34,2]
# a.sort(reverse=True)#针对数字之间进行比较
# print(a)