#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: dict_Builtin.py
  @time: 2019/02/26
  
  """
# d={'name':'lemon','age':22,'score':99.99}
#增删改查

#增加和改   复制运算

#key 要求数据类型不可变  唯一不重复 字典名[key]
# print(d['name'])
# d['name']='summer'#key是唯一的
# d['sex']='男'
# print(d)
#字典名[key]=value key存在 那就是修改   key不存在  就是新增


#查 取值 字典名[key]

#删除 pop() 删除键值对

d={'name':'lemon','age':22,'score':99.99}
# d.pop('name')
# d.popitem()#随机删除
# d.clear()#清空--->空字典

# res=d.copy()
# res=d.items()#返回键值对
# res=d.keys()
# res=d.values()

# res=d.get('name')#根据key取值 get里面传递的参数 是key  字典名[key]

res=d.update()
print(res)