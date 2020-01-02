from selenium import webdriver
from appium import webdriver
import logging
import logging.config

# 打开微商城并去广告
class Login:

    def open(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'LKX7N17B09002482',
            'platformVersion': '9',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'noReset': 'True',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }
        logging.info('start app...')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text(\"酒小二\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"我要喝酒\")').click()
        self.wait()
        self.advertisement_open()
        return self.driver


    # 隐式等待
    def wait(self):
        logging.info('====wait======')
        self.driver.wait_activity(".base.ui.MainActivity", 5)

    # 切换H5
    def webview(self):
        logging.info('====webview======')
        self.wait()
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 去广告
    def advertisement(self):
        logging.info('====advertisement======')
        try:
            self.wait()
            self.webview()
            while True:
                title = self.driver.title
                if "酒小二" in title:
                    break
                elif "正在进入商城" in title:
                    self.driver.find_element_by_xpath('//*[contains(text(), "手动选择站点")]').click()
                    self.wait()
                    self.driver.find_element_by_xpath('//*[contains(text(), "确认")]').click()
                elif "搜一搜" in title:
                    break
                else:
                    Login.open(self)
            self.driver.find_element_by_id('newCloseBtn').click()
        except:
            pass

    def advertisement_open(self):
        try:
            self.advertisement()
        except:
            logging.info('no advertisement')


if __name__ == '__main__':
    L = Login()
    L.open()