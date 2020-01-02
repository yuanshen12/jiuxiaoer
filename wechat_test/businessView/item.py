from wechat_test.common.desired_caps import appium_desired
from wechat_test.businessView.scation import Scation
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
from wechat_test.common.TMS import TMS
import re


class Item(Common):
    csv_file='../data/account.csv'  # 参数路径
    reduced_a = (By.XPATH, "/html/body/section[3]/article/a[3]")  # 首页进入热销推荐


    def item(self,mun=()):
        try:
            num = Scation(self.driver)
            num.login_guiyang()
        except:
            num = Scation(self.driver)
            num.login_guiyang()
        self.Swipe(1)
        self.driver.find_element(*self.reduced_a).click()
        self.Time(3)

if __name__ == '__main__':
        driver = appium_desired()
        num = Item(driver)
        num.item()