from selenium.webdriver.common.by import By
from common.call_wechat import wechat
from element.call_element import Element
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time, os


#  微商城
class Login(Element):
    determine = (By.CLASS_NAME, 'android.widget.Button')  # 地理位置授权
    manuslly_choose = (By.XPATH, "//*[contains(text(), '手动选择站点')]")  # 手动选择站点
    confirm = (By.XPATH, "//*[contains(text(), '确认')]")  # 确认选择地址
    advertising = (By.ID, "newCloseBtn")  # 点击取消弹屏广告

    call_ad = (By.ID, "com.callme.mall:id/close")  # 去掉广告
    call_home = (By.ID, "com.callme.mall:id/ll_tap")  # 首页菜单

    def wait(self, choose, display):  # 显示等待
        wait = WebDriverWait(self.driver, 20, 0.3).until(choose(display))
        return wait

    def webview(self, H5=()):  # 切换H5页面
        if H5 == 5:
            sleep(2)
            # print(self.driver.contexts)  # 获取H5页面的activity
            self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
            handles = self.driver.window_handles
            sleep(2)
            self.driver.switch_to.window(handles[0])
        else:
            self.driver.switch_to.context('NATIVE_APP')

    def advertisement(self):  # 去广告
        try:
            self.wait(EC.element_to_be_clickable, self.advertising).click()
        except:
            pass

    def login(self):  # 登录并进入微商城首页步骤
        call_title = '正在进入商城'
        self.webview(5)
        title = self.driver.title
        if call_title not in title:
            self.advertisement()
        else:
            self.wait(EC.element_to_be_clickable, self.manuslly_choose).click()
            self.wait(EC.element_to_be_clickable, self.confirm).click()
            self.advertisement()

# APP商城
    def home(self, num=0):  # 首页底部菜单
        home = self.wait(EC.presence_of_all_elements_located, self.call_home)[num]
        return home

    def ad(self):  # 去广告
        try:
            self.wait(EC.element_to_be_clickable, self.call_ad).click()
        except:
            pass

    @staticmethod
    def get_data(line):  # 参数
        csv_path = os.path.normpath(os.path.join(os.path.abspath(__file__), '..', '..'))
        with open('{}/data/app.csv'.format(csv_path), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = wechat()
    name = Login(driver)
    name.ad()
