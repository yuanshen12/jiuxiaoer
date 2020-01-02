import logging
from selenium.webdriver.common.by import By
from wechat_test.common.desired_caps import appium_desired
from wechat_test.common.common_fun import Common,NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions

class Scation(Common):
    csv_file='../data/account.csv'  # 参数路径
    scation_a = (By.ID,"cityName")  # 首页进入定位页面
    determine = (By.ID,'com.tencent.mm:id/b29')  # 点去弹窗
    locate = (By.CLASS_NAME, "address-name")  # 切换
    location = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[7]/li[5]/div")  # 切换到贵阳
    seek = (By.XPATH, "/html/body/sub-head/div[3]/input")  # 切换并输入贵阳火车站
    suer_one = (By.XPATH, "/html/body/search-win/div[4]/div/div[2]/div[2]/div[2]")  # 点击确定切换站点

    def scation(self):
        Common.login_test(self)
        self.Time(10)
        try:
            self.driver.find_element(*self.scation_a).click()
        except:
            Common.login_test(self)
            self.driver.find_element(*self.scation_a).click()
        try:
            self.driver.switch_to.context('NATIVE_APP')
            determine = self.driver.find_element(*self.determine)
        except NoSuchElementException:
            logging.info('no window_handles')
        else:
            determine.click()
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

    def scation_guiyang(self):
        Scation.scation(self)
        data = Common.get_csv_data(self,self.csv_file,1)
        self.driver.find_element(*self.locate).click()
        location = self.driver.find_element(*self.location)
        TouchActions(self.driver).tap(location).perform()
        self.Time(3)
        self.driver.find_element(*self.seek).send_keys(data[1])
        self.Time(3)
        self.driver.find_element(*self.suer_one).click()
        self.Time(5)
        title = self.driver.title
        return title

    def login_guiyang(self):
        self.login_test()
        data = Common.get_csv_data(self, self.csv_file, 1)
        title = self.driver.title
        if data[1] in title:
            pass
        else:
            Scation.scation_guiyang(self)
        self.advertisement()

if __name__ == '__main__':
     driver = appium_desired()
     num = Scation(driver)
     num.login_guiyang()

