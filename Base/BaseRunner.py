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


class Element():
    def __init__(self, driver):
        self.driver = app()

    def get_element(self, path, name):
        data = get_excel_data(path, name)
        for element in data:
            get_elements = lambda *display: WebDriverWait(self.driver, 20, 0.3) \
                .until(EC.visibility_of_any_elements_located(display))
            get_element = lambda *display: WebDriverWait(self.driver, 20, 0.3) \
                .until(EC.visibility_of_element_located(display))
            print("element[3]这是定位方式：{}".format(element[3]))
            print("element[4]这是定位元素：{}".format(element[4]))
            print("element[5]这是操作方式：{}".format(element[5]))
            print("element[6]这是输入数据：{}".format(element[6]))
            if len(element[4]) == 0:
                break
            elif element[4] == "time":
                sleep(element[5])
            else:
                if element[5] == "click":
                    try:
                        get_element(element[3], element[4]).click()
                    except selenium.common.exceptions.TimeoutException:
                        print("---寻找元素超时---")
                        return False
                    except selenium.common.exceptions.NoSuchElementException:
                        print("---寻找元素不存在---")
                        return False
                elif element[5] == "send_keys":
                    get_element(element[3], element[4]).send_keys(element[6])
                elif element[5] == "elements":
                    get_elements(element[3], element[4])[int(element[6])].click()
                elif element[5] == "text":
                    text = get_element(element[3], element[4]).text
                    return text


if __name__ == '__main__':
    data = Element(None).get_element("../Xls/locate.xls", "locate")
    print(data)
