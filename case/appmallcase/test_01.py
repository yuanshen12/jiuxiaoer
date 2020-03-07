from app.locate.call_send_locate import SendLocate
from app.home.call_home import Home
from common.call_wechat import TestCase
import pytest
import allure


@allure.story("定位模块")
@pytest.mark.app
class TestLocate(TestCase):
    @allure.story('用例：1')
    @allure.title('用例：定位页面的当前地址切换到首页的地址相同')
    def test_01(self):
        locate = SendLocate(self.driver)
        home = Home(self.driver)
        locate_name = locate.send_locate_info_location().text
        locate.send_locate_info_location().click()
        home_location_name = home.home_locate().text
        assert locate_name == home_location_name

    @allure.story('用例：2')
    @allure.title('用例：首页进入定位页面操作新增地址')
    def test_02(self):
        locate = SendLocate(self.driver)
        assert locate.send_locate_add_location(women=1) is True

    @allure.story('用例：3')
    @allure.title('用例：首页进入定位页面使用地图模式操作切换地址')
    def test_03(self):
        locate = SendLocate(self.driver)
        home = Home(self.driver)
        locate_name = locate.send_locate_map_location().text
        locate.send_locate_map_location(names=1).click()
        home_location_name = home.home_locate().text
        assert locate_name == home_location_name

    @allure.story('用例：4')
    @allure.title('用例：首页进入定位页面操作切换附近地址')
    def test_04(self):
        locate = SendLocate(self.driver)
        home = Home(self.driver)
        locate_nearby_name = locate.send_locate_nearby(2).text
        locate.send_locate_nearby(2).click()
        home_locate_name = home.home_locate().text
        assert home_locate_name in locate_nearby_name

    @allure.story('用例5')
    @allure.title('用例：首页进入定位页面操作切换收货地址')
    def test_05(self):
        locate = SendLocate(self.driver)
        home = Home(self.driver)
        location_name = locate.send_locate_name(0).text
        locate.send_locate_name(0).click()
        home_locate_name = home.home_locate().text
        assert location_name == home_locate_name

    @allure.story('用例：6')
    @allure.title('用例：首页进入定位页面操作通过切换区域进行搜索地址')
    def test_06(self):
        locate = SendLocate(self.driver)
        home = Home(self.driver)
        locate_search_name = locate.send_locate_search().text
        locate.send_locate_search(search=1).click()
        home_locate_name = home.home_locate().text
        assert locate_search_name == home_locate_name


if __name__ == "__main__":
    pytest.main(['-s', '-q', 'test_11.py'])
