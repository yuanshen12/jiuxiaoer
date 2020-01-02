from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common

# 个人信息
class Me_to(Common):
    chengzhangzhi = (By.XPATH,'/html/body/div[1]/div[1]/div/div[4]')
    jifen = (By.XPATH,'/html/body/div[1]/div[3]/div[1]')
    mingxi = (By.XPATH,'//*[@id="ALL"]')
    shouru = (By.XPATH,'//*[@id="IN"]')
    zhichu = (By.XPATH,'//*[@id="OUT"]')
    youhuijuan = (By.XPATH,'/html/body/div[1]/div[3]/div[3]')
    yishiyong = (By.XPATH,'//*[@id="USED"]')
    yiguoqi = (By.XPATH,'//*[@id="OVER_DUE"]')
    jijiangdaoqi = (By.XPATH,'//*[@id="NEAR_DUE"]')
    weishiyong = (By.XPATH,'//*[@id="NEAR_DUE"]')


    def Chengzhangzhi(self):
        self.base(4)
        try:
              self.driver.find_element(*self.chengzhangzhi).click()
        except:
            return False
        else:
            return True

    def Jifen(self):
        self.driver.keyevent(4)
        try:
            self.driver.find_element(*self.jifen).click()
        except:
            return False
        else:
            return True

    def Xiangxi(self):
        try:
            unm = 0
            while unm < 3:
                if unm == 0:
                    self.driver.find_element(*self.mingxi).click()
                    unm += 1
                elif unm == 1:
                    self.driver.find_element(*self.shouru).click()
                    unm += 1
                elif unm == 2:
                    self.driver.find_element(*self.zhichu).click()
                    unm += 1
        except:
            return False
        else:
            return True


    def Youhuijuan(self):
        self.driver.keyevent(4)
        try:
            self.driver.find_element(*self.youhuijuan).click()
        except:
            return False
        else:
            return True

    def Y_xiangqin(self):
        try:
            num = 0
            while num < 4:
                if num == 0:
                    self.driver.find_element(*self.yishiyong).click()
                    num += 1
                elif num == 1:
                    self.driver.find_element(*self.yiguoqi).click()
                    num += 1
                elif num == 2:
                    self.driver.find_element(*self.jijiangdaoqi).click()
                    num += 1
                elif num == 3:
                    self.driver.find_element(*self.weishiyong).click()
                    num += 1
        except:
            return False
        else:
            return True


