from common.call_statend import TestCase
from wechat.home.call_home import Home
import pytest


class TestLcation(TestCase):

    def test_01(self):
        num = Home(self.driver)
        try:
            name = num.home_about()
        except:
            return False
        assert name == "123"

    def test_02(self):
        y = 123
        assert 2 == y


if __name__ == "__main__":
    pytest.main(["-s", "test01.py"])
