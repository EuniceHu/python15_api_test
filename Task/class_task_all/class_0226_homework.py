#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_0226_homework.py
  @time: 2019/02/27
  
  """
# 1、请编程实现字符串的转换：将”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”
# 字符串大写变小写，小写变大写。
# 并且将字符串变为镜像字符串。
# 例如：字符串里面的’A’变为’Z’,’b’变为’y’ ，
# 镜像的意思就是照镜子，对比了解下。
#
# def change_str_1(s):
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# new_s=''
# for item in s:
#     if item.isupper():
#         item=item.lower()
#         item=chr(219-ord(item))
#         new_s+=item
#     else:
#         item=item.upper()
#         item=chr(155-ord(item))
#         new_s+=item
# print('大小写互换之前的字符串:',s)
# print('镜像字符串：',new_s)


#
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# new_s=''
# for item in s:
#     if item.islower():
#         item=item.upper()
#         item=chr(155-ord(item))
#         new_s+=item
#     else:
#         item=item.lower()
#         item=chr(219-ord(item))
#         new_s+=item
# print('大小写互换之前的字符串:',s)
# print('镜像字符串：',new_s)









# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# change_str_1(s)

# print(chr(115-ord(item)))
# print(chr(219-ord(item)))


# A--->Z  65    90   115
# a--->z  97    122   219


# def change_str(s):
#     intab='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#进
#     outtab='zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'#出
#     trantab=str.maketrans(intab,outtab)#做一个翻译表
#     res=s.swapcase()#切换大小写
#     res_1=res.translate(trantab)
#     print('大小写互换之后的字符串：{}'.format(res))
#     print('镜像字符串：{}'.format(res_1))
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# change_str(s)

# 2：搜索引擎中会对用户输入的数据进行处理，
# 第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的是名字是lemon,今年5岁。
# 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。

#第一种方法：
# s=input("请输入语句：")
# sz = ''  # 数字
# zw = ''  # 中文
# py = ''  # 拼音
# fh = ''  # 符号
# for c in s:
#     if c.encode('utf-8').isalpha():  # 是否为拼音
#         py+=c
#     elif c.isdigit():  # 是否数字
#         sz+=c
#     elif c.isalpha():  # 是否为中文
#         zw+=c
#     else:
#         fh+=c
# print('数字：{}'.format(sz))
# print('中文：{}'.format(zw))
# print('拼音：{}'.format(py))
# print('符号：{}'.format(fh))





# 第二种方法是用函数做的，但是输出的时候报错，还需要老师讲解
# def word_analy():
#     sz=[]#数字
#     zw=[]#中文
#     py=[]#拼音
#     fh=[]#符号
#     s=input("请输入词句：")
#     for c in s:
#         if c.isalpha():
#             if c.encode().isalpha():
#                 py.append(c)
#             else:
#                 zw.append(c)
#         elif c.isdigit():
#              sz.append(c)
#         else:
#             fh.append(c)
#     print("""
#          数字：{}
#          中文：{}
#          拼音：{}
#          符号：{} """.format("".join(sz),"".join(zw),"".join(py),"".join(fh)))
#     return
# word_analy()


# 第三种方法：

str='我的是名字是lemon,今年5岁。'


num=[]
ch=[]
en=[]
sign=[]
def analy(s):
    for i in s:
        if i.isdigit():
            num.append(i)
        elif i.isalpha():
            if i.encode().isalpha():
                en.append(i)
            else:
                ch.append(i)
        else:
            sign.append(i)
    print('数字:',num)
    print('中文:',ch)
    print('英文:',en)
    print('字符:',sign)
analy(str)







# a='a'
# b='我'
# res=a.encode()
# print(res)


# t=(1,2,3,4,5,6)
# print(t[::])
# print(t[1:7:2])#[索引头：索引尾：步长]
# print(t[:7:2])
# res=t.index(3)
# print(res)

# t=[1,0.02,'hello',True,(1,2,3,666,'python')]
# l=[77,88,'wow']
# print(t[4][4])

# t[1]='hahah'
# print(t)

# t=t+l
# print(t)
# t.append(999)
# print(t)
# t.insert(3,'lol')
# print(t)

# t.extend(l)
# print(t)
# res=t.pop(1)
# # print(res)
# t.remove('hello')

# t.clear()
# print(t)

# res=t.count('hello')
# print(res)

# h=['mmm', 'mm', 'mm', 'm']
# # h=[8,3,6,7,9]
# # h.sort(reverse=False)#对列表进行排序，True为倒序 False为正序
# h.sort(key=len)
# print(h)

# d={'name':'lol','age':18,'friend':('hhh','kkk','lll')}
# s=len(d)
# print(s)
# res=d.keys()
# print(res)
# res=d['name']
# print(res)
# res=d.items()
# print(res)
# d.pop('name')#根据key值来删除
# print(d)
# d.popitem()
# print(d)
# d.copy()
# print(d)























