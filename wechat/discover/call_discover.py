from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from wechat.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions


class Discover(Login):
    call_header = (By.CLASS_NAME, "menu-item")  # 发现页面标题
    call_img = (By.CLASS_NAME, "img-box")  # 发现页面商品图片
    call_title = (By.CLASS_NAME, "title")  # 发现页面商品标题
    call_sub_title = (By.CLASS_NAME, "sub-title")  # 发现页面商品小标题
    call_price = (By.CLASS_NAME, "price")  # 发现页面商品价格
    call_add = (By.CLASS_NAME, "buy-btn-jia-logo")  # 发现页面商品加号
    call_side = (By.CLASS_NAME, "middle-body")  # 发现页面商品反转点击
    call_cart = (By.CLASS_NAME, "float_cart")  # 发现页面点开购物车

    def __init__(self, driver):
        super().__init__(driver)
        self.login()
        Home(driver).home_menu(1)

    def discover_title(self, num):  # 发现页面选择标题栏
        age = self.wait(EC.presence_of_all_elements_located, self.call_header)[num]
        TouchActions(self.driver).tap(age).perform()

    # 发现页面点击或者返回（stat选择打开位置，img点开图片，title点开标题,sub点开小标题,price返回价格）
    def discover_item(self, stat=0, img=0, title=1, sub=0, price=0):
        if stat == 0:  # 选择点击图片
            while True:
                try:
                    self.wait(EC.presence_of_all_elements_located, self.call_img)[img].click()
                    self.swipe(600, 1200, 600, 600, 500)
                    break
                except:
                    pass
        if stat == 1:  # 选择点开标题
            while True:
                try:
                    self.wait(EC.presence_of_all_elements_located, self.call_title)[title].click()
                    self.swipe(600, 1200, 600, 600, 500)
                    break
                except:
                    pass
        else:
            if stat == 2:  # 选择点开小标题
                while True:
                    try:
                        self.wait(EC.presence_of_all_elements_located, self.call_sub_title)[sub].click()
                        self.swipe(600, 1200, 600, 600, 500)
                        break
                    except:
                        pass
            elif stat == 3:  # 选择返回价格
                while True:
                    try:
                        prices = self.wait(EC.presence_of_all_elements_located, self.call_price)[price].text
                        self.swipe(600, 1200, 600, 600, 500)
                        return prices
                    except:
                        pass
            else:
                self.wait(EC.element_to_be_clickable, self.call_add).click()

    def discover_cart(self):  # 发现页面点开购物车
        self.login()
        Home(driver).home_menu(1)
        self.wait(EC.element_to_be_clickable, self.call_cart).click()


if __name__ == "__main__":
    driver = wechat()
    name = Discover(driver)
    name.discover_item(2)
