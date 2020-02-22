from selenium.webdriver.common.by import By
from common.call_common import wechat
from common.call_common import App
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class Home(App):
    call_locate = (By.ID, "com.callme.mall:id/ll_loc")  # 首页定位
    call_seek = (By.ID, "com.callme.mall:id/et_search")  # 首页搜索
    call_carousel = (By.ID, "com.callme.mall:id/bannerViewPager")  # 首页轮播图
    call_handpick = (By.ID, "com.callme.mall:id/ll_icon")  # 首页酒类
    call_action = (By.ID, "com.callme.mall:id/ll_icon_2")  # 首页酒类下活动
    call_hours = (By.ID, "com.callme.mall:id/tv_business_hours")  # 首页营业通知
    call_hour = (By.ID, "com.callme.mall:id/tv_announce_info")  # 首页通知
    call_activity = (By.CLASS_NAME, "android.widget.Image")  # 首页活动
    call_handpicks = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab")  # 首页酒类二
    call_title = (By.ID, "com.callme.mall:id/tv_title")  # 首页商品标题
    call_tag = (By.ID, "com.callme.mall:id/tv_price")  # 首页商品优惠后
    call_tags = (By.ID, "com.callme.mall:id/tv_old_price")  # 首页商品优惠前
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
        App.home(self, num=0)

    def home_locate(self):  # 首页定位
        self.wait(EC.presence_of_element_located, self.call_locate).click()

    def home_seek(self):  # 首页搜索
        self.wait(EC.presence_of_element_located, self.call_seek).click()

    def home_carousel(self):  # 首页轮播图
        self.driver.find_element(*self.call_carousel).click()

    def home_handpick(self, num):  # 首页酒类
        self.wait(EC.visibility_of_all_elements_located, self.call_handpick)[num].click()

    def home_action(self, num):  # 首页酒类下活动
        self.driver.find_elements(*self.call_action)[num].click()

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
        hour = self.wait(EC.presence_of_element_located, self.call_hour).text
        return hour

    def home_activity(self):  # 首页活动
        self.driver.swipe(600, 1200, 600, 800, 500)
        self.wait(EC.presence_of_element_located, self.call_activity).click()

    def home_handpicks(self, num):  # 首页酒类2
        App.home(self).click()
        self.wait(EC.presence_of_all_elements_located, self.call_handpicks)[num].click()

    def home_title(self, num):  # 首页商品标题
        App.home(self).click()
        self.wait(EC.visibility_of_all_elements_located, self.call_title)[num].click()

    def home_shopping(self, stat=0, num=0):  # 首页商品价格
        App.home(self).click()
        if stat == 0:  # 点商品标题
            self.wait(EC.visibility_of_all_elements_located, self.call_title)[num].click()
        elif stat == 1:  # 获取优惠后价格
            names = self.wait(EC.presence_of_all_elements_located, self.call_tag)[num].text
            return names
        elif stat == 2:  # 获取优惠前价格
            names = self.wait(EC.presence_of_all_elements_located, self.call_tags)[num].text
            return names
        elif stat == 3:  # 点商品购物车
            self.wait(EC.presence_of_all_elements_located, self.call_add)[num].click()
        else:
            if stat == 4:  # 点商品图片
                self.wait(EC.presence_of_all_elements_located, self.call_img)[num].click()
            elif stat == 5:  # 商品查看更多
                [self.swipe(600, 1800, 600, 600, 500) for x in range(3)]
                self.wait(EC.element_to_be_clickable, self.call_more).click()

    def home_cart(self):  # 首页购物车
        self.driver.find_element(*self.call_cart).click()


if __name__ == "__main__":
    driver = wechat()
    name = Home(driver)
    name.home_cart()
