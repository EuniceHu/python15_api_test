#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_def.py
  @time: 2019/02/20
  
  """

#函数的定义：实现某个指定的功能  重复使用
# type()
#函数有什么作用 :提高代码的复用性

# 函数的语法：关键 def  顶格写
# 函数的具体语法：
# def 函数名(参数1,参数2,参数3)：
#     函数体：本函数要实现的功能
#     return 表达式


# def 顶格写  表示这个是一个函数
# 函数名  小写   不同的字母与数字之间用下划线隔开   不能用数字开头
# 参数的个数可以大于等于0
# 函数体是函数的子代码  要有缩进  写自己想实现的功能即可
# return后面的表达式 >=0个
# return的作用 就是当你调用函数的时候 会返回return后面的表达式的值
#如果return后面没有表达式  写没写  没有区别
# 如何调用函数 函数名(对应个数的参数)
#
# def radio_machine():
#     print("复读机，你好")
#     return #隐式的添加一个return关键字
# res=radio_machine()#存储返回的值
# print('函数的返回值是：{}'.format(res))


#1：return后面的代码不再执行，所以我们的有效代码要放在return前面
#2：return表示函数的结束
# 函数里面return的表达式个数   支持0个或多个  如果函数里面没有写return
# 就会隐式添加一个return 返回none
# ==1返回你指定的数据信息
# >1返回的是元祖类型，用逗号区分
# ==0返回none

#拿到add()运行的求和结果  再去加20 输出到控制台
# def add():
#     result=8+8
#     return result
#
# res=add()+20
# print(res)
# def count_number():
#     count=0
#     for i in range(1,20):
#         count+=i
#     return count#隐式的添加
# print(count_number())




# def print_info():
#     print('本节课学的是函数')
# print_info()



# def favorite_book(bookname):
#     print('我最喜欢的图书是{}'.format(bookname))
# favorite_book("百年孤独")




# def favorite_book(bookname="柠檬班Python自动化教科书"):
#     print('我最喜欢的图书是{}'.format(bookname))
# favorite_book()




# def add(a,b=3,c=5):
#     print(a+b+c)
# # add(1,2,3)
# add(1,6)
# add(1)
# add(1,c=6)



# def make_shirt(size,logo):
#     print("T恤的尺码是{}字样是{}".format(size,logo))
# make_shirt('M','hello')




# def describe_city(a='shanghai',b='china'):
#     print('{} is in {}'.format(a,b))
# describe_city()
# describe_city('beijing')
# describe_city('la','usa')



# def city_country(a,b):
#     s=[a.title()+','+b.title()]
#     return s
# c1=city_country('changsha','china')
# print(c1)



def make_album(a,b):
    d={'name':'{}'.format(a),'album':'{}'.format(b)}
    return d
k=make_album('周杰伦','七里香')
print(k)
l=make_album('林俊杰','西界')
print(l)
y=make_album('蔡依林','jolin')
print(y)



# 课本38页第2题

# def make_album(a,b):
#     d={'name':'{}'.format(a),'album':'{}'.format(b)}
#     return d
# k=make_album('周杰伦','七里香')
# print(k)
# l=make_album('林俊杰','西界')
# print(l)
# y=make_album('蔡依林','jolin')
# print(y)


# 课本38页第3题
while True:
    n=input("请输入歌手名字：")
    album=input("请输入专辑名称：")
    def make_album(n, album):
        d = {'name': '{}'.format(n), 'album': '{}'.format(album)}
        return d
    w=make_album(n,album)
    print(w)
    break
