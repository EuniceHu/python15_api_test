# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 20:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 类与对象.py

#万物皆对象
#对象都是会属于具体某个类的

#猫类
#叫声 喵喵喵  有尾巴 猫科动物  有胡须  有爪子  抓老鼠 喜欢吃鱼
#爱干净

#男朋友类
#高 富 人品好 有钱 会高效  自律 白  有才华 体贴 疼人  有车 会写代码 爱国 不秃顶

#实际的男朋友类
#高 写代码 有车  会做饭 喜欢有用 打篮球  sex=男

#继承、封装、重写、多态--->语言特性   提高代码的复用性

#类的语法

# class 类名:
#     '''类的解释文档'''
    #1）类的方法：功能
    #2）类的属性：特征

#类名的规范：标识符 数字 字母 下划线组成 ，不能以数字开头
#见名知意   不能使用关键字   驼峰命名：每个单词首字母大写
# HuaHuaLemon  huaHuaLemon
# SaberLemon   saberLemon


#实际的男朋友类
#高 写代码 有车  会做饭  打篮球  sex=男
#怎么变成代码
class BoyFriend:
    '''这是一个男朋友类，主要是用来描述男朋友这一类人'''
    #属性
    sex='boy'
    height=170

    #方法--->90%的相似度--函数
    def coding(self,language='python'):
        print('会写{}代码，而且写的66的'.format(language))

    def cooking(self,*args):
        dish_name=''#初始字符串 空字符串
        for item in args:#遍历args这个元组
            dish_name+=item#遍历每个元素 之后 都加到dish_name这个字符串上去
            dish_name+='、'#每个选项之间 加顿号隔开
        print('会做饭，而且擅长做{}'.format(dish_name))

    def play_basketball(self):
        return '最喜欢打篮球'

#万物皆对象--对象肯定是属于某个类--->类可以产生对象
#创建对象：类名()
t=BoyFriend()#一个对象

#对象具有类的所有属性和方法   调用  对象.属性  对象.方法
print(t.sex)
print(t.height)

t.coding()
t.cooking('方便面','蛋炒饭','西红柿蛋汤')
res=t.play_basketball()
print(res)


# 手机：
# A 颜色  B 像素  C 听歌 D 打电话  E 发短信  F 上网  G尺寸大小

# t1=BoyFriend()
# t2=BoyFriend()
#
# print(id(t1))
# print(id(t2))
