from appium import webdriver
from common.call_common import config_yaml
from time import sleep
import pytest


#  启动微信并打开微商城

def wechat():
    data = config_yaml()
    wechat = {}
    wechat['platformName'] = data['platformName']
    wechat['platformVersion'] = data['platformVersion']
    wechat['deviceName'] = data['deviceName']
    wechat['appName'] = data['appName']
    wechat['appPackage'] = data['appPackage']
    wechat['appActivity'] = data['appActivity']
    wechat['chromeOptions'] = data['chromeOptions']
    wechat['noReset'] = data['noReset']
    wechat['unicodeKeyboard'] = data['unicodeKeyboard']
    wechat['resetKeyboard'] = data['resetKeyboard']
    wechat['automationName'] = data['automationName']
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', wechat)
    return driver


class TestCase:

    def setup_class(self):
        print('py.test类执行前')
        data = config_yaml()
        choose = data["choose"]
        self.driver = wechat()
        self.driver.implicitly_wait(20)
        if choose == 0:  # 进入微商城
            environment = data['environment']
            if environment == '酒小二':
                self.driver.find_element_by_android_uiautomator('text(\"{}\")'.format(environment)).click()
                self.driver.find_element_by_android_uiautomator('text(\"我要喝酒\")').click()
            elif environment == '叫酒开发':
                self.driver.find_element_by_android_uiautomator('text(\"{}\")'.format(environment)).click()
                self.driver.find_element_by_android_uiautomator('textContains(\"测试商城\")').click()
        elif choose == 1:  # 进入app
            # try:  # 首次打开app
            #     self.driver.find_element_by_id("com.callme.mall:id/agree").click()
            #     [self.driver.swipe(900, 1200, 100, 1200, 500) for x in range(6)]
            #     self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            # except:
            #     pass
            pass

    def teardown_class(self):
        print('py.text类执行后')
        sleep(3)
        self.driver.close_app()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'call_wechat.py'])
