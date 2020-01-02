from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common

# 个人信息
class Geren(Common):
    touxiang = (By.XPATH,'/html/body/div[1]/div[1]/div/div[1]')
    nicheng = (By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div[2]/i')
    niinput = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/input')
    baocun = (By.XPATH, "/html/body/div[3]/div[2]/div[3]/button[2]")
    nicheng_text = (By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div[1]')
    xingbie = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div[2]/i')
    nv = (By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[1]")
    queding = (By.XPATH, "//*[contains(text(), '确定')]")
    nv_text = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div[1]')
    shengri = (By.XPATH,'/html/body/div[1]/div[6]/div/div[2]/div[2]/i')
    list = (By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[3]/div[1]/ul/li')
    queding1 = (By.XPATH,'/html/body/div[5]/div[2]/div[1]/span[2]')
    shengre_text = (By.XPATH,'/html/body/div[1]/div[6]/div/div[2]/div[1]')
    zidingyi = ( By.XPATH,'/html/body/div[1]/div[9]/div/i')
    oninput = (By.XPATH,'/html/body/div[2]/div[2]/div[2]/input')
    baocun1 = (By.XPATH,'/html/body/div[2]/div[2]/div[3]/button[2]')
    baocun_text = (By.XPATH,'/html/body/div[1]/div[9]/div[1]')

    shan = (By.XPATH,'/html/body/div[1]/div[9]/button')
    shan_1 = (By.XPATH,'/html/body/div[1]/div[9]/button/i')



    def geren(self):
        self.base(4)
        self.driver.find_element(*self.touxiang).click()

    def Nicheng(self):
        self.geren()
        self.driver.find_element(*self.nicheng).click()
        self.driver.find_element(*self.niinput).send_keys('道德许可')
        self.driver.find_element(*self.baocun).click()
        self.wait_time(2)
        el = self.driver.find_element(*self.nicheng_text).text
        return el

    def Xinbie(self):
        self.driver.find_element(*self.xingbie).click()
        self.wait_time(2)
        self.driver.find_element(*self.nv).click()
        self.driver.find_element(*self.queding).click()
        EL = self.driver.find_element(*self.nv_text).text
        return EL

    def Shengri(self):
        self.wait_time(2)
        self.driver.find_element(*self.shengri).click()
        self.wait_time(2)
        EL = self.driver.find_element(*self.list).text
        return EL

    def Shengre(self):
        self.driver.find_element(*self.queding1).click()
        EL = self.driver.find_element(*self.shengre_text).text
        return EL

    def Xinqu(self):
        self.wait_time(2)
        self.driver.find_element(*self.zidingyi).click()
        self.driver.find_element(*self.oninput).send_keys('健康饮酒')
        self.driver.find_element(*self.baocun1).click()
        EL = self.driver.find_element(*self.baocun_text).text
        return EL

    def Xinqu_S(self):
        try:
            self.driver.find_element(*self.shan).click()
            self.driver.find_element(*self.shan_1).click()
        except:
            return False
        else:
            return True







