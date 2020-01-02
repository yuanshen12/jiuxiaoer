from wechat.common.call_statend import TestCase
from wechat.common.call_common import Login
import pytest


class TestLcation(TestCase):

    def test_01(self):
        h = "hello!"
        assert 'h' not in h

    def test_02(self):
        y = 123
        assert 2 == y


if __name__ == "__main__":
    pytest.main(["-s", "test01.py"])
