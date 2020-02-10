from selenium.webdriver.common.by import By
from wechat.common.call_wechat import wechat
from wechat.element.call_element import Element
from time import sleep
import yaml
import os


#  登录并进入到微商城首页
# noinspection PyBroadException
class Login(Element):
    determine = (By.CLASS_NAME, 'android.widget.Button')  # 地理位置授权
    manuslly_choose = (By.XPATH, "//*[contains(text(), '手动选择站点')]")
    confirm = (By.XPATH, "//*[contains(text(), '确认')]")
    advertising = (By.ID, "newCloseBtn")

    def __init__(self, driver):
        super().__init__(driver)
        path = os.path.normpath(os.path.join(os.path.abspath(__file__), '..', '..'))
        file = open("{}\\confing\\wechat.yaml".format(path), "r", encoding="utf-8")
        data = yaml.safe_load(file)
        choose = data["environment"]
        if choose == '酒小二':
            driver.find_element_by_android_uiautomator('text(\"{}\")'.format(choose)).click()
            driver.find_element_by_android_uiautomator('text(\"我要喝酒\")').click()
        elif choose == '叫酒开发':
            driver.find_element_by_android_uiautomator('text(\"{}\")'.format(choose)).click()
            driver.find_element_by_android_uiautomator('textContains(\"测试商城\")').click()

    def time(self, sp):  # 隐式等待时间
        activity = self.driver.current_activity
        self.driver.wait_activity(activity, sp)

    def webview(self, H5=()):  # 切换H5页面
        if H5 == 5:
            sleep(2)
            self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
            handles = self.driver.window_handles
            sleep(2)
            self.driver.switch_to.window(handles[0])
        else:
            self.driver.switch_to.context('NATIVE_APP')

    def advertisement(self):  # 去广告
        try:
            sleep(3)
            self.driver.find_element(*self.advertising).click()
        except:
            pass

    def login(self):  # 登录并进入微商城首页步骤
        call_title = '正在进入商城'
        self.webview(5)
        title = self.driver.title
        if call_title not in title:
            self.advertisement()
        else:
            self.driver.find_element(*self.manuslly_choose).click()
            sleep(4)
            self.driver.find_element(*self.confirm).click()
            sleep(3)
            self.advertisement()


if __name__ == '__main__':
    driver = wechat()
    Login(driver)
