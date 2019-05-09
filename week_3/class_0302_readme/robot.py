#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: robot.py
  @time: 2019/03/02
  
  """

def robot(name,msg):
    print("{}你有一条信息：{}".format(name,msg))

#测试代码
if __name__ == '__main__':#代码执行的主入口
    robot('001','今天一起吃晚饭吗？')#调用函数

if __name__ == '__main__':
    robot('003','我们一起哈哈哈吧！')