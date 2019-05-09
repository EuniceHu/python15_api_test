# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 21:31
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_0303.py

# 请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
# [{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register',
# 'mobile':'18688773467','pwd':'123456'},
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge',
# 'mobile':'18688773467','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！
file=open('py15.txt')
resp=file.readlines()#返回的是一个列表 每一行作为一个字符串元素
# print(resp)
# print(resp[0])
L=[]
for element in resp:
    r_1=element.strip('\n')
    r_2=r_1.split('@')#返回的还是列表
    # print('r_2:',r_2)#是一个列表  有3组元素
    d={}#d[key]=value
    for item in r_2:
        value=item.split(':',1)
        # print(value)
        d[value[0]]=value[1]
    L.append(d)
print(L)

# L=[]
# for element  in resp:
#     d={}#d[key]=value
#     for item in element.strip('\n').split('@'):
#         value=item.split(':',1)
#         d[value[0]]=value[1]
#     L.append(d)
# print(L)


# L=[]
# for value in resp:
#     value_1=value.strip('\n')
#     value_2=value_1.split('@')
#     print(value_2)#返回的是列表 列表里面的元素都是字符串
#     d={}
#     for item in value_2:
#         item=item.split(':',1)#根据冒号去切割 但是指定切割一次？
#         print(item)
#         d[item[0]]=item[1]
#     L.append(d)
#     print(L)
# s='url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456\n'
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'}