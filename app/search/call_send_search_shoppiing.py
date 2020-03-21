from selenium.common.exceptions import NoSuchElementException
from common.call_wechat import wechat
from app.search.call_search import Search
from app.search.call_search_shopping import SearchShopping
from app.home.call_home import Home
from app.locate.call_send_locate import SendLocate
from app.balance.call_send_balance import SendBalance
from common.call_common_app import config_yaml


class SendSearch(Search):

    def __init__(self, driver):
        super().__init__(driver)

    def send_search_start(self):
        search = SendLocate(self.driver)
        search.send_locate_search().click()
        home = Home(self.driver)
        home.home_seek().click()

    def send_search(self, num=0):  # 输入商品
        if num == 0:
            self.search_content()
        self.search_content_name().click()
        shopping = SearchShopping(self.driver)
        shopping_text = shopping.search_shopping_title()
        return shopping_text

    def send_shopping_submit(self):  # 立即购买
        shopping = SearchShopping(self.driver)
        shopping.search_shopping_add().click()
        shopping.search_shopping_submit().click()
        balance = SendBalance(self.driver)
        balance.send_balance_ok()
        balance.send_balance_locate()
        balance.send_balance_submit()

    def send_shopping_go(self):  # 继续逛逛
        balance = SendBalance(self.driver)
        go = balance.send_balance_go()
        return go

    def send_shopping_cart(self):  # 加入购物车结算
        self.send_shopping_go().click()
        shopping = SearchShopping(self.driver)
        shopping.search_shopping_add().click()
        shopping.search_shopping_submit_cart().click()
        search = SendSearch(self.driver)
        search.search_settlement().click()
        balance = SendBalance(self.driver)
        balance.send_balance_ok()
        balance.send_balance_locate()
        balance.send_balance_submit()


if __name__ == '__main__':
    driver = wechat()
    name = SendSearch(driver)
    name.send_shopping_submit()
