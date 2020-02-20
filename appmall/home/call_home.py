from selenium.webdriver.common.by import By
from common.call_common import wechat
from common.call_common import App
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class Home(App):
    call_locate = (By.ID, "com.callme.mall:id/ll_loc")  # 首页定位
    call_seek = (By.ID, "com.callme.mall:id/et_search")  # 首页搜索
    call_carousel = (By.CLASS_NAME, "android.widget.ImageView")  # 首页轮播图
    call_handpick = (By.CLASS_NAME, "android.widget.LinearLayout")  # 首页酒类
    call_hours = (By.ID, "com.callme.mall:id/tv_business_hours")  # 首页营业通知
    call_hour = (By.ID, "com.callme.mall:id/tv_announce_info")  # 首页通知
    call_activity = (By.CLASS_NAME, "android.view.View")  # 首页活动
    call_handpicks = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab")  # 首页酒类二
    call_class = (By.CLASS_NAME, "android.widget.TextView")  # 首页酒类筛选
    call_title = (By.ID, "com.callme.mall:id/tv_title")  # 首页商品标题
    call_tag = (By.CLASS_NAME, "android.widget.LinearLayout")  # 首页商品价格
    call_img = (By.ID, "com.callme.mall:id/iv_wine")  # 首页商品图片
    call_add = (By.ID, "com.callme.mall:id/iv_add")  # 首页商品购物车
    call_cart = (By.ID, "com.callme.mall:id/rl_cart")  # 首页购物车
    call_more = (By.ID, "com.callme.mall:id/seeMore")  # 首页查看更多

    def __init__(self, driver):
        super().__init__(driver)
        App.ad(self)


    def home_locate(self):  # 首页定位
        self.wait(EC.presence_of_element_located, self.call_locate).click()

    def home_seek(self):  # 首页搜索
        self.wait(EC.presence_of_element_located, self.call_seek).click()

    def home_carousel(self, num):  # 首页轮播图
        while True:
            try:
                self.wait(EC.presence_of_all_elements_located, self.call_carousel)[num].click()
                break
            except:
                pass

    def home_handpick(self, num):  # 首页酒类
        self.wait(EC.presence_of_all_elements_located, self.call_handpick)[num].click()

    def home_hours(self):  # 首页营业通知
        hours = self.wait(EC.presence_of_element_located, self.call_hours).text
        return hours

    def home_hour(self):  # 首页通知
        hour = self.wait(EC.presence_of_element_located, self.call_hour)
        return hour

    def home_activity(self, num):  # 首页活动
        self.swipe(600, 1200, 600, 800, 500)
        self.wait(EC.presence_of_all_elements_located, self.call_activity)[num].click()

    def home_handpicks(self, num):  # 首页酒类2
        self.swipe(500, 1200, 500, 500, 500)
        self.wait(EC.presence_of_all_elements_located, self.call_handpicks)[num].click()

    def home_class(self, num):  # 首页酒类筛选
        self.swipe(500, 1200, 500, 500, 500)
        self.wait(EC.presence_of_all_elements_located, self.call_class)[num].click()

    def home_title(self, num):  # 首页商品标题
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_title)[num].click()
                break
            except:
                pass

    def home_tag(self, num):  # 首页商品价格
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                names = self.wait(EC.presence_of_all_elements_located, self.call_tag)[num].text
                return names
            except:
                pass

    def home_img(self, num):  # 首页商品图片
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_img)[num].click()
                break
            except:
                pass

    def home_carts(self, num):  # 首页商品购物车
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                sleep(5)
                self.wait(EC.presence_of_all_elements_located, self.call_add)[num].click()
                break
            except:
                pass

    def home_cart(self):  # 首页购物车
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                self.wait(EC.element_to_be_clickable, self.call_cart).click()
                break
            except:
                pass

    def home_more(self):  # 首页查看更多
        while True:
            try:
                self.swipe(500, 800, 500, 500, 500)
                self.wait(EC.element_to_be_clickable, self.call_more).click()
                break
            except:
                pass


if __name__ == "__main__":
    driver = wechat()
    name = Home(driver)
    name.home_cart()
