import logging
from time import sleep
from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common

# 马上喝切换指定酒类
class Switch_wine(Common):
    beer_open = (By.XPATH, '/html/body/nav[2]/ul/li[1]/a')
    wine = (By.XPATH, "//*[contains(text(), '红酒')]")
    liquor = (By.XPATH, "//*[contains(text(), '白酒')]")
    foreign = (By.XPATH, "//*[contains(text(), '洋酒')]")
    beer = (By.XPATH, "//*[contains(text(), '啤酒')]")
    drunk = (By.XPATH, "//*[contains(text(), '下酒菜')]")
    drinks = (By.XPATH, "//*[contains(text(), '饮料')]")
    # 排序
    comprehensive_open = (By.XPATH, "/html/body/nav[2]/ul/li[2]")
    comprehensive = (By.XPATH, "//*[contains(text(), '综合排序')]")
    sales = (By.XPATH, "//*[contains(text(), '销量从高到低')]")
    # 价格排序
    prich_high = (By.XPATH, "//*[text()='价格从高到低']")
    prich_low = (By.XPATH, "//*[contains(text(), '价格从低到高')]")
    prich_one = (By.XPATH, "/html/body/section/article/ul/li[1]/a/div[4]/span")
    prich_two = (By.XPATH, "/html/body/section/article/ul/li[2]/a/div[4]/span")
    # 筛选
    screen = (By.XPATH, "/html/body/nav[2]/ul/li[3]/a")
    brand = (By.XPATH, "//*[@id='-2']/aside[2]/div[7]")
    prich_screen = (By.XPATH, "//*[@id='-1']/aside[2]/div[1]")
    type = (By.XPATH, "//*[@id='50']/aside[2]/div[1]")
    place = (By.XPATH, "//*[@id='51']/aside[2]/div[1]")
    ethyl = (By.XPATH, "//*[@id='52']/aside[2]/div[1]")
    capacity = (By.XPATH, "//*[@id='53']/aside[2]/div[2]")
    suer = (By.XPATH, "//*[contains(text(), '确定')]")
    reset = (By.XPATH, "//*[contains(text(), '重置')]")
    # 葡萄酒
    grape = (By.XPATH, "//*[contains(text(), '葡萄酒')]")
    TO = (By.XPATH, '/html/body/nav[2]/ul/li[1]')
    grape_type = (By.XPATH, "//*[@id='50']/aside[2]/div[1]")

# 从首页获取预期值（红酒）
    def Grape(self):
        try:
            grape_text = self.driver.find_element(*self.grape)
        except:
            return False
        else:
            grape_text.click()
            return True

# 切换到销量排序
    def TO_sales(self):
        try:
            self.driver.find_element(*self.comprehensive_open).click()
            sales = self.driver.find_element(*self.sales)
        except:
            return False
        else:
            logging.info('login success!')
            sales.click()
            return True

# 切换到价格从高到低排序(第一个价格）
    def prich_One(self):
        self.driver.find_element(*self.comprehensive_open).click()
        T = 0
        while T < 3:
            self.wait_time(2)
            self.driver.find_element(*self.comprehensive_open).click()
            self.wait_time(3)
            try:
                self.driver.find_element(*self.prich_high).click()
            except:
                self.driver.find_element(*self.comprehensive_open).click()
                self.driver.find_element(*self.prich_high).click()
            T += 1
        self.wait_time(3)
        # sleep(3)
        # self.driver.find_element(*self.comprehensive_open).click()
        # self.driver.find_element(*self.prich_high).click()
        # sleep(3)
        prich_One = self.driver.find_element(*self.prich_one).text
        return float(prich_One)
# 切换到价格从高到低排序（第二个价格）
    def prich_Two(self):
        prich_Two = self.driver.find_element(*self.prich_two).text
        return float(prich_Two)

