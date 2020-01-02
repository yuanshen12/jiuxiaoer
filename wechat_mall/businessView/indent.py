from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from selenium.webdriver.common.touch_actions import TouchActions

# 发现
class indent(Common):
    quanbu = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[1]')
    daifu = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[2]')
    daifa = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[3]')
    daishou = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[4]')
    daiping = (By.XPATH,'/html/body/div[1]/div[1]/div/ul/li[5]')
    likexiadan = (By.XPATH,"//*[contains(text(), '立即下单')]")

    def open(self):
        self.base(3)

    def qiehuan(self,num):
        try:
            if num ==0:
                el = self.driver.find_element(*self.quanbu)
                TouchActions(self.driver).tap(el).perform()  # tap点击选址
            elif num ==1:
                el = self.driver.find_element(*self.daifu)
                TouchActions(self.driver).tap(el).perform()  # tap点击选址
            elif num ==2:
               el = self.driver.find_element(*self.daifa)
               TouchActions(self.driver).tap(el).perform()  # tap点击选址
            elif num ==3:
                el = self.driver.find_element(*self.daishou)
                TouchActions(self.driver).tap(el).perform()  # tap点击选址
            elif num ==4:
                el = self.driver.find_element(*self.daiping)
                TouchActions(self.driver).tap(el).perform()  # tap点击选址

        except:
            return False
        else:
            self.wait_time(2)
            return True

    def like(self):
        try:
            self.driver.find_element(*self.likexiadan).click()
            try:
                return True
            except:
                return False
        except:
            True

