from selenium.webdriver.common.by import By
from wechat.common.call_common import Login
from wechat.common.call_wechat import wechat


class Home(Login):
    call_locate = (By.ID, "cityName")  # 定位
    call_search = (By.CLASS_NAME, "h-search")  # 搜索
    call_slideshow = (By.XPATH, "/html/body/section[1]/article[3]/ul/li[1]")  # 轮播图
    call_handpick = (By.CLASS_NAME, 'a')  # 啤酒(精选列表0,1,2,3,4,5,6,7）
    call_figure = (By.CLASS_NAME, "positionClass")

    def call_home(self,):
        self.login()
        self.time(3)
        # seek = self.driver.find_element(*self.call_improted).click()
        product = self.driver.find_elements(*self.call_figure)[0].text
        print(">>" + product)


if __name__ == "__main__":
    driver = wechat()
    H = Home(driver)
    H.call_home()
