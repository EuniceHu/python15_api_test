#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: file.py
  @time: 2019/02/26
  
  """
#file:txt 日志  不包括mp4 excel html
#处理：读，写
#什么时候用呢：想用就用


#存储数据的操作
#第一步：打开文件 open()  file
#有中文的时候，注意设置编码为utf-8
file=open('python.txt',encoding='utf-8')
# print(file.read())#默认是读取文件中的所有内容，保持格式
# print('----------------------------')
# print(file.read(5))
# print('******************************')
# print(file.readline())#按行读取 每次只能读一行的内容

# print(file.readlines())#按行读取，读完所有行---返回列表 每一行是列表的一个元素


#练习：读出前10行诗句，怎么读
# print(file.readline())
# for i in range(10):
#    print(file.readline())
# #
# #
# # count=0
# # while count<10:
# #     print(file.readline())


#读出5-8行的诗句 怎么读

# for i in range(1,10):#5,6,7,8
# #     if 5<=i<=8:
# #      print(file.readline())
# #     else:
# #         file.readline()

#读出1~4行的诗句

for i in range(1,10):
    if 1<=i<=4:
        print(file.readline())
    else:
        file.readline()


# for i in range(1,10):
#     if 2<=i<=5:
#         print(file.readline())
#     else:
#         file.readline()



#open()函数
# 文件打开的模式
# 只读模式的情况下 去进行写操作 报错
#r只读     r+ 读写
#w 只写    w+ 读写
#a只能追加写   a+读写
# 1、w 写模式，它是不能读的，如果用w模式打开一个已经存在的文件，
# 会清空以前的文件内容，重新写
#    w+ 是读写内容，只要沾上w，肯定会清空原来的文件
# 2、r 读模式，只能读，不能写，而且文件必须存在
#    r+ 是读写模式，只要沾上r，文件必须存在
# 3、a 追加模式，也能写,在文件的末尾添加内容
# 4、rb+、wb+、ab+,这种是二进制模式打开或者读取，一些音乐文件
# file=open('python.txt','r+',encoding='UTF-8')
# print(file.readline())
# file.write('hahaha')
# file.seek(0,0)#重新改变光标的位置 移动的量  相对位置 0 开头 【1当前位置  2尾巴】---二进制文件才能用到
# print(file.read())
#
#
# file=open('yu.txt','w')
# file.close()#关闭文件
# W模式下，如果打开不存在的文件，就会新建一个文件
#W模式下，如果打开存在的文件，就会清空文件，再去做其他操作

# a+模式 读写  能不能读，关键是看光标在哪里
# file=open('python.txt','a+',encoding='UTF-8')
# file.write('isnns的名字好长啊！！！')
# file.seek(0,0)
# print(file.read())

