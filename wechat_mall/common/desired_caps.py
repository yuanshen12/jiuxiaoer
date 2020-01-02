from appium import webdriver
import yaml
import logging.config
import os

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

# 调用APP配置信息
def appium_desired():
    with open('../config/app_config.yaml','r',encoding='utf-8') as file:
     data=yaml.safe_load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app']=app_path

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    suer = data['environment']
    if suer == '酒小二':
        driver.find_element_by_android_uiautomator('text(\"酒小二\")').click()
        driver.find_element_by_android_uiautomator('text(\"我要喝酒\")').click()
    else:
        driver.find_element_by_android_uiautomator('text(\"叫酒开发\")').click()
        driver.find_element_by_android_uiautomator('text(\"测试商城\")').click()
    return driver

if __name__ == '__main__':
    appium_desired()