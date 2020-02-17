from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_common import Login
from common.call_wechat import wechat


class Home(Login):
    call_locate = (By.ID, "cityName")  # 定位
    call_search = (By.CLASS_NAME, "h-search")  # 搜索
    call_carousel = (By.XPATH, "/html/body/section[1]/article[3]/ul/li[{}]")  # 轮播图
    call_handpick = (By.CLASS_NAME, 'a')  # 啤酒(精选列表0,1,2,3,4,5,6,7）
    call_activity = (By.CLASS_NAME, "hotarea-link")  # 活动及楼层（0,1,2,3,4,5,6）
    call_menu = (By.CLASS_NAME, "nav-item")  # 底部菜单栏（0,1,2,3,4）
    call_cart = (By.CLASS_NAME, "float_cart")  # 首页购物车
    call_more = (By.CLASS_NAME, "moretext")  # 查看更多（0,1,2,3,4）
    call_shopping = (By.CLASS_NAME, "redbase")  # 首页点开抽屉页面（0,1,2……）
    call_img = (By.CLASS_NAME, "img")  # 首页商品图片(0,1,2……）
    call_title = (By.CLASS_NAME, "goods-title")  # 首页商品标题（0,1,2……）
    call_tag = (By.CLASS_NAME, "goods-price")  # 首页商品价格标签（0,1,2……）
    call_about = (By.CLASS_NAME, "about")  # 首页进入关于酒小二

    def __init__(self, driver):
        super().__init__(driver)
        self.login()

    def home_location(self):  # 首页打开定位
        self.wait(EC.element_to_be_clickable, self.call_locate).click()

    def home_search(self):  # 首页打开搜索
        self.wait(EC.element_to_be_clickable, self.call_search).click()

    def home_carousel(self, num=1):  # 首页打开轮播图(1,2……）
        while True:
            try:
                self.wait(EC.element_to_be_clickable, self.amend(self.call_carousel, num)).click()
                break
            except:
                self.swipe(840, 540, 200, 540, 500)
                continue

    def home_handpick(self, num):  # 精选列表（0,1,2,3,4,5,6,7,8）
        self.wait(EC.presence_of_all_elements_located, self.call_handpick)[num].click()

    def home_activity(self, num):  # 精选活动（0,1,2,3,4,5,6,7)
        while True:
            try:
                self.wait(EC.presence_of_all_elements_located, self.call_activity)[num].click()
                break
            except:
                self.swipe(600, 1200, 600, 600, 500)
                continue

    def home_cart(self):  # 首页点进购物车
        self.wait(EC.presence_of_element_located, self.call_cart).click()

    def home_menu(self, num):  # 首页底部菜单栏(0,1,2,3,4)
        self.wait(EC.presence_of_all_elements_located, self.call_menu)[num].click()

    def home_more(self, num):  # 首页查看更多（0,1,2,3）
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_more)[num].click()
                break
            except:
                continue


    def home_shopping(self, num):  # 首页点开抽屉（0,1,2,……）
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_shopping)[num].click()
                break
            except:
                pass

    def home_img(self, num):  # 首页商品图片（0,1,2……）
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_img)[num].click()
            except:
                pass
            else:
                break

    def home_title(self, num):  # 首页商品标题（0,1,2……）
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_title)[num].click()
            except:
                pass
            else:
                break

    def home_tag(self, num):  # 首页商品价格标签
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                text = self.wait(EC.presence_of_all_elements_located, self.call_tag)[num].text
            except:
                pass
            else:
                break
        return text

    def home_about(self):  # 首页底部帮助中心
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_element_located, self.call_about).click()
            except:
                pass
            else:
                break


if __name__ == "__main__":
    driver = wechat()
    H = Home(driver)
    H.home_carousel()
