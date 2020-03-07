from common.call_wechat import wechat
from common.call_common import Login
from app.home.call_home import Home
from selenium.webdriver.common.by import By


class Search(Login):
    call_back = (By.ID, "com.callme.mall:id/back")  # 搜索页面返回
    call_content = (By.ID, "com.callme.mall:id/content")  # 搜索页面输入（包含热门搜索，历史记录）
    call_clean = (By.ID, "com.callme.mall:id/clean_history")  # 搜索页面删除历史
    call_number = (By.ID, "com.callme.mall:id/number")  # 购物车角标
    call_shopping_cart = (By.ID, "com.callme.mall:id/shoppingCart")  # 购物车
    call_money = (By.ID, "com.callme.mall:id/money")  # 所在购物车价钱
    call_settlement = (By.ID, "com.callme.mall:id/settlement")  # 去结算

    def __init__(self, driver):
        super().__init__(driver)
        Home(self.driver).home_seek()

    def search_back(self):  # 搜索页面返回
        self.driver.find_element(*self.call_back).click()

    def search_content(self, stat=0, num=0):  # 搜索页面输入(初始是输入框，从1开始点热门，历史搜索）
        content = self.driver.find_elements(*self.call_content)
        if stat == 0:
            content[num].send_keys(123)
        else:
            content[num].click()

    def search_clean(self):  # 搜索页面清空历史记录
        self.driver.find_element(*self.call_clean).click()

    def search_number(self):  # 购物车角标(可获得商品数量）
        self.driver.find_element(*self.call_number)

    def search_cart(self):  # 购物车
        self.driver.find_element(*self.call_shopping_cart).click()

    def search_money(self):  # 加入购物车金额
        names = self.driver.find_element(*self.call_money).text
        return names

    def search_settlement(self):
        self.driver.find_element(*self.call_settlement).click()


if __name__ == '__main__':
    driver = wechat()
    Search(driver).search_settlement()
