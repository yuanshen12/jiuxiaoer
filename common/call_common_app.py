from selenium.webdriver.common.by import By
from element.call_element import Element
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import yaml
import time, os


def config_yaml():  # 获取配置文件yaml信息
    path = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", ".."))
    with open("{}/config/config.yaml".format(path), 'r', encoding='utf-8') as file:
        date = yaml.safe_load(file)
        return date


class Login(Element):
    call_ad = (By.ID, "com.callme.mall:id/close")  # 去掉广告
    call_login_name = (By.ID, "com.callme.mall:id/loginType")  # 账号登录
    call_login_user = (By.ID, "com.callme.mall:id/username")  # 账号
    call_password = (By.ID, "com.callme.mall:id/password")  # 密码
    call_login = (By.ID, "com.callme.mall:id/login")  # 登录
    call_login_wechat = (By.ID, "com.callme.mall:id/login_weixin")  # 微信授权登录
    call_wechat = (By.ID, "com.callme.mall:id/btn1")  # 同意

    def wait(self, choose, display):  # 显示等待
        wait = WebDriverWait(self.driver, 20, 0.3).until(choose(display))
        return wait

    def ad(self):  # 去广告
        try:
            self.driver.find_element(*self.call_ad).click()
        except NoSuchElementException:
            pass

    def login(self, choose=0):  # 登录
        data = config_yaml()
        if choose == 0:
            self.wait(EC.visibility_of_element_located, self.call_login_name).click()
            self.wait(EC.visibility_of_element_located, self.call_login_user).send_keys(data['login'])
            self.wait(EC.visibility_of_element_located, self.call_password).send_keys(data['password'])
            self.wait(EC.visibility_of_element_located, self.call_login).click()
        elif choose == 1:
            self.wait(EC.visibility_of_element_located, self.call_login_wechat).click()
            self.wait(EC.visibility_of_element_located, self.call_wechat).click()

    @staticmethod
    def get_data(line):  # 参数
        csv_path = os.path.normpath(os.path.join(os.path.abspath(__file__), '..', '..'))
        with open('{}/data/app.csv'.format(csv_path), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    name = Login()
    name.get_data()
