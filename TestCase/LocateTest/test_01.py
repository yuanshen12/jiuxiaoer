import pytest
from Base.BaseRunner import TestCase
import allure
from PageOject.Location.location import Location
from PageOject.Search.search import Search
from PageOject.Settle.settle import Settle


@allure.story("定位模块")
@pytest.mark.app
class TestLocate(TestCase):

    @pytest.mark.smoking
    @allure.title("用例:微信支付")
    def test_01(self):
        locate = Location(self.driver).location_switchover()
        search = Search(self.driver).search_page()
        settle = Settle(self.driver).get_settle()
        assert locate and search and settle is True

    @pytest.mark.smoking
    @allure.title("用例：支付宝支付")
    def test_02(self):
        pass


    @pytest.mark.smoking
    @allure.title("用例：付到付款")
    def test_03(self):
        pass


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_01.py"])