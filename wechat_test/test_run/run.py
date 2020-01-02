import unittest
from  HTMLTestRunner_CN import HTMLTestRunner
import time,logging
import sys
path='D:\\wechat_sum\\'
sys.path.append(path)

test_dir='../test_case'
report_dir='../reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='商城自动化',description='商城自动化测试报告',verbosity=2,retry=2,save_last_try=False)
    logging.info('start run test case...')
    runner.run(discover)