from app.search.call_send_search_shoppiing import SendSearch
from app.home.call_home import Home
from common.call_wechat import TestCase
import pytest
import allure


@allure.story('搜索模块')
@pytest.mark.app
class TestSearch(TestCase):
    @allure.title('用例：首页进入搜索商品是否正常')
    def test_07(self):
        search = SendSearch(self.driver)
        send_search = search.send_search()
        send_search_text = send_search().text
        assert send_search_text is None


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_02.py'])
