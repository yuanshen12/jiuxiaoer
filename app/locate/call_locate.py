from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from app.home.call_home import Home
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
    call_info = (By.ID, "com.callme.mall:id/address")  # 定位当前地址(门牌号)
    call_again = (By.ID, "com.callme.mall:id/location")  # 定位重新定位
    call_location = (By.ID, "com.callme.mall:id/name")  # 定位收货地址
    call_location_sure = (By.ID, "com.callme.mall:id/btn")  # 定位收货地址确定
    call_add = (By.XPATH, "//*[@text= '新增地址']")  # 定位新增地址
    call_nearby = (By.ID, "com.callme.mall:id/image")  # 定位附近地址
    call_name = (By.ID, "com.callme.mall:id/name")  # 定位新增姓名
    call_women = (By.ID, "com.callme.mall:id/sex_women")  # 定位新增性别女
    call_phone = (By.ID, "com.callme.mall:id/phone")  # 定位新增电话
    call_add_location = (By.ID, "com.callme.mall:id/location")  # 定位新增位置
    call_tag = (By.ID, "com.callme.mall:id/tag")  # 定位新增标签
    call_save = (By.ID, "com.callme.mall:id/save")  # 定位新增保存

    def locate_address(self):  # 定位区域
        data = Login.get_data(1)
        self.driver.find_element(*self.call_address).click()
        self.driver.find_element(*self.call_seek).send_keys(data[1])
        self.driver.find_elements(*self.call_seek)[2].click()

    def locate_seek(self):  # 定位搜索
        self.driver.find_element(*self.call_seek).click()

    def locate_sure(self):  # 定位搜索切换地址
        data = Login.get_data(2)
        self.locate_seek()
        self.driver.find_element(*self.call_seek).send_keys(data[1])
        self.driver.find_elements(*self.call_search)[0].click()

    def locate_locate(self):  # 定位地图模式
        self.driver.find_element(*self.call_locate).click()

    def locate_update(self):  # 定位地图模式更新地址
        self.driver.find_element(*self.call_update).click()

    def locate_list(self, num):  # 定位地图位置列表
        self.driver.find_elements(*self.call_list)[num].click()

    def locate_history(self):  # 地图模式历史搜索删除
        self.driver.find_element(*self.call_history).click()

    def locate_cancel(self):  # 定位搜索取消
        self.driver.find_element(*self.call_cancel).click()

    def locate_info(self):  # 定位当前地址
        self.driver.find_element(*self.call_info).click()

    def locate_again(self):  # 定位重新定位
        self.driver.find_element(*self.call_again).click()

    def locate_name(self, num):  # 定位收货地址
        self.driver.find_elements(*self.call_location)[num].click()

    def locate_location_sure(self):  # 定位收货地址确定
        self.driver.find_element(*self.call_location_sure).click()

    def locate_add(self):  # 定位新增地址
        num = 0
        while num < 5:
            try:
                self.driver.find_element(*self.call_add).click()
            except:
                self.swipe(600, 1200, 600, 600, 500)
            else:
                break

    def locate_adds(self, women=1):  # 定位新增地址列表
        data = Login.get_data(3)
        self.driver.find_element(*self.call_name).send_keys(data[1])
        if women == 0:
            self.driver.find_element(*self.call_women).click()
        self.driver.find_element(*self.call_phone).send_keys(data[2])
        self.driver.find_element(*self.call_again).click()
        self.driver.find_elements(*self.call_list)[0].click()
        self.driver.find_element(*self.call_info).send_keys(data[3])
        self.driver.find_element(*self.call_tag).send_keys(data[4])
        self.driver.find_element(*self.call_save).click()

    def locate_nearby(self, num):  # 定位附近地址
        while True:
            try:
                self.driver.find_elements(*self.call_nearby)[num].click()
            except:
                self.swipe(600, 1200, 600, 800, 500)
            else:
                break


if __name__ == "__main__":
    names = Locate(driver=wechat())
    names.locate_adds()
