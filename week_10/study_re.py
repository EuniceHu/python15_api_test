#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: study_re.py
  @time: 2019/04/25
  
  """
import re
#解析正则表达式-->在字符串里查找
from week_9.class_0420.common.config import config

data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
#原本字符，元字符
# p = "normal_user" #正则表达式
# p="#.*?#"
# m=re.search(p,data)#从任意位置开始找，找到第一个就返回
# print(m)

#元字符
#()代表一个组，代表查找开始和结束
# p="#(.*?)#"
# m=re.search(p,data)
# #从任意位置开始找，找第一个就放回Match object ，如果没有就返回None
# print(m.group())#返回表达式和组里面的内容
# print(m.group(1))#只返回指定组的内容
# g = m.group(1)#拿到参数化的key
# v=config.get('data',g)#根据KEY取配置文件里面的值
# print(v)
# data_new=re.sub(p,v,data,count=1)#查找替换 count查找替换的次数
# print('data_new',data_new)
# ms=re.findall(p,data)#查找全部，返回列表
# print(ms)
#如果要匹配多次，替换多次，使用循环来替换
p="#(.*?)#"
while re.search(p,data):#找到返回True
    print('data是',data)
    m = re.search(p, data)
    # 从任意位置开始找，找第一个就放回Match object ，如果没有就返回None
    g = m.group(1)  # 拿到参数化的key
    v = config.get('data', g)  # 根据KEY取配置文件里面的值
    print(v)
    #记得替换后的内容，继续用data接收
    data = re.sub(p, v, data, count=1)  # 查找替换 count查找替换的次数
print('最后替换后的data',data)




