import pytest
from common.call_wechat import wechat


@pytest.fixture()
def setup_class(self):
    print('用例执行前')
    self.driver = wechat()


def teardown_class(self):
    print('用例执行后')
    self.driver.close_app()

