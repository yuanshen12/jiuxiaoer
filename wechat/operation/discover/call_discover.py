from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from wechat.common.call_wechat import wechat
from wechat.common.call_common import Login
from wechat.operation.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions


class Discover(Login):
    call_header = (By.CLASS_NAME, "menu-item")  # 发现页面标题
    call_img = (By.CLASS_NAME, "img-box")  # 发现页面商品图片
    call_title = (By.CLASS_NAME, "title")  # 发现页面商品标题
    call_sub_title = (By.CLASS_NAME, "sub-title")  # 发现页面商品小标题
    call_price = (By.CLASS_NAME, "price")  # 发现页面商品价格
    call_add = (By.CLASS_NAME, "buy-btn-jia-logo")  # 发现页面商品加号
    call_side = (By.CLASS_NAME, "middle-body")  # 发现页面商品反转点击

    def discover_title(self, num):  # 发现页面选择标题栏
        age = self.wait(EC.presence_of_all_elements_located, self.call_header)[num]
        TouchActions(self.driver).tap(age).perform()

    def discover_img(self, one):  # 发现页商品图片点击
        self.login()
        Home(driver).home_menu(1)
        names = self.wait(EC.presence_of_all_elements_located, self.call_img)[one]
        print(names.text)





if __name__ == "__main__":
    driver = wechat()
    name = Discover(driver)
    name.discover_img(1)
