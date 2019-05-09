# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 21:15
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_上下文管理器.py

with open('py15.txt','w+',encoding='utf-8') as file:
    file.write('今天演示失败，好沮丧')
print(file.closed)
