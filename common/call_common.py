from selenium.webdriver.common.by import By
from common.call_wechat import wechat
from element.call_element import Element
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#  登录并进入到微商城首页
class Login(Element):
    determine = (By.CLASS_NAME, 'android.widget.Button')  # 地理位置授权
    manuslly_choose = (By.XPATH, "//*[contains(text(), '手动选择站点')]")  # 手动选择站点
    confirm = (By.XPATH, "//*[contains(text(), '确认')]")  # 确认选择地址
    advertising = (By.ID, "newCloseBtn")  # 点击取消弹屏广告

    def wait(self, choose, display):  # 显示等待
        wait = WebDriverWait(self.driver, 20, 0.3).until(choose(display))
        return wait

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


if __name__ == '__main__':
    driver = wechat()
    name = Login(driver)
    name.login()