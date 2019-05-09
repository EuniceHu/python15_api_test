#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: learn_test_suite.py
  @time: 2019/03/22
  
  """
import unittest
import HTMLTestRunnerNew
#suite 存储测试用例的套件

#先创建TestSuite类的对象TestSuite()

suite=unittest.TestSuite()

#第一种方法 一个一个的去添加用例

# from week_6.class_0321_readme.learn_unittest_one import *
# suite.addTest(TestAdd('test_001'))
# suite.addTest(TestAdd('test_002'))
# suite.addTest(TestSub('test_001'))
# suite.addTest(TestSub('test_002'))


#第二种方法 通过Loader来加载用例  通过模块名来加载用例

# from week_6.class_0321_readme import learn_unittest_one#模块名
# loader=unittest.TestLoader()#创建TestLoader的对象TestLoader()
# suite.addTest(loader.loadTestsFromModule(learn_unittest_one))

#第三种 通过loader来加载用例  通过测试类名来加载用例
from week_6.class_0321_readme.learn_unittest_one import *
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))
suite.addTest(loader.loadTestsFromTestCase(TestSub))


#执行用例
# runner=unittest.TextTestRunner()#创建一个对象来执行用例
# runner.run(suite)

#执行用例----unittest版本
# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)
#     runner.run(suite)

#执行用例  执行并生成Html测试报告---HTMLTestRunnerNew
with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190324py15测试报告',
        description='这是关于加法和减法功能验证的报告',
        tester='胡小胡')
    runner.run(suite)

#. 通过了一条用例
#E 代码出错
#F 用例执行失败


#总结 调用测试类的时候，一定要先创建对象之后，才能调用
"""
第一步：先导入 import  unittest  导入要测试的方法类
第二步：编写测试用例类，一定要继承unittest.TestCase类
第三步：编写测试用例，一定要用test开头，不然执行不出来
第四步：在测试用例里面，编写期望值，实际值，实际值是导入的方法类，
一定要在类名后面加()创建对象，传参数，之后用assert断言
第五步：新建模块，使用suite存储用例，先导入import unittest
第六步：创建个TestSuite类的对象TestSuite(),创建对象，才能调用方法
第七步：有三种方法来加载用例
1：一个一个加，导入所有测试类，用TestSuite()调用addTest()方法
2：使用Loader来加载，导入模块，创建个TestLoader类的对象TestLoader(),来调用LoadTestsFromModule方法
3：使用Loader来加载，导入所有测试类，创建个TestLoader类的对象TestLoader(),来调用loadTestsFromTestCase方法
第八步：执行用例，首先要创建个TextTestRunner类的对象TextTestRunner()
用TextTestRunner()调用run方法使用Suite
TextTestRunner().run(Suite)

"""