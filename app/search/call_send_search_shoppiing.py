from selenium.common.exceptions import NoSuchElementException
from common.call_wechat import wechat
from app.search.call_search import Search
from app.home.call_home import Home
from common.call_common_app import config_yaml


class SendSearch(Search):

    def __init__(self, driver):
        super().__init__(driver)
        home = Home(self.driver)
        home.home_seek().click()

    def send_search(self, num=0):  # 输入商品
        if num == 0:
            self.search_content()
        search = self.search_content_name()
        return search


if __name__ == '__main__':
    driver = wechat()
    name = SendSearch(driver)
    name.send_search()
