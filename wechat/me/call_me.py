from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from wechat.home.call_home import Home
from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions


class Me(Login):

    call_choose = (By.CLASS_NAME, "href-link")  # 我的页面选择
    call_level = (By.CLASS_NAME, "user-level")  # 我的页面等级VIP
    call_SevenMoor = (By.CLASS_NAME, "j-SevenMoor")  # 我的页面联系客服
    call_add = (By.CLASS_NAME, "add-item")  # 我的页面投诉建议

    def __init__(self, driver):
        super().__init__(driver)
        self.login()
        Home(driver).home_menu(4)

    def me_choose(self, num):  # 我的页面选项（1、个人信息,2、我的积分……）
        choose = self.wait(EC.presence_of_all_elements_located, self.call_choose)[num]
        if 0 <= num < 10:
            choose.click()
        elif num >= 10:
            self.swipe(600, 1200, 600, 600, 500)
            sleep(1)
            choose.click()

    def me_level(self):  # 我的页面等级VIP
        self.wait(EC.element_to_be_clickable, self.call_level).click()

    def me_SevenMoor(self):  # 我的页面点开客服
        sleep(1)
        self.swipe(600, 1600, 600, 200, 500)
        names = self.wait(EC.presence_of_element_located, self.call_SevenMoor)
        TouchActions(self.driver).tap(names).perform()

    def me_add(self):  # 我的页面点开投诉建议
        sleep(1)
        self.swipe(600, 1600, 600, 200, 500)
        self.wait(EC.element_to_be_clickable, self.call_add).click()


if __name__ == "__main__":
    driver = wechat()
    name = Me(driver)
    name.me_add()