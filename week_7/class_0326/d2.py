"""
# 变量
# 有意义。 函数_  类 驼峰， global USERNAME 需要修改。 eval() 很大的副作用的。
# range()

数据类型
1. string  不可变类型
2. int
3. float
4. boolean  条件判断或者逻辑控制的依据。多种运算形式的返回值。
5. list  有顺序的容器。 可变
6. dict 没有顺序的。 可变
7. tuple 解包， 一个元素 （1,） 不可变类型


逻辑控制，流程控制，控制流程
条件 if...elif...else:
遍历 for...in;;
while:
continue, break

函数：
1.参数。。 形式，实际，位置参数，关键字，默认参数。 动态参数
*args **kwargs, *a, **b **kw ==> keywords
2. return 遇到 return 终止运行






"""
# 面试题1： 列表非常相似的一种数据结构。
# print(type(range(1,2)))

# 面试题2.
# str1 = "myclsss"
# str1[2] = 's'



# my_dict = {"name": "yuze", "age": "16"}
#
# for key,value in my_dict.items():
#     print(key, value)
#
#
# def run(a):
#     if a!= 10:
#         return None
#
#     print("hekle")
#     print("continue")


# 务必弄懂。。经典面试 80% 的, 提出改进计划。。。
def add(a, mylist=[]):
    if not mylist:
        mylist = []
    mylist.append(a)
    return mylist

print(add.__defaults__)
print(add(4))  # [4]
print(add.__defaults__)
print(add(5))  # [4,5]
print(add.__defaults__)
print(add(6, ['a']))  #["a", 6]
print(add.__defaults__)
print(add(7))   #[4,5,7]
print(add.__defaults__)










