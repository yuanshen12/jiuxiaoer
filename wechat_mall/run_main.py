import sys
print(sys.path)
import os
os.chdir('C:\\Users\\Administrator\\PycharmProjects\\jiuxiaoer')
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\jiuxiaoer')

import unittest
import HTMLTestRunner
from wechat_mall.common.mail import mail

def add_case(case_path=('C:\\Users\\Administrator\\PycharmProjects\\jiuxiaoer\\wechat_mall\\test_case'),rule=("test_*.py")):
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover

if __name__ == '__main__':
    fp = open('C:\\Users\\Administrator\\PycharmProjects\\jiuxiaoer\\wechat_mall\\report\\result.html', "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                    title=u'正式商城测试报告：',
                    description=u'用例执行情况：')
    runner.run(add_case())
    mail()



#  正式启用，有测试报告时间等

'''
path = 'C:\\Users\\Administrator\\PycharmProjects\\jiuxiaoer\\wechat_mall'
sys.path.append(path)

test_dir = './test_case'
test_report = '../wechat_mall/report'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = test_report + '/' + now + 'test_report.html'

if __name__ == '__main__':
    with open(report_name,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='APP Test Report',description='APP test report')
        logging.info('start run test case...')
        runner.run(discover)
        mail()
'''