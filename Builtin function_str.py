#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Builtin function_str.py
  @time: 2019/02/26
  
  """
s='pytHonyy'
res=s.split('y',2)
print(res)
# s.isalpha()
# tran=s.maketrans('yy','bb')#翻译函数
# res=s.translate(tran)
# res=s.replace('y','@',1)#替换
#第一个参数是目标字符串
# 第二个替换的字符串
# 第三个参数是替换次数 默认是全部替换
# res=s.split('y',-1)#切割第一个参数  根据指定的字符进行切割
#第二个参数  切割次数  -1 默认是全部切割

# res=s.strip()#默认取出头和尾的空格,也可以去掉指定的字符 只能是头和尾
# print(len(s))
# print(res)
# print(len(res))


# res=s.swapcase()#大小写互换
# print(res)


#课后作业 自行了解没有讲过的函数
#然后配合老师安排的题目
# s.translate()
# s.swapcase()