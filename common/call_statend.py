import pytest,unittest
from wechat.common.call_wechat import wechat

#  启动微信并调用unittest


class TestCase:

    def setup_class(self):
        print('用例执行前')
        self.driver = wechat()

    def teardown_class(self):
        print('用例执行后')
        self.driver.close_app()




