from app.locate.call_send_locate import SendLocate
from common.call_statend import TestCase
from common.call_common import Login
import pytest


class TestHome(TestCase):

    def test_1(self):  # 定位搜索切换区域
        locate = SendLocate(self.driver)
        assert locate.send_locate_info() is True

    def test_2(self):  # 定位切换地图模式
        locate = SendLocate(self.driver)
        maps = locate.send_locate_map()
        assert maps is True

    def test_3(self):  # 定位收货地址切换
        locate = SendLocate(self.driver)
        locate.send_locate_name()

    def test_4(self):  # 定位附近地址
        locate = SendLocate(self.driver)
        name = locate.send_locate_nearby()
        assert name.text is not None

    def test_5(self):  # 定位新增地址
        locate = SendLocate(self.driver)
        name = locate.send_locate_add()
        assert name is True

    def test_9(self):  # 定位搜索地图模式
        data = Login.get_data(1)
        locate = SendLocate(self.driver)
        name = locate.send_locate_sure()
        assert data[1] in name.text


if __name__ == "__main__":
    pytest.main(['-s', '-q', 'test_01.py'])