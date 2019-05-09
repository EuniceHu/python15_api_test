#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_0302_file.py
  @time: 2019/03/04
  
  """
#
# 有两行数据，存在txt文件里面：
#
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
#
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
#
# 请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
#
# [{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
#
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
#
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！
#
# 多思考多讨论！
#

# 思路：根据结果可以知道，结果是存到一个列表里面，列表里面的数据类型是字典
#第一次循环先把换行符去掉，按照@符号分割为3个元素
#第二次循环里面有3个元素，每个元素循环一次，就按照：分割1次 这样列表里面就有2个元素
#定义一个空字典，让索引为0的值等于索引为1的值
#最后把字典里面的值追加到空列表里面 返回值
def get_url(url):
    file=open(url)
    lines=file.readlines()
    # print(lines)
    list=[]#定义一个列表，存返回的数据
    for i in lines:
        yuansu=i.strip("\n").split("@")
        print(yuansu)
        dict={}
        for j in yuansu :
            t=j.split(':',1)
            print(t)
            dict[t[0]]=t[1]#d[key]=value  字典赋值
        list.append(dict)
    return list
print(get_url("url.txt"))


























# def get_url(url):
#     file = open("url.txt",encoding= 'utf-8') # 打开文件
#     lines = file.readlines()  # 按行读取
#     l = []   # 定义一个空列表，用来接收每行数据
#     for i in lines:
#         list = i.strip("\n").split("@")
#         dict = {}
#         for item in list:
#             temp = item.split(":",1)
#             dict[temp[0]] = temp[1]
#         l.append(dict)
#     return l
#
# print(get_url("url.txt"))


