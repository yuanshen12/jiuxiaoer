from HTMLTestRunner_CN import HTMLTestRunner
import unittest
import time
import sys,os

case = os.path.abspath('../wechat/case')
report = os.path.abspath('../report')
print(case, report)
sys.path.append(case)

discover = unittest.defaultTestLoader.discover(case, pattern="test01.py")

now = time.strftime("%Y-%m-%d")
report_name = report + '/' + now + 'report.html'

with open(report_name, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title='自动化测试', description='商城自动化测试报告', verbosity=2, retry=2, save_last_try=False)
    runner.run(discover)