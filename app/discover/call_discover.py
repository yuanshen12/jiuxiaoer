from selenium.webdriver.common.by import By
from common.call_wechat import wechat
from common.call_common import Login
from app.home.call_home import Home
from time import sleep


class Discover(Login):
    call_title = (By.ID, "com.callme.mall:id/titleText")  # 帮你挑标题
    call_tab_title = (By.ID, "com.callme.mall:id/tv_tab_title")  # 帮你挑标题切换
    call_img = (By.ID, "com.callme.mall:id/image")  # 帮你挑商品图片
    call_shopping_title = (By.ID, "com.callme.mall:id/text_title")  # 帮你挑商品标题
    call_tips = (By.ID, "com.callme.mall:id/text_tips1")  # 帮你挑商品小标题
    call_money = (By.ID, "com.callme.mall:id/price")  # 帮你挑商品价格
    call_add = (By.ID, "com.callme.mall:id/add")  # 帮你挑商品加入购物车

    def __init__(self, driver):
        super().__init__(driver)
        Home(self.driver).home(1).click()

    def discover_title(self):  # 帮你挑标题
        discover = self.driver.find_element(*self.call_title)
        return discover

    def discover_tab_title(self, num):  # 帮你挑标题切换
        sleep(5)
        self.driver.find_elements(*self.call_tab_title)[num].click()

    def discover_img(self, num):  # 帮你挑商品图片
        self.driver.find_elements(*self.call_img)[num].click()

    def discover_shopping_title(self, num):  # 帮你挑商品标题
        title = self.driver.find_elements(*self.call_shopping_title)[num]
        return title

    def discover_tips(self, num):  # 帮你挑商品小标题
        tips = self.driver.find_elements(*self.call_tips)[num]
        return tips

    def discover_money(self, num):  # 帮你挑商品价格
        money = self.driver.find_elements(*self.call_money)[num]
        return money

    def discover_add(self, num):  # 帮你挑商品添加到购物车
        self.driver.find_elements(*self.call_add)[num].click()


if __name__ == '__main__':
    driver = wechat()
    Discover(driver).discover_add(1)