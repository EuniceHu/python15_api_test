#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: contants.py
  @time: 2019/04/16
  
  """
import os

# base1_dir=os.path.abspath(__file__)
# print(base1_dir)
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#week_8的路径
# print(base_dir)
case_file=os.path.join(base_dir,'data','cases1.xlsx')
# print(case_file)

global_file=os.path.join(base_dir,'config','global.conf')
print(global_file)
online_file=os.path.join(base_dir,'config','online.conf')
print(online_file)
test_file=os.path.join(base_dir,'config','test.conf')
print(test_file)
db_file=os.path.join(base_dir,'config','db.conf')
print(db_file)
