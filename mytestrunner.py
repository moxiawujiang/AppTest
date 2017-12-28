__author__ = '芜疆'
#encoding=utf-8
import unittestdemo
import  unittest


# mysuite=unittest.TestSuite()
#单个添加
# mysuite.addTest(unittestdemo.MyTestCase("test_login_failed"))
# mysuite.addTest(unittestdemo.MyTestCase("test_login_and_logout"))

#以整个类添加case
case=unittest.TestLoader().loadTestsFromTestCase(unittestdemo.MyTestCase)

#可以数组形式添加 ([case],[case1])多个suite
mysuite=unittest.TestSuite(case)

myrunner=unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)