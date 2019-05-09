#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: var.py
  @time: 2019/02/26
  
  """
#全局变量
#局部变量
#北京都是晴天 除了朝阳区是雨天
#全局变量：晴天
#局部变量：雨天


#全局变量生效的范围大于局部变量
#当局部变量存在的时候，优先取局部变量


#python里面的全局和局部
#函数外的是全局变量
#函数内的是 局部变量   只能作用于函数里面

# offer=20#全局变量  存最高offer
#
# def student_info(class_name,name):
#     offer=20#局部变量 在函数内部
#     print("{}期的{}同学拿到了{}k的offer"
#           .format(class_name,name,offer))
#
# def student_record():
#     print('目前柠檬班的最高薪资是{}'.format(offer))
#
#
# student_info('15','不期而遇')
# student_record()


#当全局变量和局部变量同时存在的时候，优先取决于局部变量








offer=1#全局变量  存最高offer

def student_info(class_name,name):#A 调用A函数的时候，才会改变变量的值
    global  offer#声明为全局变量
    offer=20#局部变量  在函数内部
    print("{}期的{}同学拿到了{}k的offer"
          .format(class_name,name,offer))
    offer+=2

def student_record():
    print('目前柠檬班的最高薪资是{}'.format(offer))

student_info('15','不期而遇')
print(offer)
student_record()
# student_info('15','不期而遇')


#global 全局变量
#使用场景：两个请求同时用了一个变量