#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: study_eval_json.py
  @time: 2019/04/16
  
  """
"""
数据类型的转换，str--->dict
"""

import json
#正常的json格式
#{"key":}
params= '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'#返回
p = '{"mobilephone":"15810447878","pwd":None}'#请求入参
d=eval(p)
print(p)

# d=eval(params)#根据python的数据类型来做转换
# print(d["status"])

d1=json.loads(params)
print(type(d1),d1)
print(d1['msg'])

#定义空值为NONE的时候，可以用eval转换
#空值为null的时候，需要用json.loads()转换