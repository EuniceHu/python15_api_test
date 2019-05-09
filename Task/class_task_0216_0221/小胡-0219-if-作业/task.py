#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: task.py
  @time: 2019/02/19
  
  """
# 第1题：
# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
# score=input("请输入你的成绩：")
# if score.isdigit():
#     score=int(score)
#     if score>100 and score<0:
#         print('数据范围在0-100之间')
#     elif score>80:
#         print('优秀')
#     elif score>70:
#         print('良好')
#     elif score>=60:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print('数据输入有误')

# 第2题:
# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# p=int(input('请输入购买金额：'))
# if 50<=p<=100:
#     print('我们会给10%的折扣')
#     print('最终价格为：{}'.format(p*0.9))
# elif p>100:
#     print('我们会给20%的折扣')
#     print('最终价格为：{}'.format(p*0.8))
# elif p<0:
#     print('输入的金额有误，请重新输入!')
# else:
#     print('不好意思，没有折扣')


# 浮点数怎么办？

# def discount(discount,min,max):



# 第3题：
# 3、输入一个数，判断一个数n能同时被3和5整除
#
# n=int(input("请输入一个整数："))
# if n%3==0 and n%5==0:
#     print(n,'可以同时被3和5整除')
# else:
#     print(n,'不能同时被3和5整除')



# 第4题

# 4、输入一个年份，输出是否为闰年，闰年条件：
# 能被4整除但不能被100整除，或者能被400整除的年份都是闰年
# y = input('请输入年份：')
# if len(y)==4:
#     y=int(y)
#     if ((y%4==0 and y%100!=0) or (y%400 == 0)):
#         print(y,'是闰年')
#     else:
#         print(y,'不是闰年')
# else:
#     print("请输入正确的年份！")



# 第5题
# 5、一个 5 位数，判断它是不是回文数。
# 即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。01210
y = input('请输入数字：')
if len(y)==5 and y.isdigit():
    if y[0]!='0':
        if y[0]==y[4] and y[1]==y[3]:
            print('{}是一个回文数'.format(y))
    else:
        print('数据输入有误')
else:
    print('请输入一个5位数')



y = input('请输入数字：')
if len(y) == 5 and y[0] != '0':
    if y[0]==y[4] and y[1] == y[3]:
        print(y,'是回文数')
    else:
        print(y,'不是回文数')
else:
    print('请输入合法数字')


# x=input("请输入任意位数的数字：")
# if len(x)==5 and  x==x[::-1]:
#     if x[0]=='0':
#         print('{}不是回文数'.format(x))
#     else:
#      print('{}是回文数'.format(x))
# else:
#     print('{}不是回文数'.format(x))




# 第6题
# 6、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，
# 来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal
#
# import random
# a=int(input("请输入一个数字："))
# d=random.randint(1,9)
# print(d)
# if a==d:
#     print('equal')
# elif a>d:
#     print('bigger')
# else:
#     print('less')



# 扩展题：
# 登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}字典中，
# 通过控制台输入用户名和密码判读是否正确，
# 然后给出对应的提示消息：登录成功 OR 用户名或密码错误
d={'name':'huahua','pwd':'123456'}
userName=input("请输入用户名：")
if userName in d.values():
    passWord = input("请输入密码：")
    if passWord in d.values():
            print("登陆成功")
    else:
            print("密码错误")
else:
    print("用户名错误")

# 设计一个登陆程序，用户名和密码存在于字典当中，
# # 首先输入用户名，如果用户名不存在或者为空，则一直提示需要输入正确的用户名
# # 当用户名正确的时候，提示要输入密码，如果密码和用户名不对应，提示密码错误需要重新输入
# # 如果密码错误超过3次，则中断程序
# # 当输入密码错误时，提示还有几次机会
# # 用户名和密码都输入正确的时候，提示登录成功
# d={'admin':'lemon','huahua':'123456'}
# while True:
#     name=input("请输入用户名：")
#     if name in d.keys():
#         count = 0
#         while count<3:
#             pwd=input("请输入密码：")
#             if pwd in d.values():
#                 print("登录成功！")
#                 break
#             else:
#                 count+=1
#                 print("密码错误，请重新输入！,还有{}次机会".format(3-count))
#     else:
#         print("请输入正确的用户名！")
#         continue
#     break
#
#




#
# 输入num为四位数 对其按照如下的规则进行加密：
# 每一位分别加5，然后分别对其替换为该数除以10取余后的结果
# 将该数的第1位和第4位互换，第二位和第三位互换
# 最后合起来作为加密后的整数输出   作为字符串输出



