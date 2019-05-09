# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:59
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_0305.py

str='我的是名字是lemon,今年5岁。'
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。

def analysis(s):
    number=[]#存储数字的列表
    ch=[]#存储中文的列表
    en=[]#存储英文的列表
    sign=[]#存储符号的列表
    #
    for item in s:
        if item.isdigit():#判断是否是数字
            number.append(item)
        elif item.isalpha():#判断是否是字母或者是汉字
            if item.encode().isalpha():
                en.append(item)
            else:
                ch.append(item)
        else:
            sign.append(item)

    print('数字:',number)
    print('中文:',ch)
    print('英文:',en)
    print('字符:',sign)

analysis(str)
# print('i'.isalpha())
# print('我'.isalpha())
# print('i'.encode().isalpha())
# print('我'.encode().isalpha())