# 切换到价格从低到高排序（第一个价格）
    def prich_Low(self):
        self.driver.find_element(*self.comprehensive_open).click()
        T = 0
        while T < 3:
            self.wait_time(2)
            self.driver.find_element(*self.comprehensive_open).click()
            self.wait_time(2)
            try:
                self.driver.find_element(*self.prich_low).click()
            except:
                self.driver.find_element(*self.comprehensive_open).click()
                self.driver.find_element(*self.prich_low).click()
            T += 1
        self.wait_time(3)
        prich_Low = self.driver.find_element(*self.prich_one).text
        return float(prich_Low)
# 切换综合排序
    def Comprehensive(self):
        try:
            self.driver.find_element(*self.comprehensive_open).click()
            self.wait_time(2)
            self.driver.find_element(*self.comprehensive).click()
        except:
            return False
        else:
            return True
# 筛选（品牌）
    def Brand(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.find_element(*self.brand).click()
            Brand = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Brand.click()
            return True
# 筛选（价格）
    def Prich_screen(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.find_element(*self.prich_screen).click()
            Prich_screen = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Prich_screen.click()
            return True
# 筛选（类型）
    def Type(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.swipe(int(1048)/2,int(3000)/2,int(1048)/2,int(2000)/4,duration=sleep(1))
            sleep(2)
            self.driver.find_element(*self.type).click()
            Type = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Type.click()
            return True
# 筛选（产地）
    def Place(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.swipe(int(1048)/2,int(3500)/2,int(1048)/2,int(1500)/4,duration=sleep(1))
            sleep(3)
            self.driver.find_element(*self.place).click()
            Place = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Place.click()
            return True
# 筛选（酒精度）
    def Ethyl(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.swipe(int(1048)/2,int(3500)/2,int(1048)/2,int(800)/4,duration=sleep(1))
            sleep(1)
            self.driver.find_element(*self.ethyl).click()
            Ethyl = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Ethyl.click()
            return True
# 筛选（容量）
    def Capacity(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            self.driver.swipe(int(1048)/2,int(3750)/2,int(1048)/2,int(100)/4,duration=sleep(1))
            sleep(1)
            self.driver.find_element(*self.capacity).click()
            Capacity = self.driver.find_element(*self.suer)
        except:
            return False
        else:
            Capacity.click()
            return True
# 筛选（重置）
    def Reset(self):
        sleep(3)
        try:
            self.driver.find_element(*self.screen).click()
            Reset = self.driver.find_element(*self.reset)
        except:
            return False
        else:
            Reset.click()
            return True
# 从切换页面获取实际值（pijiu)
    def TO_suer(self):
        Beer_suer = self.driver.find_element(*self.TO).text
        return Beer_suer

# 切换红酒并获取预期值
    def wine_text(self):
        self.driver.find_element(*self.TO).click()
        sleep(1)
        wine_text = self.driver.find_element(*self.wine)
        wine = wine_text.text
        wine_text.click()
        return wine

# 切换白酒并获取预期值
    def liquor_text(self):
        self.wait_time(2)
        self.driver.find_element(*self.TO).click()
        self.wait_time(2)
        liquor_text = self.driver.find_element(*self.liquor)
        liquor = liquor_text.text
        liquor_text.click()
        return liquor

# 切换洋酒并获取预期值
    def foreign_text(self):
        self.driver.find_element(*self.TO).click()
        sleep(1)
        foreign_text = self.driver.find_element(*self.foreign)
        foreign = foreign_text.text
        foreign_text.click()
        return foreign

# 切换啤酒并获取预期值
    def beer_text(self):
        self.driver.find_element(*self.TO).click()
        sleep(1)
        beer_text = self.driver.find_element(*self.beer)
        beer = beer_text.text
        beer_text.click()
        return beer

# 切换下酒菜并获取预期值
    def drunk_text(self):
        self.driver.find_element(*self.TO).click()
        sleep(1)
        drunk_text = self.driver.find_element(*self.drunk)
        drunk = drunk_text.text
        drunk_text.click()
        return drunk

# 切换饮料并获取预期值
    def drinks_text(self):
        self.driver.find_element(*self.TO).click()
        sleep(1)
        drinks_text = self.driver.find_element(*self.drinks)
        drinks = drinks_text.text
        drinks_text.click()
        return drinks
