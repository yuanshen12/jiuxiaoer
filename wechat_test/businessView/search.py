import logging
from wechat_test.common.desired_caps import appium_desired
from wechat_test.businessView.scation import Scation
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common


class Search(Common):
    csv_file='../data/account.csv'  # 参数路径

    search_a = (By.XPATH,"//*[@id='header']/aside[2]/input")  # 首页点击搜索
    search_b = (By.XPATH, "/html/body/header/div[1]/div/form/input")  # 搜索输入
    search_c = (By.XPATH, "/html/body/div[1]/div[4]/ul/li[1]")  # 确定搜索商品
    search_d = (By.XPATH, "/html/body/section/article/ul/li[1]/a/div[3]/div[2]")  # 商品详情
    search_e = (By.XPATH, "/html/body/section/article/ul/li[1]/a/div[5]/aside/div[1]")  # 加入购物车
    search_f = (By.XPATH, "//*[@id='TripBook']/aside/div[1]/a")  # 加入购物车
    search_g = (By.XPATH, "/html/body/nav/article/aside[1]/div[1]/div")  # 打开购物车
    search_h = (By.XPATH, "/html/body/nav/article/aside[1]/div[1]/span")  # 打开购物车
    search_j = (By.XPATH, "/html/body/section/article/ul/li[1]/a/div[3]/div[2]")  # 获取text
    search_k = (By.XPATH, "/html/body/div[1]/div[1]")  # 获取text
    search_l = (By.XPATH, "//*[contains(text(), '去结算')]") # 结算
    search_z = (By.XPATH, "/html/body/div[2]") # 提交订单详情
    search_i = (By.XPATH, "//*[@id='TripBook']/aside/div[2]/a")  # 立即购买
    search_m = (By.XPATH, "/html/body/div[3]/div[2]") # 逛逛
    search_n = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]")  # 搜索历史
    search_p = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/button")  # 清空历史搜索


    def Search_a(self):
        num = Scation(self.driver)
        num.login_guiyang()
        data = Common.get_csv_data(self,self.csv_file,2)
        self.driver.find_element(*self.search_a).click()
        self.driver.find_element(*self.search_b).send_keys(data[1])
        self.Time(3)
        self.driver.press_keycode(66)
        self.Time(3)
        num = self.driver.find_element(*self.search_d).text
        return num

    def Search_b(self):
        self.Time(5)
        try:
            self.driver.find_element(*self.search_h).click()
            self.gouwu_shanchu()
            self.Time(2)
        except:
            pass
        else:
            self.driver.keyevent(4)
        self.Time(5)
        self.driver.find_element(*self.search_e).click()
        self.Time(5)
        self.driver.find_element(*self.search_f).click()
        self.Time(5)
        try:
            self.driver.find_element(*self.search_h).click()
            return True
        except:
            return False

    def Search_c(self):
        self.Time(5)
        self.driver.find_element(*self.search_l).click()
        self.settle(1)
        scation_z_text = self.driver.find_element(*self.search_z).text
        return scation_z_text

    def Search_d(self):
        self.Search_a()
        self.driver.find_element(*self.search_e).click()
        self.Time(3)
        self.driver.find_element(*self.search_i).click()
        self.settle(1)
        scation_z_text = self.driver.find_element(*self.search_z).text
        return scation_z_text

    def Search_e(self):
        self.driver.find_element(*self.search_m).click()
        self.Time(5)
        self.advertisement()
        self.driver.find_element(*self.search_a).click()
        search_n_text = self.driver.find_element(*self.search_n).text
        return search_n_text

    def Search_f(self):
        try:
            self.driver.find_element(*self.search_p).click()
            return True
        except:
            return False

    def Search_g(self):
        data = Common.get_csv_data(self,self.csv_file,2)
        self.driver.find_element(*self.search_b).send_keys(data[1])
        self.Time(3)
        self.driver.press_keycode(66)
        self.Time(3)
        try:
            self.driver.find_element(*self.search_h).click()
            self.gouwu_shanchu()
            self.Time(2)
        except:
            pass
        else:
            self.driver.keyevent(4)
        self.Time(5)
        self.driver.find_element(*self.search_e).click()
        self.Time(5)
        self.driver.find_element(*self.search_f).click()
        self.Time(5)
        self.driver.find_element(*self.search_l).click()
        self.settle(1)
        scation_z_text = self.driver.find_element(*self.search_z).text
        return scation_z_text


if __name__ == '__main__':
     driver = appium_desired()
     num = Search(driver)
     num.Search_d()