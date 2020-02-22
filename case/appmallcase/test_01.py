from appmall.home.call_home import Home
from appmall.locate.call_locate import Locate
from common.call_statend import TestCase
from common.call_common import Login
import pytest


class TestHome(TestCase):

    def test_1(self):  # 定位搜索切换区域
        data = Login.get_data(1)
        locate = Locate(self.driver)
        home = Home(self.driver)
        home.home_locate().click()
        locate.locate_address()
        locate.locate_sure()
        assert data[1] in home.home_locate().text

    def test_2(self):  # 定位搜索地图模式
        locate = Locate(self.driver)


if __name__ == "__main__":
    pytest.main(['-s', '-q', 'test_01.py'])