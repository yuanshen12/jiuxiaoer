from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common

# 个人信息
class Me_three(Common):
    wodedingdan = (By.XPATH,'/html/body/div[1]/div[5]/div[1]/div[1]')
    dingdan_jin = (By.XPATH,'/html/body/div[1]/div[5]/div[1]/div[2]/i')
    daifu = (By.XPATH,'/html/body/div[1]/div[5]/div[2]/ul/li[1]')
    daifu_a = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[2]/div')
    daifa = (By.XPATH,'/html/body/div[1]/div[5]/div[2]/ul/li[3]')
    daishou = (By.XPATH,'/html/body/div[1]/div[5]/div[2]/ul/li[5]')
    daiping = (By.XPATH,'/html/body/div[1]/div[5]/div[2]/ul/li[7]')
    daifa_a = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[3]')
    daishou_a = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[4]')
    daiping_a = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[5]')

    def Wo(self):
        self.wait_time(3)
        self.base(4)
        el = self.driver.find_element(*self.wodedingdan).text
        return el

    def Wo_ding(self):
        self.driver.find_element(*self.dingdan_jin).click()
        tetle = self.driver.title
        return tetle

    def Daifu(self,num):
        if num == 0:
            self.driver.keyevent(4)
            EL = self.driver.find_element(*self.daifu).text
            return EL
        elif num == 1:
            self.driver.keyevent(4)
            EL = self.driver.find_element(*self.daifa).text
            return EL
        elif num == 2:
            self.driver.keyevent(4)
            EL = self.driver.find_element(*self.daishou).text
            return EL
        elif num == 3:
            self.driver.keyevent(4)
            EL = self.driver.find_element(*self.daiping).text
            return EL


    def Daifu_A(self,num):
        if num == 0:
            self.driver.find_element(*self.daifu).click()
            EL = self.driver.find_element(*self.daifu_a).text
            return EL
        elif num == 1:
            self.driver.find_element(*self.daifa).click()
            EL = self.driver.find_element(*self.daifa_a).text
            return EL
        elif num == 2:
            self.driver.find_element(*self.daishou).click()
            EL = self.driver.find_element(*self.daishou_a).text
            return EL
        elif num == 3:
            self.driver.find_element(*self.daiping).click()
            EL = self.driver.find_element(*self.daiping_a).text
            return EL









