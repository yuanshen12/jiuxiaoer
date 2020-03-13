from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common_app import Login


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
    call_login = (By.ID, "com.callme.mall:id/login")  # 登录

    def locate_address(self, station):  # 定位区域
        self.wait(EC.element_to_be_clickable, self.call_address).click()
        self.wait(EC.element_to_be_clickable, self.call_seek).send_keys(station)
        self.wait(EC.visibility_of_any_elements_located, self.call_seek)[2].click()

    def locate_seek(self):  # 定位搜索
        self.wait(EC.element_to_be_clickable, self.call_seek).click()

    def locate_sure(self, station):  # 定位搜索切换地址
        self.wait(EC.visibility_of_element_located, self.call_seek).send_keys(station)

    def locate_sure_location(self, num=0):  # 搜索确定切换地址
        locate_search = self.wait(EC.visibility_of_all_elements_located, self.call_name)[num]
        return locate_search

    def locate_locate(self):  # 定位地图模式
        locate = self.wait(EC.element_to_be_clickable, self.call_locate)
        return locate

    def locate_update(self):  # 定位地图模式更新地址
        update = self.wait(EC.element_to_be_clickable, self.call_update)
        return update

    def locate_list(self, num):  # 定位地图位置列表
        lists = self.wait(EC.visibility_of_any_elements_located, self.call_name)[num]
        return lists

    def locate_history(self):  # 地图模式历史搜索删除
        self.driver.find_element(*self.call_history).click()

    def locate_cancel(self):  # 定位搜索取消
        self.driver.find_element(*self.call_cancel).click()

    def locate_info(self):  # 定位当前地址
        info = self.wait(EC.visibility_of_element_located, self.call_info)
        return info

    def locate_again(self):  # 定位重新定位
        again = self.wait(EC.visibility_of_element_located, self.call_again)
        return again

    def locate_name(self, num):  # 定位收货地址
        location = self.wait(EC.visibility_of_any_elements_located, self.call_info)[num]
        return location

    def locate_location_sure(self):  # 定位收货地址确定
        location_sure = self.wait(EC.visibility_of_element_located, self.call_location_sure)
        return location_sure

    def locate_add(self):  # 定位新增地址
        add = self.wait(EC.visibility_of_element_located, self.call_add)
        return add

    def locate_adds(self, name, phone, tablet, tag, women=1, num=1):  # 定位新增地址(women is 1是男女，num is 1 选择地址）
        self.wait(EC.visibility_of_element_located, self.call_name).send_keys(name)
        if women != 1:
            self.wait(EC.element_to_be_clickable, self.call_women).click()
        self.wait(EC.visibility_of_element_located, self.call_phone).send_keys(phone)
        if num == 1:
            self.wait(EC.visibility_of_element_located, self.call_again).click()
            self.wait(EC.visibility_of_any_elements_located, self.call_list)[1].click()
        self.wait(EC.visibility_of_element_located, self.call_info).send_keys(tablet)
        self.wait(EC.visibility_of_element_located, self.call_tag).send_keys(tag)
        self.wait(EC.element_to_be_clickable, self.call_save).click()

    def locate_nearby(self, num):  # 定位附近地址
        nearby = self.wait(EC.visibility_of_all_elements_located, self.call_name)[num]
        return nearby

    def locate_login(self):  # 登录
        login = self.driver.find_element(*self.call_login)
        return login


if __name__ == "__main__":
    names = Locate(driver=wechat())
    names.locate_login()
