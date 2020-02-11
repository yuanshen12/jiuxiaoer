from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from wechat.common.call_wechat import wechat
from wechat.common.call_common import Login
from wechat.operation.home.call_home import Home
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class Locate(Login):
    call_address = (By.CLASS_NAME, 'address-name')  # 定位页面选择区域
    call_seek = (By.CLASS_NAME, "input-box")  # 定位页面点开搜索
    call_map = (By.CLASS_NAME, "map-btn")  # 定位页面地图模式
    call_info = (By.CLASS_NAME, "info")  # 定位页面当前地址（0,1）
    call_input = (By.XPATH, "/html/body/sub-head/div[3]/input")  # 定位页面输入搜索
    call_location = (By.CLASS_NAME, "location")  # 定位页面收货地址（0,1,2……）
    call_add = (By.CLASS_NAME, 'new-addr')  # 定位页面新增地址
    call_locate = (By.CLASS_NAME, 'addr')  # 定位页面附近地址（0,1,2,……）

    def locate_address(self, num):  # 定位页面选择区域(0,1,2,3……）
        self.wait(EC.element_to_be_clickable, self.call_address).click()
        # name = self.wait(EC.presence_of_all_elements_located, self.call_name)[num]
        # TouchActions(self.driver).tap(name).perform()

    def locate_seek(self, num):  # 定位页面点进搜索
        self.wait(EC.element_to_be_clickable, self.call_seek).click()
        self.wait(EC.presence_of_element_located, self.call_input).send_keys(num)

    def locate_map(self):  # 定位页面点开地图模式
        self.wait(EC.element_to_be_clickable, self.call_map).click()

    def locate_info_text(self, num=0):  # 定位地址当前地址文本
        sleep(2)
        name = self.wait(EC.presence_of_all_elements_located, self.call_info)[num].text
        return name

    def locate_info(self, num):  # 定位页面当前地址(0选择地址，1重新定位）
        name = self.wait(EC.presence_of_all_elements_located, self.call_info)[num]
        if name.text == "定位中...":
            sleep(2)
            name.click()

    def locate_location(self, num):  # 定位页面收货地址（0,1,2……）
        while True:
            try:
                self.wait(EC.visibility_of_any_elements_located, self.call_location)[num].click()
                self.swipe(600, 1000, 600, 600, 500)
            except:
                pass
            else:
                break

    def locate_add(self):  # 定位页面点开新增地址
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_element_located, self.call_add).click()
            except:
                pass
            else:
                break

    def locate_locate(self):
        self.login()
        Home(driver).home_location()
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_locate).click()
            except:
                pass
            else:
                break







if __name__ == '__main__':
    driver = wechat()
    PI = Locate(driver)
    PI.locate_add()
