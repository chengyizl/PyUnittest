import unittest

from test_unittest.test1 import IntegerArithmeticTestCase


suite = unittest.TestSuite()

# IntegerArithmeticTestCase下的测试用例
cases =  [IntegerArithmeticTestCase('testAdd'),IntegerArithmeticTestCase('testMultiply')]

# 往套件里添加测试用例
suite.addTests(cases)

with open('../report/demo.txt', 'w', encoding='utf-8') as f:
        # 初始化runner  runner可以理解为运行器
        runner = unittest.TextTestRunner(f)

        runner.run(suite)