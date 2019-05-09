#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: list.py
  @time: 2019/02/16
  
  """


#列表 list[]
#1：特征
#1.空列表 L=[]
# print(type(L))
#2.列表里面的元素可以是任意类型 不同的元素之间用逗号隔开
L=[1,0.02,'hello',True,(1,2,3,666,'python'),['python','java','ruby']]
#  0  1     2      3      4                         5  正序
# -6 -5    -4     -3     -2                         -1

#3.是有索引的 正序/反序编号都支持 取值方式同字符串
# L=[1,0.02,'hello',True,(1,2,3,666,'python')]
#单个取值 列表名[索引值]
# print(L[3])
#切片  列表名[索引头：索引尾：步长] 步长默认为1
#倒序排列
# print(t[::-1])
#嵌套取值 列表里面还有列表 层级定位
# print(L[-1][1][::-1])
#4：列表是有序可变类型
L[2]='不期而遇'#重新赋值
print(L)

#列表和元祖 并不是绝对的不能修改
t=(1,0.02,'hello',True,(1,2,3,666,'python'),['python','java','ruby'])
L=[1,0.02,'hello',True,(1,2,3,666,'python'),['python','java','ruby']]
t[-1][-1]='c#'
print(t)

L[4]='柠檬'
print(L)