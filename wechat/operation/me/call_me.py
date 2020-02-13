from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from wechat.common.call_wechat import wechat
from wechat.common.call_common import Login
from wechat.operation.home.call_home import Home


class Me(Login):

    call_choose = (By.CLASS_NAME, "href-link")  # 我的页面选择
    call_level = (By.CLASS_NAME, "user-level")  # 我的页面等级VIP
    call_SevenMoor = (By.CLASS_NAME, "item j-SevenMoor")  # 我的页面联系客服
    call_add = (By.CLASS_NAME, "add-item")  # 我的页面投诉建议

    def me_choose(self, num):
        self.login()
        Home(driver).home_menu(4)
        self.wait(EC.presence_of_all_elements_located, self.call_choose)[num].click()


if __name__ == "__main__":
    driver = wechat()
    name = Me(driver)
    name.me_choose()