from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from wechat.home.call_home import Home


class Indent(Login):

    call_menu = (By.CLASS_NAME, "menu-li")  # 订单页面状态选择
    call_title = (By.CLASS_NAME, "title")  # 订单页面订单标题（站点，时间，状态）
    call_main = (By.CLASS_NAME, "main-text")  # 订单页面订单商品标题
    call_number = (By.CLASS_NAME, "number")  # 订单页面实付价格
    call_del = (By.CLASS_NAME, "passiv-style")  # 订单页面删除功能（评价晒单）
    call_buy = (By.CLASS_NAME, "buy-again")  # 订单页面再次购买
    call_btn = (By.CLASS_NAME, "btn")  # 订单页面立即下单

    def indent_menu(self):
        self.login()
        Home(driver).home_menu(3)
        self.wait(EC.presence_of_all_elements_located, self.call_menu).click()


if __name__ == "__main__":
    driver = wechat()
    name = Indent(driver)
    name.indent_menu()