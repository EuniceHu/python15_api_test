#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: module_import.py
  @time: 2019/03/02
  
  """

# import os
# name='hhh'

#除了顶级项目名外 一层一层的去定位你要用的模块
#导入的方式一：import 模块名 具体到模块名 不需要.py这个后缀
#如果文件在python的安装目录下，可以直接导入

# import week_3.class_0228.add
# week_3.class_0228.add.add_function(8,9)

#导入的方式二：import 模块名  as newname 具体到模块名 不需要.py这个后缀
#as取个别名

# import week_3.class_0228.add as t
# t.add_function(8,9)


#导入的方式三：from...import... import后面可以具体到模块名以及函数名以及类名

# 一：具体到函数名#
# from week_3.class_0228.add import add_function#具体到函数名
# add_function(20,78)
# 二：具体到模块名#
# from week_3.class_0228 import add 具体到模块名
# add.add_function(10,20)
# add.sub_function(11,22)

# 三：*代表所有的#
# from week_3.class_0228.add import *
# add_function(10,20)
# sub_function(11,22)

#导入的方式四：当函数名称较长的时候，可以取个别名
from week_3.class_0228.add import add_function_two_positive_number as x
x(11,22)

#导入模块记住一句话：除了顶级目录，一层一层的去定位，相对当前模块