import logging
from wechat_test.common.desired_caps import appium_desired
from wechat_test.businessView.scation import Scation
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common

class Drink(Common):
    csv_file='../data/account.csv'  # 参数路径

    drink_a = (By.XPATH, "/html/body/nav[2]/ul/li[3]/a")  # 马上喝切换筛选
    drink_b = (By.XPATH, "//*[contains(text(), '燕京')]")  # 选择燕京
    drink_c = (By.XPATH, "//*[contains(text(), '确定')]")  # 马上喝筛选点击确定
    drink_d = (By.XPATH, "/html/body/section/article/ul/li[7]/a/div[5]/aside/div[1]")  # 点击加号
    drink_e = (By.XPATH, "//*[contains(text(), '立即购买')]")  # 马上喝点立即购买
    drink_m = (By.XPATH, "/html/body/div[2]")  # 提交订单详情
    drink_f = (By.XPATH, "/html/body/div[3]/div[2]") # 逛逛
    drink_g = (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]") # 订单状态
    drink_h = (By.CLASS_NAME, "android.widget.Button")  # 点击确定


    def drink_A(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(2)
        self.Time(10)
        self.driver.find_element(*self.drink_a).click()
        self.driver.find_element(*self.drink_b).click()
        self.driver.find_element(*self.drink_c).click()
        self.Swipe(3)
        self.Time(3)
        self.driver.find_element(*self.drink_d).click()
        self.Time(3)
        self.driver.find_element(*self.drink_e).click()
        self.settle(1)
        T = self.driver.find_element(*self.drink_m).text
        return T

    def drink_B(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(3)
        self.Time(5)
        T = self.driver.find_element(*self.drink_g).text
        return T

    def drink_C(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(3)
        self.Time(5)
        T = self.driver.find_element(*self.drink_g).text
        return T

    def drink_D(self):
        self.base(2)
        self.Time(10)
        self.driver.find_element(*self.drink_a).click()
        self.driver.find_element(*self.drink_b).click()
        self.driver.find_element(*self.drink_c).click()
        self.Swipe(3)
        self.Time(3)
        self.driver.find_element(*self.drink_d).click()
        self.Time(3)
        self.driver.find_element(*self.drink_e).click()


    def drink_E(self):
        num = Scation(self.driver)
        num.login_guiyang()
        Drink.drink_D(self)
        self.settle(0)
        self.Time(3)
        try:
            self.driver.switch_to.context('NATIVE_APP')
            determine = self.driver.find_element(*self.drink_h)
            if determine.text in "立即支付":
                self.driver.keyevent(4)
            else:
                determine.click()
        except:
            logging.info('no window_handles')
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        self.Time(5)
        T = self.driver.find_element(*self.drink_g).text
        return T

    def drink_F(self):
        num = Scation(self.driver)
        num.login_guiyang()

if __name__ == '__main__':
        driver = appium_desired()
        num = Drink(driver)
        num.drink_E()