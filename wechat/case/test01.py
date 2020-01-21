from wechat.common.call_statend import TestCase
from wechat.common.call_common import Login
from wechat.operation.locate_page.call_locate_page import Locate
import pytest


class TestLcation(TestCase):

    def test_01(self):
        num = Locate(self.driver)
        num.call_use_locate()
        num.call_locate(0)
        h = "hello!"
        assert 'h' not in h

    def test_02(self):
        y = 123
        assert 2 == y


if __name__ == "__main__":
    pytest.main(["-s", "test01.py"])
