from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common

# 搜索
class sousou(Common):

    shouye_sou = (By.XPATH,'//*[@id="header"]/aside[2]/input')
    remen = (By.XPATH,'/html/body/div[1]/div[2]/sapn[1]')
    gouwuche = (By.XPATH,'/html/body/nav/article/aside[1]/div[1]/div')
    kong = (By.XPATH,'/html/body/div[1]')
    jiage = (By.XPATH,'/html/body/section/article/ul/li[1]/a/div[4]/span')
    jia = (By.XPATH,'/html/body/section/article/ul/li[1]/a/div[5]/aside/div[1]')
    jiarugouwuche = (By.XPATH,"//*[contains(text(), '加入购物车')]")
    jiage1 = (By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[4]/div[2]')
    lijigoumai = (By.XPATH,"//*[contains(text(), '立即购买')]")
    jiage2 = (By.XPATH,'//*[@id="footer"]/div/div/span[2]/span')


    def Sou_qingouwuche(self):
        self.driver.find_element(*self.shouye_sou).click()
        self.driver.find_element(*self.remen).click()
        self.driver.find_element(*self.gouwuche).click()
        self.gouwu_shanchu()
        self.driver.keyevent(4)
        self.wait_time(2)
        T = self.driver.find_element(*self.jiage).text
        return T

    def Sou_jiarugouwuche(self):
        self.driver.find_element(*self.jia).click()
        self.wait_time(3)
        self.driver.find_element(*self.jiarugouwuche).click()
        self.wait_time(3)
        self.driver.find_element(*self.gouwuche).click()
        self.wait_time(3)
        T = self.driver.find_element(*self.jiage1).text
        return T

    def Jiesuan(self):
        self.driver.keyevent(4)
        self.wait_time(3)
        T = self.driver.find_element(*self.jiage).text
        return T

    def Jiesuan1(self):
        self.wait_time(2)
        self.driver.find_element(*self.jia).click()
        self.wait_time(3)
        self.driver.find_element(*self.lijigoumai).click()
        self.wait_time(3)
        T = self.driver.find_element(*self.jiage2).text
        return T










