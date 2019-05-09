#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: study_reflect.py
  @time: 2019/04/27
  
  """


class People:

    number_eye = 2

    def __init__(self,name,age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = People('xiaohu',26)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)



    #添加属性
    print(hasattr(People,"number_leg"))
    #如果有属性就返回True，没有就返回False
    print(hasattr(People, "number_eye"))

    setattr(People,"number_leg",2)
    print(hasattr(People, "number_leg"))
    print(People.number_leg)
    setattr(p,"name","monngo")
    print(getattr(p,"name"))

    setattr(p,"dance",True)#实例属性
    print(p.dance)


    #获取属性
    getattr(People,"number_leg")#获取类属性
    getattr(p,"dance")#获取实例属性


    #删除属性
    delattr(p,"dance")#删除
    getattr(p,"dance")#获取实例属性

