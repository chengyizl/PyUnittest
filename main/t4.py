import os
import unittest
from HTMLTestRunner import HTMLTestRunner
# 自动寻找测试用例并生成报告
# suite = unittest.TestSuite()

loader = unittest.TestLoader()

start_dir = os.path.dirname(os.path.abspath(__file__))

suite1 = loader.discover(start_dir)

with open('../report/demo.html', 'wb') as f:

    runner = HTMLTestRunner(stream=f,verbosity=2,title=u'接口测试报告',description=u'用例执行情况',tester=u'刘旺')
    runner.run(suite1)