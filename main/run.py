import unittest
import os
from HTMLTestRunner import HTMLTestRunner
# 利用testloader加载测试用例
from test_unittest.testTaizhou import Test
from datetime import datetime


loader = unittest.TestLoader()
cases = loader.loadTestsFromTestCase(Test)

suite = unittest.TestSuite()
suite.addTests(cases)

def getNowtime():

    return datetime.now().strftime('%Y%m%d%H%M%S')

def getReport():
    start_dir = os.path.dirname(os.path.abspath(__file__))

    #获取报告目录
    report_dir = os.path.join(start_dir,'report')
    #判断目录是否存在
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    return os.path.join(report_dir,getNowtime() + '.html')

# D:\\IdeaProjects\\PyUnittest\\report\\report.html
with open(getReport(),'wb') as f:
    runner = HTMLTestRunner(stream=f,verbosity=2,title=u'接口测试报告',description=u'用例执行情况',tester=u'刘旺')
    runner.run(suite)