from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
import logging
from selenium.webdriver.common.touch_actions import TouchActions

# 发现
class discover(Common):
    fianax = (By.XPATH, '/html/body/div[10]/div/div[2]/div[3]')
    jia = (By.XPATH,'//*[@id="visit-302"]/div[2]/div[1]/div/div[1]/div[4]/table/tbody/tr/td[2]/div/button[2]')
    jia_a = (By.XPATH,'//*[@id="visit-302"]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr/td[2]/div/button[2]')
    gouwu = (By.XPATH,'/html/body/div[8]')
    che = (By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[3]')
    xiang = (By.XPATH,'//*[@id="visit-302"]/div[2]/div[1]/div/div[1]/div[3]/div[1]')
    xiang_a = (By.XPATH,'//*[@id="visit-302"]/div[2]/div[1]/div/div[2]/div[1]/div[1]')
    suan = (By.XPATH,'//*[@id="paddingTop"]/section/div[3]/div/div[1]/div[1]/strong')
    like = (By.XPATH,"//*[contains(text(), '立即购买')]")
    suan_a = (By.XPATH,'//*[@id="footer"]/div/div/span[2]/span')

    one = (By.XPATH,'/html/body/div[1]/div/ul/li[1]/div[1]')
    two = (By.XPATH,'/html/body/div[1]/div/ul/li[2]/div[1]')
    three = (By.XPATH,'/html/body/div[1]/div/ul/li[3]/div[1]')


    def Faxian(self):
        try:
            self.driver.find_element(*self.jia).click()
        except:
            self.driver.find_element(*self.jia_a).click()
        self.driver.find_element(*self.gouwu).click()
        self.wait_time(1)
        try:
            self.driver.find_element(*self.che)
            return True
        except:
            return False

    def Qiehuan(self,num):
        self.base(1)
        logging.info('============Qiehuan==============')
        self.wait_time(2)
        try:
            if num == 0:
                el = self.driver.find_element(*self.one)
                TouchActions(self.driver).tap(el).perform()  # tap点击选址
            elif num == 1:
                el1 = self.driver.find_element(*self.two)
                TouchActions(self.driver).tap(el1).perform()  # tap点击选址
            elif num == 2:
                el2 = self.driver.find_element(*self.three)
                TouchActions(self.driver).tap(el2).perform()  # tap点击选址
        except:
            return False
        else:
            return True

    def Xiangqin(self):
        self.driver.keyevent(4)
        try:
            self.driver.find_element(*self.xiang).click()
        except:
            self.driver.find_element(*self.xiang_a).click()
        SUAN = self.driver.find_element(*self.suan).text
        return int(SUAN)
    def Xiang(self):
        self.driver.find_element(*self.like).click()
        SUAN = self.driver.find_element(*self.suan_a).text
        return int(float(SUAN))







