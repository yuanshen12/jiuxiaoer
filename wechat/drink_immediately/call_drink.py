from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_common import Login
from common.call_wechat import wechat
from wechat.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class Drink(Login):
    call_mix = (By.CLASS_NAME, "mix-parent")  # 马上喝页面标题
    call_parent = (By.XPATH, "/html/body/nav[2]/ul/li[1]/ul/li[{}]")  # 马上喝酒类选择
    call_rank = (By.XPATH, "/html/body/nav[2]/ul/li[2]/ul/li[{}]")  # 马上喝综合排序的排序
    call_screen = (By.XPATH, "//*[@id='doc-mix-offcanvas']/aside[1]/div/article[{}]/aside[2]/div[{}]")  # 马上喝页面筛选的品牌选择
    call_ensure = (By.CLASS_NAME, "mix-u-sm-6")  # 马上喝页面筛选的确定和重置
    call_search = (By.CLASS_NAME, "search-btn")  # 马上喝页面搜索功能
    call_item = (By.CLASS_NAME, "tab-item")  # 马上喝页面全部，促销，等按钮
    call_tab = (By.CLASS_NAME, "tab-search")  # 马上喝页面点开全部按钮
    call_img = (By.CLASS_NAME, "img")  # 马上喝页面商品图片
    call_title = (By.CLASS_NAME, "goods-title")  # 马上喝页面商品标题
    call_price = (By.CLASS_NAME, "goods-price")  # 马上喝页面商品价格
    call_add = (By.CLASS_NAME, "cart-add")  # 马上喝页面商品加号
    call_cart = (By.CLASS_NAME, "icon-shopping_cart")  # 马上喝页面购物车
    call_content = (By.CLASS_NAME, "content-right")  # 马上喝页面去结算

    def __init__(self, driver):
        super().__init__(driver)
        self.login()
        Home(driver).home_menu(2)

    def drink_mix(self, num):  # 马上喝页面标题(0,1,2）
        self.wait(EC.presence_of_all_elements_located, self.call_mix)[num].click()

    def drink_parent(self, num):  # 马上喝页面酒类选择(1,2,3……）
        self.drink_mix(0)
        self.wait(EC.presence_of_element_located, self.amend(self.call_parent, num)).click()

    def drink_rank(self, num):  # 马上喝页面排序选择(1,2……）
        self.drink_mix(1)
        self.wait(EC.presence_of_element_located, self.amend(self.call_rank, num)).click()

    def drink_screen(self, stat=1,  three=2):  # 马上喝筛选（stat选择类型1品牌，2价格，three选择第几个）
        self.drink_mix(2)
        while True:
            try:
                self.wait(EC.element_to_be_clickable, self.amends(self.call_screen, stat, three)).click()
            except:
                self.swipe(600, 1200, 600, 600, 500)
                continue
            else:
                break

    def drink_ensure(self, num=0):  # 马上喝筛选页面的重置和确定
        self.drink_screen()
        self.wait(EC.presence_of_all_elements_located, self.call_ensure)[num].click()

    def drink_search(self):  # 马上喝页面点开搜索
        self.wait(EC.element_to_be_clickable, self.call_search).click()

    def drink_item(self, num):  # 马上喝页面促销
        self.wait(EC.presence_of_all_elements_located, self.call_item)[num].click()


if __name__ == "__main__":
    driver = wechat()
    name = Drink(driver)
    name.drink_item(1)