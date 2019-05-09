import json

str1 = '{"name":"yuze", "age": "18"}'

# 转化成字典
a = json.loads(str1)
print(a)

b = json.dumps(a)
print(type(b)) # json格式的 string