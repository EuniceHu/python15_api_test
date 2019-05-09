# encoding: utf-8 
"""
@author: 凹凸曼
@number: 1526
@file: homework_0324.py
@time: 2019/3/24 19:23
"""
import unittest,HTMLTestRunner
from week_6 import homework_0323

"""#suite是用来存储用例的容器
执行完成后的代码标识：. 用例通过    E 该用例代码有问题    F 用例失败"""
suite=unittest.TestSuite()

loader=unittest.TestLoader()          #用例加载器
suite.addTest(loader.loadTestsFromModule(homework_0323))

# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)
#     runner.run(suite)

#"wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，先清空，再打开文件
with open('test.html','wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(       #调用HTMLTestRunner生成测试报告
        stream=file,
        verbosity=2,        #设置测试报告级别为2，共三个级别0,1,2  数字越大测试报告的信息越详细
        title='http登录接口测试报告',       #测试报告名称
        tester='antiman')                   #测试人员
    runner.run(suite)

