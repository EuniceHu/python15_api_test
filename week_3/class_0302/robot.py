# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 9:36
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : robot.py

def robot(name,msg):
    print("{}你有一条信息：{}".format(name,msg))

#测试代码
if __name__ == '__main__':#代码执行的主入口
    robot('001','今天一起吃晚饭吗？')#调用函数