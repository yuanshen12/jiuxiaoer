from selenium.webdriver.common.by import By
from wechat.common.call_wechat import Wechat
from wechat.common.call_common import Login
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class Locate(Login):
    use_locate = (By.ID, "cityName")
    determine = (By.CLASS_NAME, 'android.widget.Button')
    choose_locate = (By.CLASS_NAME, "address-name")
    choose_locates = (By.XPATH, "//*[text()='贵阳']")
    choose_seek = (By.XPATH, "/html/body/sub-head/div[3]/input")
    choose_seeks = (By.XPATH, '/html/body/div[1]/div/div[3]/input')
    choose_seek_use = (By.CLASS_NAME, 'wrap')

    def call_use_locate(self):  # 首页进入定位设置页面
        self.login()
        try:
            self.driver.find_element(*self.use_locate).click()
        except:
            self.webview(5)
            self.driver.find_element(*self.use_locate).click()

    def call_locate(self, choose):  # 定位页面
        if choose == 0:
            self.driver.find_element(*self.choose_locate).click()
            ch = self.driver.find_element(*self.choose_locates)
            num = ch.text
            yuan = open("../operation/text", "w+", encoding='utf-8')
            yuan.write(num)
            sleep(4)
            TouchActions(self.driver).tap(ch).perform()
        elif choose == 1:
            self.driver.find_element(*self.choose_seek).click()
            self.driver.find_element(*self.choose_seeks).send_keys('火车站')
            sleep(3)
            self.driver.find_elements(*self.choose_seek_use)[1].click()
            sleep(3)
        elif choose == 2:
            pass




if __name__ == '__main__':
    driver = Wechat()
    PI = Locate(driver)
    PI.call_use_locate()
    PI.call_locate(0)
    PI.call_locate(1)

