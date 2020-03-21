from app.search.call_send_search_shoppiing import SendSearch
from common.call_common_app import config_yaml
from common.call_wechat import TestCase
import pytest
import allure


@allure.story('搜索模块')
@pytest.mark.app
class TestSearch(TestCase):
    @pytest.mark.smoking
    @allure.title('用例7：首页进入搜索商品是否正常')
    def test_07(self):
        data = config_yaml()
        search = SendSearch(self.driver)
        search.send_search_start()
        send_search = search.send_search().text
        assert data['search'] in send_search

    @allure.title('用例8：搜索页面立即购买')
    @pytest.mark.smoking
    def test_08(self):
        shopping = SendSearch(self.driver)
        shopping.send_shopping_submit()
        go_text = shopping.send_shopping_go().text
        assert go_text is not None

    @allure.title('用例9：搜索页面加入购物车购买')
    @pytest.mark.smoking
    def test_09(self):
        shopping = SendSearch(self.driver)
        shopping.send_shopping_cart()
        shopping_go_text = shopping.send_shopping_go().text
        assert shopping_go_text is not None


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_02.py'])
