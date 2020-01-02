from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from selenium.webdriver.common.touch_actions import TouchActions


# 个人信息
class Me_five(Common):

    banghzu = (By.XPATH,'/html/body/div[1]/div[14]/div[1]')
    goumai = (By.XPATH,'/html/body/section/div/ul/a[1]/li')
    fapiao = (By.XPATH,'/html/body/section/div/ul/a[2]/li')
    kefu = (By.XPATH,'/html/body/section/div/ul/a[3]/li')
    peisongshi = (By.XPATH,'/html/body/section/div/ul/a[4]/li')
    peisongfei = (By.XPATH,'/html/body/section/div/ul/a[5]/li')
    shouhou = (By.XPATH,'/html/body/section/div/ul/a[6]/li')
    tuihuan = (By.XPATH,'/html/body/section/div/ul/a[7]/li')
    zixun = (By.XPATH,'/html/body/section/div/ul/a[8]/li')
    changjian = (By.XPATH,'/html/body/section/div/ul/a[9]/li')
    jifen = (By.XPATH,'/html/body/section/div/ul/a[10]/li')
    guanyu = (By.XPATH,'/html/body/section/div/ul/a[11]/li')
    chengping = (By.XPATH,'/html/body/section/div/ul/a[12]/li')
    xianxia = (By.XPATH,'/html/body/section/div/ul/a[13]/li')
    xiazai = (By.XPATH,'/html/body/section/div/ul/a[14]/li')
    gongsi = (By.XPATH,'/html/body/section/div/ul/a[15]/li')
    zhaoshang = (By.XPATH,'/html/body/section/div/ul/a[16]/li')

    def open(self):
        self.base(4)
        self.Swipe(1)
        self.driver.find_element(*self.banghzu).click()


    def Bangzhu(self):
        try:
            num = 0
            while num <= 15:
                if num == 0:
                    self.driver.find_element(*self.goumai).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 1:
                    self.driver.find_element(*self.fapiao).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 2:
                    self.driver.find_element(*self.kefu).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 3:
                    self.driver.find_element(*self.peisongshi).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 4:
                    self.driver.find_element(*self.peisongfei).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 5:
                    self.driver.find_element(*self.shouhou).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 6:
                    self.driver.find_element(*self.tuihuan).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 7:
                    self.driver.find_element(*self.zixun).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 8:
                    self.driver.find_element(*self.changjian).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 9:
                    self.driver.find_element(*self.jifen).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 10:
                    self.driver.find_element(*self.guanyu).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 11:
                    self.driver.find_element(*self.chengping).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 12:
                    self.driver.find_element(*self.xianxia).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 13:
                    self.driver.find_element(*self.xiazai).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 14:
                    self.driver.find_element(*self.gongsi).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
                elif num == 15:
                    self.driver.find_element(*self.zhaoshang).click()
                    self.wait_time(1)
                    self.driver.keyevent(4)
                    self.wait_time(1)
                    num += 1
        except:
            return False
        else:
            return True









