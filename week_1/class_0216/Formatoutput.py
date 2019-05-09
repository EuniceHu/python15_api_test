#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Formatoutput.py
  @time: 2019/02/16
  
  """


#格式化输出
# name='hhh'
# age='22'#int str float
# sex='女'#0 女生 1 男生 注解
# salary='9000'#int str float
# hobby='游泳'
# height='170.45'#浮点数

#+字符串的拼接 + 只能针对同类型的数据 str(数字)--->字符串类型


print()#内置函数  *args-->arguments--->参数们  可以输入任意多个参数，用逗号隔开

name='hhh'
age=22#int str float
sex='女'#0 女生 1 男生 注解
salary='9000'#int str float
hobby='游泳'
height=170.45#浮点数

# 第一种格式化输出 %s %d %f 占坑  按顺序赋值 %s是万能的
# print('学生的名字叫：%s,他的薪资是：%s,她今年%d岁,他的身高是：%.2f'%(name,salary,age,height))
# print('学生的名字叫：'+name+'他的工资是：'+salary,'她今年',age,'岁')

#第二种格式化输出{} format 推荐使用
#1不标序号 按顺序赋值  按照format里面的变量 索引值
#2标序号 按序号给值

# print('学生的名字叫：{},他的薪资是：{},她今年{}岁,她的身高是：{}'.format(name,salary,age,height))

print("""
学生的名字叫：{0},
他的薪资是：{1},
她今年{2}岁,
她的身高是：{3}'
"""
.format(name,salary,age,height)
        # 0    1      2    3
)









# # 格式化输出 占坑符 %d %f %s
# age=22
# height=170.34
# hobby='打篮球'
#
# # 格式化输出方法一
# print('''---------小cc的个人档案-------------
#       年龄是：''',age,'''
#       身高是：''',height,'''
#       业余爱好是：''',hobby,'''
#       ''')
# print('''---------小cc的个人档案-------------
#       年龄是：%d
#       身高是：%0.2f
#       业余爱好是：%s
#       '''%(age,height,hobby))
# # 格式化输出方法二
# print('''---------Bay max的个人档案-------------
#       年龄是:{0}
#       身高是：{2}
#       业余爱好是：{0}
#       '''.format(age,height,hobby))#0开始编号坑 开始编号元素