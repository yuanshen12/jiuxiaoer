from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from time import sleep

# 活动
class activity(Common):
    new_suer = (By.XPATH,"//*[@id='ho']/a[1]")
    goddes = (By.XPATH,"//*[@id='ho']/a[2]")
    foods = (By.XPATH,"//*[@id='ho']/a[3]")
    food = (By.XPATH,"/html/body/nav[2]/ul/li[1]/a")
    pot = (By.XPATH,"//*[@id='ho']/a[4]")
    queding = (By.XPATH,"//*[contains(text(), '确定')]")
    new = (By.XPATH,"/html/body/section[3]/article/a[2]")
    full = (By.XPATH,"/html/body/section[3]/article/a[3]")
    beer = (By.XPATH,"/html/body/div[4]/section[1]/article[1]/div/a")
    beer_a = (By.XPATH,"//*[contains(text(), '查看更多啤酒')]")
    hot = (By.XPATH,"/html/body/section[3]/article/a[1]")
    suer = (By.XPATH,"/html/body/nav[2]/ul/li[1]/a")
    wine = (By.XPATH,"/html/body/div[4]/section[2]/article[1]/div/a")
    wine_a = (By.XPATH,"//*[contains(text(), '查看更多红酒')]")
    liquor = (By.XPATH,"/html/body/div[4]/section[3]/article[1]/div/a")
    liquor_a = (By.XPATH,"//*[contains(text(), '查看更多白酒')]")
    foreign = (By.XPATH,"/html/body/div[4]/section[4]/article[1]/div/a")
    foreign_a = (By.XPATH,"//*[contains(text(), '查看更多洋酒')]")
# 加入购物车和结算
    home_p = (By.XPATH,"/html/body/div[4]/section[1]/article[2]/ul/li[1]/a/div[2]")
    home_page = (By.XPATH,"/html/body/div[4]/section[1]/article[2]/ul/li[1]/button/div")
    gouwu = (By.XPATH,"//*[@id='TripBook']/aside/div[1]/a")
    gouwu_open = (By.XPATH,"/html/body/aside[2]/div")
    home_pa = (By.XPATH,"/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[3]/p")
    jin = (By.XPATH,"/html/body/div[4]/section[1]/article[2]/ul/li[1]/a/div[3]/span")
    suan = (By.XPATH,"//*[@id='TripBook']/aside/div[2]/a")
    jin_a = (By.XPATH,"//*[@id='footer']/div/div/span[2]/span")
    suibianguang = (By.XPATH,"/html/body/div[1]/div[2]/div[2]")



# 清空购物车
    def dele(self):
        self.driver.find_element(*self.gouwu_open).click()
        try:
            self.gouwu_shanchu()
            self.wait_time(2)
        except:
            return False
        finally:
            self.driver.find_element(*self.suibianguang).click()

    def deles(self):
        try:
            self.dele()
        except:
            return False
        else:
            self.wait_time(2)
            return True

# 新品尝鲜
    def Suer(self):
        self.driver.find_element(*self.new_suer).click()
        self.wait_time(2)
        title = self.driver.title
        return title
# 女神专区
    def Goddes(self):
        self.driver.keyevent(4)
        self.wait_time(2)
        self.driver.find_element(*self.goddes).click()
        self.wait_time(2)
        title = self.driver.title
        return title
# 饮料小食
    def Foods(self):
        self.driver.keyevent(4)
        self.wait_time(5)
        foods = self.driver.find_element(*self.foods)
        Foods = foods.text
        foods.click()
        self.wait_time(2)
        return Foods
# 饮料
    def Food(self):
        self.wait_time(5)
        food = self.driver.find_element(*self.food)
        Food = food.text
        food.click()
        self.wait_time(2)
        return Food
# 酒友圈
    def Pot(self):
        self.driver.keyevent(4)
        self.wait_time(2)
        self.driver.find_element(*self.pot).click()
        self.wait_time(5)
        try:
            self.driver.find_element(*self.queding).click()
        except:
            return True
        else:
            return False
#新用户活动
    def New(self):
        self.wait_time(10)
        try:
            self.driver.find_element(*self.new).click()
            self.wait_time(10)
        except:
            return False
        else:
            self.driver.keyevent(4)
            return True
# 首页下单满减
    def Full(self):
        self.wait_time(5)
        try:
            self.driver.find_element(*self.full).click()
            self.wait_time(10)
        except:
            return False
        else:
            self.driver.keyevent(4)
            return True

# 首页进入热销
    def Hot(self):
        self.wait_time(2)
        try:
            self.driver.find_element(*self.full).click()
            self.wait_time(10)
        except:
            return False
        else:
            # self.driver.keyevent(4)
            return True


# 专题封装
    def num(self,S,SS):
        self.driver.keyevent(4)
        self.wait_time(5)
        if SS == 1:
            self.Swipe(S)
            self.driver.find_element(*self.beer).click()
        elif SS ==2:
            self.Swipe(S)
            self.driver.find_element(*self.wine).click()
        elif SS ==3:
            self.Swipe(S)
            self.driver.find_element(*self.liquor).click()
        elif SS ==4:
            self.Swipe(S)
            self.driver.find_element(*self.foreign).click()
        self.wait_time(3)
        suer = self.driver.find_element(*self.suer).text
        return suer

# 专题更多封装
    def num_d(self,S,SS):
        self.driver.keyevent(4)
        self.wait_time(5)
        if SS ==1:
            self.Swipe(S)
            self.driver.find_element(*self.beer_a).click()
        elif SS ==2:
            self.Swipe(S)
            self.driver.find_element(*self.wine_a).click()
        elif SS ==3:
            self.Swipe(S)
            self.driver.find_element(*self.liquor_a).click()
        elif SS ==4:
            self.Swipe(S)
            self.driver.find_element(*self.foreign_a).click()
        self.wait_time(3)
        suer = self.driver.find_element(*self.suer).text
        return suer

#精品加入购物车
    def Gouwu(self):
        self.driver.keyevent(4)
        self.wait_time(3)
        self.Swipe(1)
        self.wait_time(3)
        gouwu = self.driver.find_element(*self.home_p).text
        self.driver.find_element(*self.home_page).click()
        self.wait_time(2)
        self.driver.find_element(*self.gouwu).click()
        return gouwu

# 购物车
    def Gouwu_C(self):
        self.wait_time(2)
        self.driver.find_element(*self.gouwu_open).click()
        self.wait_time(2)
        gouwu = self.driver.find_element(*self.home_pa).text
        return gouwu
# 结算
    def jiesuan(self):
        self.driver.keyevent(4)
        self.wait_time(2)
        self.Swipe(2)
        J = self.driver.find_element(*self.jin).text
        return J
    def Jin(self):
        self.wait_time(5)
        self.driver.find_element(*self.home_page).click()
        self.wait_time(1)
        self.driver.find_element(*self.suan).click()
        self.wait_time(2)
        J = self.driver.find_element(*self.jin_a).text
        return J

