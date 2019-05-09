# 面试题：可变参数作为函数的默认值
# 可变类型 list, dict (string, int, float ,tuple, 不可变）

# 解决办法 1. 每次传实参
# 2.
# 3.
# def add(ele, mylist=None):
#     if not mylist:
#         mylist = []
#     mylist.append(ele)
#     return mylist
#
#     #     new_list = []
#     #     new_list.append(ele)
#     #     return new_list
#     #
#     # mylist.append(ele)
#     # return mylist
#
#
# print(add(4, []))
#
# print(add(5, []))
#
# print(add(6, []))
#
# # 字符串空， 整数是否为0 ，list 为[] , None, dict {}
# # a = 0
# # print("hello")
# # if not a:
# #     print("a 为空")
#
# # 函数的作用。 ==》 封装一段可以重复运行的代码
# # 函数封装可以提高代码的可读性。
#
# # 多写注释
# print('hello')
#
# ### 搜佛
# # OSofo
# print('hello')

# 类和对象。 是 python 里面最核心的。 生孩子
# __init__(self):    __new__ : return self
#    self.age = "f"

# 面试题：__init__  __new__
# 面试题：实现一个单例；
# 类属性和实例属性

class Movie:
    # 类属性
    workers = ['导演', '演员', '场记', '托', '编剧']

    def __init__(self, name):
        self.workers = []
        self.name = name

    # def __new__(cls, *args, **kwargs):
    #     pass
# movie1 = Movie("琅琊榜")
print(Movie("琅琊榜").workers) # 不统一
print(Movie.workers)  # None 报错。

# movie2 = Movie('琅琊榜')
# 盗版的。跟上面的不是同一个对象
Movie('琅琊榜').workers = ['导演']

# movie3 = Movie("琅琊榜")
print(Movie("琅琊榜").workers)  # ['导演']
print(Movie.workers)  #  ['导演', '演员', '场记', '托', '编剧']

# os.path 路径
# 异常处理  try...except Exception as e...:

# 捕获异常和抛出异常有什么关系

# try:
#     1/0
#     print("没出错！！！")
# except Exception as e: # 捕获异常
#     print("出错咯")
#     raise
# finally:
#     # close
#     pass
#
# # 文件处理   打开文件以后，一定要注意关闭
# open('file', 'r', encoding='utf-8')

# with open(...) as filename:
#     pass

# openpyxl  close()
# 上下文表达式

# Excel

# logging   loggere.
# parse config...  配置文件

# 测试 unittest
# TestCase, Suite,收集用例的容器，  loader,添加模块，类。  addTest.. 对象
# TextTestRunner, HTMLTestRunner


# DDT   # 装饰类@ddt.ddt   测试用例的@ddt.data(*) @ddt.unpack 脱衣服

# test_write_data()

# Excel #1.workbook 2. sheet 3.cell 对象。==》 值  cell.value  =>字符串





# 删除数据库， 删除整个系统， 做一些非常危险的攻击性行为
# 局部作用域
eval('print("hello")')












