from common.call_wechat import wechat
import pytest


@pytest.fixture(scope="session")
def setup_class():
    print('用例执行前')
    wechat()


def teardown_class(self):
    print('用例执行后')
    self.driver.close_app()


@pytest.fixture(scope="session")
def login():
    print("登录操作")



