from selenium.webdriver.common.by import By
from wechat.common.call_common import Login
from wechat.common.call_wechat import wechat


class Home(Login):
    call_locate = (By.ID, "cityName")  # 定位
    call_search = (By.CLASS_NAME, "h-search")  # 搜索
    call_slideshow = (By.XPATH, "/html/body/section[1]/article[3]/ul/li[1]")  # 轮播图
    call_handpick = (By.CLASS_NAME, 'a')  # 啤酒(精选列表0,1,2,3,4,5,6,7）
    call_activity = (By.CLASS_NAME, "hotarea-link")  # 活动及楼层（0,1,2,3,4,5,6）
    call_menu = (By.CLASS_NAME, "nav-item")  # 底部菜单栏（0,1,2,3,4）
    call_shoppingcart = (By.CLASS_NAME, "float_cart")  # 首页购物车

    def call_home(self,):
        self.login()
        self.time(3)
        while True:
            self.swipe(840, 540, 200, 540, 500)
            try:
                self.driver.find_element(*self.call_slideshow).click()
            except:
                pass
            else:
                break

        # seek = self.driver.find_element(*self.call_shoppingcart).click()
        # product = self.driver.find_elements(*self.call_menu)[4].click()
        # print(">>" + seek)


if __name__ == "__main__":
    driver = wechat()
    H = Home(driver)
    H.call_home()
