# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 类与对象.py

#手机类
#属性：
#方法：call message video
class Phone:

    #手机属性===>类属性
    # color='black'
    # price=4500
    # brand='oppo'
    # size='5.5'

    #参数化-魔法方法--初始化方法
    def __init__(self,color,price,brand,size=5):#我们是调用这个方法
        self.color=color#颜色
        self.price=price#价格
        self.brand=brand#品牌
        self.size=size#尺寸

    # def __int__(self):#这是错的！！！！！

    #方法
    @classmethod
    def call(cls,tel_no):#打电话  类方法
        # print(cls.color)
        # print(cls.color)
        print('拨号：{}，开始打电话'.format(tel_no))

    def send_message(self,tel_no,content='早上好'):#发送短信  对象方法
        print('给{}，发送短信：{}'.format(tel_no,content))

    def watch_tv(self,*args):#看电视 *args 动态参数
        app=''
        for item in args:
            app+=item
            app+='、'
        print('可以利用这些APP看电视，比如说：{}'.format(app))

    def take_shoot(self):#拍照
        self.color
        print('拍照')

    @staticmethod
    def add(a,b):#加法
        #静态方法--->工具方法  他不会调用任何类里面方法或者是属性
        print(a+b)

    def phone_info(self):#打印手机的相关信息
        print('颜色：{}，品牌：{}，价格：{}，尺寸：{}'
              .format(self.color,self.brand,self.price,self.size))

if __name__ == '__main__':
    # t=Phone('red','2300','vivo',6.5)#color,price,brand,size
    # t.add(4,5)
    # t.take_shoot()
    # t.watch_tv('爱奇艺','优酷','腾讯视频')
    # t.send_message('13899090909','快点来上课，第一节课已经要完了！')
    # t.call('13899090909')
    # t.phone_info()

    Phone.call('15096090550')



