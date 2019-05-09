# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 10:05
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_file文件操作.py
#文件的新建 读取  写入数据
#open()#新建文件的操作 .txt 文本文件

# file=open('../class_0228/python15.txt',encoding='utf-8')#获取文件的操作权限 然后进行读或者写操作
# file=open('python15.txt','r+',encoding='utf-8')
# res=file.read(10)#读取的字符的长度
# print(file.tell())#按位
# print(res)
# # file.write('double同学在不在？！')
# # print(file.tell())#1个汉字--3位 数字符号英文 1位
# file.seek(3,0)
# print(file.tell())
# print(file.read(1))
# file.close()
#uft-8 gbk unicode-->3位--3位


#r 只读  读取的文件必须要存在，否则会报错，如果我们要进行读或者写的文件里面有中文  那么就要设置编码为utf-8
#r+读写  可以进行读写操作，但是目标文件必须要存在，否则会报错，
#1:先读再写  写入的内容就会写在最后面  2：直接写： 从头开始写  逐字覆盖写
#3：写在指定位置 tell()获取当前位置 seek(offset,where) 偏移光标/位置--了解
#offset 0 3 2 4 where 0 头部 1当前位置  2 尾部

#w 只写 清空写  如果文件存在，清空写；如果文件不存在，新建一个文件再去写
# file=open('python15.txt','w',encoding='utf-8')
# file.write('丢丢的班级逃课太可怕了！')
# file.close()

#w+ 读写 如果文件存在，清空写；如果文件不存在，新建一个文件再去写
# file=open('python15.txt','w+',encoding='utf-8')
# file.write('丢丢的班级逃课太可怕了！')
# file.seek(0,0)
# print(file.read())
# file.close()

#a 追加 如果文件存在，直接追加；如果文件不存在，新建一个文件再去写
file=open('python666.txt','a',encoding='utf-8')
file.write('丢丢的班级逃课太可怕了！')
# file.seek(0,0)
# print(file.read())
file.close()

#a+ 读追加如果文件存在，直接追加；如果文件不存在，新建一个文件再去写，可以读
file=open('python15.txt','a+',encoding='utf-8')
file.seek(0,0)
print(file.read())
file.write('99999！')
# file.seek(0,0)
# print(file.read())
file.close()

#rb rb+ wb wb+ ab ab+ #文件流的形式的去写入文件的时候  binary