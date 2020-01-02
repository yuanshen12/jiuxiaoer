import logging
from wechat_test.common.desired_caps import appium_desired
from wechat_test.businessView.scation import Scation
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common

class Switch(Common):
    csv_file='../data/account.csv'  # 参数路径

    switch_a = (By.XPATH, "//*[contains(text(), '啤酒')]")  # 首页进入啤酒
    switch_b = (By.XPATH, "//*[contains(text(), '红酒')]")  # 切换至红酒
    switch_c = (By.XPATH, "//*[contains(text(), '葡萄酒')]")  # 首页进入葡萄酒
    switch_d = (By.XPATH, "//*[contains(text(), '白酒')]")  # 首页进入白酒
    switch_e = (By.XPATH, "//*[contains(text(), '洋酒')]")  # 首页进入洋酒
    switch_f = (By.XPATH, '/html/body/nav[2]/ul/li[1]/a')  # 马上喝酒类切换

    switch_g = (By.XPATH, "//*[contains(text(), '下酒菜')]")  # 马上喝切换下酒菜
    switch_h = (By.XPATH, "//*[contains(text(), '饮料')]")  # 马上喝切换饮料
    switch_j = (By.XPATH, "//*[contains(text(), '物料')]")  # 马上喝切换物料
    switch_k = (By.XPATH, "//*[contains(text(), '酒具')]")  # 马上喝切换酒具

    def Switch_A(self,switch):
        num = Scation(self.driver)
        num.login_guiyang()
        if switch == 1:
            self.driver.find_element(*self.switch_a).click()
        elif switch == 2:
            self.driver.find_element(*self.switch_c).click()
        elif switch == 3:
            self.driver.find_element(*self.switch_d).click()
        elif switch == 4:
            self.driver.find_element(*self.switch_e).click()

    def Switch_B(self):
        self.Time(10)
        kind = 0
        try:
            while kind in range(9):
                self.Time(5)
                kind = kind + 1
                if kind == 1:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_b).click()
                elif kind == 2:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_j).click()
                elif kind == 3:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_d).click()
                elif kind == 4:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_e).click()
                elif kind == 5:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_g).click()
                elif kind == 6:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_h).click()
                elif kind == 7:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_k).click()
                elif kind == 8:
                    self.driver.find_element(*self.switch_f).click()
                    self.Time(1)
                    self.driver.find_element(*self.switch_a).click()
        except:
            return False
        else:
            return True

class Switch_comprehensive(Common):
    csv_file='../data/account.csv'  # 参数路径

    switch_a = (By.XPATH, "/html/body/nav[2]/ul/li[2]")  # 马上喝切换排序
    switch_b = (By.XPATH, "//*[contains(text(), '综合排序')]")  # 马上喝排序切换至综合
    switch_c = (By.XPATH, "//*[contains(text(), '销量从高到低')]")  # 马上喝排序切换至销量
    switch_d = (By.XPATH, "//*[text()='价格从高到低']")  # 马上喝排序切换从高到低
    switch_e = (By.XPATH, "//*[contains(text(), '价格从低到高')]")  # 马上喝排序切换从低到高

    def Switch_A(self):
        switch = 0
        try:
            while switch in range(4):
                switch += 1
                if switch == 1:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_c).click()
                elif switch == 2:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_b).click()
                elif switch == 3:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_d).click()
                elif switch == 4:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_e).click()
        except:
            return False
        else:
            return True

class Switch_screen(Common):
    csv_file='../data/account.csv'  # 参数路径

    switch_a = (By.XPATH, "/html/body/nav[2]/ul/li[3]/a")  # 马上喝切换筛选
    switch_b = (By.XPATH, "//*[@id='-2']/aside[2]/div[7]")  # 马上喝切换至品牌
    switch_c = (By.XPATH, "//*[@id='-1']/aside[2]/div[1]")  # 马上喝切换至价格
    switch_d = (By.XPATH, "//*[@id='58']/aside[2]/div[1]")  # 马上喝切换至种类
    switch_e = (By.XPATH, "//*[@id='59']/aside[2]/div[1]")  # 马上喝切换至产地
    switch_f = (By.XPATH, "//*[@id='60']/aside[2]/div[1]")  # 马上喝切换至酒精度
    switch_g = (By.XPATH, "//*[@id='61']/aside[2]/div[1]")  # 马上喝切换至麦芽度
    switch_h = (By.XPATH, "//*[@id='62']/aside[2]/div[1]")  # 马上喝切换至容量
    switch_j = (By.XPATH, "//*[contains(text(), '确定')]")  # 马上喝筛选点击确定
    switch_k = (By.XPATH, "//*[contains(text(), '重置')]")  # 马上喝筛选点击重置
    switch_l = (By.XPATH, "/html/body/section/article/ul/li[2]/a/div[5]/aside/div[1]")  # 马上喝添加购物车
    switch_z = (By.XPATH, "//*[contains(text(), '立即购买')]")  # 马上喝点立即购买
    search_m = (By.XPATH, "/html/body/div[2]")  # 提交订单详情

    def Switch_A(self):
        Screen = 0
        try:
            while Screen in range(7):
                self.Time(5)
                Screen += 1
                if Screen == 1:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_b).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 2:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_c).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 3:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_e).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 4:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_f).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 5:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.Swipe(1)
                    self.Time(1)
                    self.driver.find_element(*self.switch_g).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 6:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.Swipe(1)
                    self.Time(1)
                    self.driver.find_element(*self.switch_h).click()
                    self.driver.find_element(*self.switch_j).click()
                elif Screen == 7:
                    self.driver.find_element(*self.switch_a).click()
                    self.Time(2)
                    self.driver.find_element(*self.switch_k).click()
        except:
            return False
        else:
            return True

    def Switch_B(self):
        self.Time(5)
        self.driver.find_element(*self.switch_l).click()
        self.Time(3)
        self.driver.find_element(*self.switch_z).click()
        self.settle(1)
        T = self.driver.find_element(*self.search_m).text
        return T

if __name__ == '__main__':
        driver = appium_desired()
        num = Switch_screen(driver)
        num.Switch_B()