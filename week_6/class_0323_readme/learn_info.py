# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 10:46
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_info.py

def print_msg(*args):#动态参数/不定长参数  传递进来是组装成了元组
    print(args)
    print('数据的长度：{}'.format(len(args)))

print_msg([[0,0,0],[1,1,1]])
#
# print_msg(1,2,'hello',[1,2,3])