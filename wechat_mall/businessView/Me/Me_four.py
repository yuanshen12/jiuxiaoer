from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from selenium.webdriver.common.touch_actions import TouchActions


# 个人信息
class Me_four(Common):
    zuji = (By.XPATH,'/html/body/div[1]/div[8]/div[1]/div/div[2]')
    hongjiu = (By.XPATH,'/html/body/div[1]/ul/li[2]')
    baijiu = (By.XPATH,'/html/body/div[1]/ul/li[3]')
    yangjiu = (By.XPATH,'/html/body/div[1]/ul/li[4]')

    shoucang = (By.XPATH,'/html/body/div[1]/div[8]/div[3]/div/div[2]')

    wenda = (By.XPATH,'/html/body/div[1]/div[10]/div[1]/div/div[2]')
    huida = (By.XPATH,'/html/body/subheader/div/div[3]/button')
    tiwen = (By.XPATH,'//*[@id="btnQuestion"]')

    huiyuan =(By.XPATH,'/html/body/div[1]/div[10]/div[3]/div')

    fapiao = (By.XPATH,'/html/body/div[1]/div[12]/div[1]/div/div[2]')
    zhizhi =(By.XPATH,'//*[@id="content"]/div/subheader/div/div[3]')
    dianzi = (By.XPATH,'//*[@id="content"]/div/subheader/div/div[1]')

    dizhi = (By.XPATH,'/html/body/div[1]/div[12]/div[3]/div/div[2]')
    xinzeng = (By.XPATH, "//*[contains(text(), '新增收货地址')]")
    xingming =(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/input')
    pthon = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/input')
    dizhi1 = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[4]/div[2]/div[1]')
    dizhi2 = (By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/div[3]/div/ul/li[1]')
    menpai = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[5]/div[2]/input')
    gongsi = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[7]/div/div/div/div[2]')
    baocun = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div')
    shanchu = (By.XPATH, "//*[contains(text(), '删除')]")
    queding = (By.XPATH, "//*[contains(text(), '确定')]")

    def open(self):
        self.base(4)

    def Zuji(self,num):
        if num == 1:
            try:
                self.driver.find_element(*self.zuji).click()
                unm = 0
                while unm < 3:
                    if unm == 0:
                        el = self.driver.find_element(*self.hongjiu)
                        TouchActions(self.driver).tap(el).perform()  # tap点击选址
                        unm += 1
                    if unm == 1:
                        el1 = self.driver.find_element(*self.baijiu)
                        TouchActions(self.driver).tap(el1).perform()  # tap点击选址
                        unm += 1
                    if  unm == 2:
                        el2 = self.driver.find_element(*self.yangjiu)
                        TouchActions(self.driver).tap(el2).perform()  # tap点击选址
                        unm += 1
            except:
                return False
            else:
                self.driver.keyevent(4)
                return True
        if num == 2:
            try:
                self.driver.find_element(*self.shoucang).click()
                unm = 0
                while unm < 3:
                    if unm == 0:
                        el = self.driver.find_element(*self.hongjiu)
                        TouchActions(self.driver).tap(el).perform()  # tap点击选址
                        unm += 1
                    if unm == 1:
                        el1 = self.driver.find_element(*self.baijiu)
                        TouchActions(self.driver).tap(el1).perform()  # tap点击选址
                        unm += 1
                    if unm == 2:
                        el2 = self.driver.find_element(*self.yangjiu)
                        TouchActions(self.driver).tap(el2).perform()  # tap点击选址
                        unm += 1
            except:
                return False
            else:
                self.driver.keyevent(4)
                return True
        if num == 3:
            try:
                self.driver.find_element(*self.wenda).click()
                unm = 0
                while unm < 2:
                    if unm == 0:
                        self.driver.find_element(*self.huida).click()
                        unm += 1
                    elif unm == 1:
                        self.driver.find_element(*self.tiwen).click()
                        unm += 1
            except:
                return False
            else:
                self.driver.keyevent(4)
                return True
        if num == 4:
            try:
                self.driver.find_element(*self.huiyuan).click()
            except:
                return False
            else:
                self.driver.keyevent(4)
                return True
        if num == 5:
            self.Swipe(1)
            try:
                self.driver.find_element(*self.fapiao).click()
                unm = 0
                while unm < 2:
                    if unm == 0:
                        self.driver.find_element(*self.zhizhi).click()
                        unm += 1
                    elif unm == 1:
                        self.driver.find_element(*self.dianzi).click()
                        unm += 1
            except:
                return False
            else:
                self.driver.keyevent(4)
                return True
        if num == 6:
            self.Swipe(1)
            self.driver.find_element(*self.dizhi).click()
            self.wait_time(2)
            try:
                self.driver.find_element(*self.xinzeng).click()
                self.driver.find_element(*self.xingming).send_keys('自动化测试')
                EL = self.driver.find_element(*self.pthon)
                EL.clear()
                EL.send_keys(13558252700)
                self.driver.find_element(*self.dizhi1).click()
                self.wait_time(15)
                self.driver.find_element(*self.dizhi2).click()
                self.driver.find_element(*self.menpai).send_keys("琅西四组")
                self.driver.find_element(*self.gongsi).click()
                self.driver.find_element(*self.baocun).click()
            except:
                return False
            else:
                self.wait_time(3)
                self.driver.find_element(*self.shanchu).click()
                self.driver.find_element(*self.queding).click()
                return True














