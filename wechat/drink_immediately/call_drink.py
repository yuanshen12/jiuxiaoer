from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_common import Login
from common.call_wechat import wechat
from wechat.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions


class Drink(Login):
    call_mix = (By.CLASS_NAME, "mix-parent")  # 马上喝页面酒类显示
    call_parent = (By.XPATH, "/html/body/nav[2]/ul/li[1]/ul/li[1]")  # 马上喝酒类第一项
    call_rank = (By.CLASS_NAME, "/html/body/nav[2]/ul/li[2]/ul/li[1]")  # 马上喝综合排序的排序
    call_attrib = (By.CLASS_NAME, "attrib-list")  # 马上喝页面筛选的品牌选择
    call_search = (By.CLASS_NAME, "search-btn")  # 马上喝页面搜索功能
    call_item = (By.CLASS_NAME, "tab-item")  # 马上喝页面全部，促销，等按钮
    call_tab = (By.CLASS_NAME, "tab-search")  # 马上喝页面点开全部按钮
    call_img = (By.CLASS_NAME, "img")  # 马上喝页面商品图片
    call_title = (By.CLASS_NAME, "goods-title")  # 马上喝页面商品标题
    call_price = (By.CLASS_NAME, "goods-price")  # 马上喝页面商品价格
    call_add = (By.CLASS_NAME, "cart-add")  # 马上喝页面商品加号
    call_cart = (By.CLASS_NAME, "icon-shopping_cart")  # 马上喝页面购物车
    call_content = (By.CLASS_NAME, "content-right")  # 马上喝页面去结算

    def drink_mix(self, num):  # 马上喝页面酒类点开
        self.wait(EC.presence_of_all_elements_located, self.call_mix)[num].click()

    def drink_parent(self):  # 马上喝页面酒类选择
        self.login()
        Home(driver).home_menu(2)
        self.drink_mix(0)
        parent = self.call_parent
        self.wait(EC.presence_of_element_located, parent).click()

    def drink_rank(self):  # 马上喝页面排序
        self.login()
        Home(driver).home_menu(2)
        self.drink_mix(1)
        rank = self.call_rank
        self.wait(EC.presence_of_element_located, rank).click()


if __name__ == "__main__":
    driver = wechat()
    name = Drink(driver)
    name.drink_parent()