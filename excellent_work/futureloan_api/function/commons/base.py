# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-15 16:20
import os


class Base():

    @staticmethod
    def get_cur_path(file):
        '''获取当前文件路径'''
        return os.path.abspath(file)

    @staticmethod
    def get_cur_dir(file):
        return os.path.split(os.path.realpath(file))[0]


if __name__ == '__main__':

    path = Base.get_cur_path(__file__)
    path2 = Base.get_cur_dir(__file__)


    print(path)
    print(path2)
