import logging
from wechat_test.common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
from wechat_test.businessView.scation import Scation

class Me(Common):
    csv_file='../data/account.csv'  # 参数路径

    me_a = (By.XPATH, "//*[contains(text(), '地址管理')]")
    me_b = (By.XPATH, "//*[contains(text(), '删除')]")
    me_c = (By.XPATH, "//*[contains(text(), '确定')]")
    me_d = (By.XPATH, "//*[contains(text(), '删除')]")

    def me_A(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(4)
        self.Time(3)
        try:
            self.driver.find_element(*self.me_a).click()
        except:
            self.Swipe(1)
            self.driver.find_element(*self.me_a).click()
        self.Time(3)
        num = self.driver.find_elements(*self.me_d)
        list = []
        for i in num:
            a = i.text
            list.append(a)
        P = list.count('删除')
        while True:
            self.Time(2)
            if P <= 1:
                break
            else:
                self.Time(2)
                self.driver.find_element(*self.me_b).click()
                self.driver.find_element(*self.me_c).click()
                P -= 1
        return P


if __name__ == '__main__':
        driver = appium_desired()
        num = Me(driver)
        num.me_A()