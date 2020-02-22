from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from appmall.home.call_home import Home
from time import sleep


# 首页进入的定位页面
class Locate(Login):
    call_address = (By.ID, "com.callme.mall:id/station")  # 定位切换区域
    call_seek = (By.ID, "com.callme.mall:id/content")  # 定位搜索区域
    call_search = (By.ID, "com.callme.mall:id/addreLayout")  # 确定贵阳站
    call_home = (By.ID, "com.callme.mall:id/ll_tap")  # 首页菜单
    call_locate = (By.ID, "com.callme.mall:id/mapTipsLayout")  # 地图模式
    call_update = (By.ID, "com.callme.mall:id/getLocationBtn")  # 地图模式更新
    call_list = (By.ID, "com.callme.mall:id/nameLayout")  # 地图模式位置列表
    call_history = (By.ID, "com.callme.mall:id/clean_history")  # 地图模式历史搜索删除
    call_cancel = (By.ID, "com.callme.mall:id/cancel")  # 定位搜索取消
    call_info = (By.ID, "com.callme.mall:id/address")  # 定位当前地址
    call_again = (By.ID, "com.callme.mall:id/location")  # 定位重新定位
    call_name = (By.ID, "com.callme.mall:id/name")  # 定位收货地址
    call_add = (By.LINK_TEXT, "text(\"新增地址\")")  # 定位新增地址
    call_nearby = (By.ID, "com.callme.mall:id/image")  # 定位附近地址

    def __init__(self, driver):
        super().__init__(driver)
        Home(driver).home_locate().click()

    def locate_address(self):  # 定位区域
        data = Login.get_data(1)
        self.wait(EC.presence_of_element_located, self.call_address).click()
        self.wait(EC.presence_of_element_located, self.call_seek).send_keys(data[1])
        self.wait(EC.presence_of_all_elements_located, self.call_seek)[2].click()
        names = self.wait(EC.presence_of_element_located, self.call_address)
        return names

    def locate_seek(self):  # 定位搜索
        self.wait(EC.presence_of_element_located, self.call_seek).click()

    def locate_sure(self):  # 定位搜索切换地址
        data = Login.get_data(2)
        self.locate_seek()
        self.wait(EC.presence_of_element_located, self.call_seek).send_keys(data[1])
        self.wait(EC.presence_of_all_elements_located, self.call_search)[0].click()

    def locate_locate(self):  # 定位地图模式
        self.wait(EC.presence_of_element_located, self.call_locate).click()

    def locate_update(self):  # 定位地图模式更新地址
        self.wait(EC.presence_of_element_located, self.call_update).click()

    def locate_list(self, num):  # 定位地图位置列表
        self.wait(EC.presence_of_all_elements_located, self.call_list)[num].click()

    def locate_history(self):  # 地图模式历史搜索删除
        self.wait(EC.presence_of_element_located, self.call_history).click()

    def locate_cancel(self):  # 定位搜索取消
        self.wait(EC.presence_of_element_located, self.call_cancel).click()

    def locate_info(self):  # 定位当前地址
        self.wait(EC.presence_of_element_located, self.call_info).click()

    def locate_again(self):  # 定位重新定位
        self.wait(EC.presence_of_element_located, self.call_again).click()

    def locate_name(self, num):  # 定位收货地址
        self.wait(EC.presence_of_all_elements_located, self.call_name)[num].click()

    def locate_add(self):  # 定位新增地址
        sleep(3)
        self.swipe(600, 1200, 500, 600, 500)
        # self.driver.find_element_by_android_uiautomator('text(\"新增地址\")').click()
        self.wait(EC.element_to_be_clickable, self.call_add).click()


if __name__ == "__main__":
    name = Locate(driver=wechat())
    name.locate_add()