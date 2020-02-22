from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from wechat.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions


class Indent(Login):

    call_menu = (By.CLASS_NAME, "menu-li")  # 订单页面状态选择
    call_title = (By.CLASS_NAME, "title")  # 订单页面订单标题（站点，时间，状态）
    call_main = (By.CLASS_NAME, "main-text")  # 订单页面订单商品标题
    call_number = (By.CLASS_NAME, "number")  # 订单页面实付价格
    call_del = (By.CLASS_NAME, "passiv-style")  # 订单页面删除功能（评价晒单）
    call_del_sure = (By.XPATH, "/html/body/div[1]/div[7]/div/div[2]/button[{}]")  # 订单删除确定
    call_buy = (By.CLASS_NAME, "buy-again")  # 订单页面再次购买
    call_btn = (By.CLASS_NAME, "btn")  # 订单页面立即下单

    def __init__(self, driver):
        super().__init__(driver)
        self.login()
        Home(driver).home_menu(3)

    def indent_menu(self, num):  # 订单页面选择订单状态列表
        names = self.wait(EC.presence_of_all_elements_located, self.call_menu)[num]
        TouchActions(self.driver).tap(names).perform()

    def indent_title(self, num):  # 订单页面标题（站点，订单状态）
        while True:
            try:
                title = self.wait(EC.visibility_of_any_elements_located, self.call_title)[num]
            except:
                self.swipe(600, 1200, 600, 600, 500)
            else:
                return title

    def indent_main(self, num):  # 订单页面点开商品标题
        while True:
            try:
                self.wait(EC.presence_of_all_elements_located, self.call_main)[num].click()
                break
            except:
                self.swipe(600, 1200, 600, 600, 500)

    def indent_number(self, num):  # 订单页面商品价格
        while True:
            try:
                number = self.wait(EC.presence_of_all_elements_located, self.call_number)[num].text
            except:
                self.swipe(600, 1200, 600, 600, 500)
            else:
                return number

    def indent_del(self, num=0, two=1):  # 订单页面删除订单
        while True:
            try:
                self.wait(EC.visibility_of_all_elements_located, self.call_del)[num].click()
                if two == 1:  # 取消
                    names = self.wait(EC.element_to_be_clickable, self.amend(self.call_del_sure, two))
                elif two == 2:  # 确定
                    names = self.wait(EC.element_to_be_clickable, self.amend(self.call_del_sure, two))
            except:
                self.swipe(600, 1200, 600, 600, 500)
            else:
                return names

    def indent_buy(self, num=0):  # 订单页面再次购买
        while True:
            try:
                buy = self.wait(EC.presence_of_all_elements_located, self.call_buy)[num]
            except:
                self.swipe(600, 1200, 600, 600, 500)
            else:
                return buy.click()

    def indent_btn(self):  # 订单页面立即购买（返回首页）
        self.indent_menu(2)
        self.wait(EC.element_to_be_clickable, self.call_btn).click()


if __name__ == "__main__":
    driver = wechat()
    name = Indent(driver)
    name.indent_buy()