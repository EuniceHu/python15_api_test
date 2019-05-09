#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: context.py
  @time: 2019/04/26
  
  """
import re
from week_9.class_0420.common.config import config
def replace(data):
    p = "#(.*?)#"
    while re.search(p, data):  # 找到返回True
        print('data是', data)
        m = re.search(p, data)
        # 从任意位置开始找，找第一个就放回Match object ，如果没有就返回None
        g = m.group(1)  # 拿到参数化的key
        v = config.get('data', g)  # 根据KEY取配置文件里面的值
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)
    return data