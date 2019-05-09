#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Path_to_dealwith.py
  @time: 2019/02/28
  
  """
#相对路径  绝对路径
# D:\Python_15\作业\小胡-0221-循环作业\xunhuan.py  绝对路径
# open()#打开一个文件
#相对路径
# file=open('python15.txt')#参照物是文件本身
# print(file.read())
#当把python15.txt移动到week_3的文件夹下，报下面这个错误
# FileNotFoundError: [Errno 2] No such file or directory: 'python15.txt'
#当把python15.txt移动到python_15的文件夹下，相对于path_to_dealwith文件本身
#往上找一级是class_0228 ../ 再往上找一级是week_3 ../，python15.txt与week_3是平级
# 所以file=open('../../python15.txt')就找到了

#绝对路径
#\t \n \r ----转义 r R 或者是加\
# file=open(r'D:\Python_15\week_3\class_0228\test15.txt')
# print(file.read())

# 路径处理
import  os#导入os模块
# path_1=os.getcwd()#获取当前路径 不会具体到模块名
# # path_2=os.path.realpath(__file__)#__file__指的是当前文件本身
# path_2=os.path.realpath(__file__)
# # os.path.relpath()
# path_3=os.path.basename(__file__)#__file__指的是当前文件本身
# print('path_1:',path_1)
# print('path_2:',path_2)
# print('path_3:',path_3)
# print(__file__)#获取文件本身的路径
# D:/Python_15/week_3/class_0228/Path_to_dealwith.py
# path_1: D:\Python_15\week_3\class_0228
# path_2: D:\Python_15\week_3\class_0228\Path_to_dealwith.py
# path_3: Path_to_dealwith.py

#创建一个文件夹
# res=os.path.split(path_2)
# print(res)
# os.path.realpath(__file__)
path_2=os.path.realpath(__file__)
print('path_2:',path_2)
# 可以对路径进行切割 os.path.split(path) path是路径字符串

res=os.path.split(path_2)#对路径进行处理，返回的是元祖的类型数据
#split只会切割一层 根据\来切割
print(res)
# ('D:\\Python_15\\week_3\\class_0228', 'Path_to_dealwith.py')
# os.mkdir(path) path是路径字符串 新建一个文件夹
# os.mkdir(res[0]+'\python15')#拼接路径字符串

# 拼接路径
new_path=os.path.join(res[0],'python15','python_A')#join只是用来拼接路径，注意层级
os.mkdir(new_path)#新建 只能一级一级的去建立






#创建一个文件夹
# os.mkdir(os.path.join(os.path.split(path_2)[0],'test'))
# os.mkdir(os.path.join(os.path.split(os.path.realpath(__file__))[0],'test'))