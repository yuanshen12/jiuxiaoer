from appium import webdriver
import uiautomator2
import yaml
import os

#  启动微信并打开微商城

def wechat():
    path = os.path.normpath(os.path.join(os.path.abspath(__file__), '..', '..'))
    with open('{}\\config\\wechat.yaml'.format(path), 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
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
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', wechat)
        driver.implicitly_wait(20)
        choose = data["choose"]
        if choose == 0:  # 进入微商城
            environment = data['environment']
            if environment == '酒小二':
                driver.find_element_by_android_uiautomator('text(\"{}\")'.format(environment)).click()
                driver.find_element_by_android_uiautomator('text(\"我要喝酒\")').click()
            elif environment == '叫酒开发':
                driver.find_element_by_android_uiautomator('text(\"{}\")'.format(environment)).click()
                driver.find_element_by_android_uiautomator('textContains(\"测试商城\")').click()
        elif choose == 1:  # 进入app
            try:
                driver.find_element_by_android_uiautomator('text(\"葡萄酒\")')
            except:
                driver.find_element_by_id("com.callme.mall:id/btn0").click()
                driver.find_element_by_android_uiautomator('text(\"南宁\")').click()
        elif choose == 2:  # 进入小程序
            pass
        return driver


if __name__ == '__main__':
    wechat()
