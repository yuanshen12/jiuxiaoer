from Base.BaseYaml import get_yaml
from appium import webdriver
from Base.BaseXlm import get_excel_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from time import sleep

data = get_yaml("../Yaml/config.yaml")


def app():
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
        self.driver = app()
        # self.logTest = myLog().getLog("chrome")

    def teardown_class(self):
        self.driver.close_app()


if __name__ == '__main__':
    app()
