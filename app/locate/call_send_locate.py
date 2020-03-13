from selenium.common.exceptions import NoSuchElementException
from common.call_wechat import wechat
from app.locate.call_locate import Locate
from app.home.call_home import Home
from common.call_common_app import config_yaml
from time import sleep


class SendLocate(Locate):

    def __init__(self, driver):
        super().__init__(driver)
        home = Home(self.driver)
        home.home_locate().click()

    def send_locate_info_location(self):  # 当前地址
        self.locate_again().click()
        info = self.locate_info()
        return info

    def send_locate_add_location(self, women):  # 新增地址
        data = config_yaml()
        try:
            self.locate_add().click()
            self.locate_adds(data['name'], data['phone'], data['tablet'], data['tag'], women)
            return True
        except NoSuchElementException:
            return False

    def send_locate_map_location(self, names=0):  # 定位地图模式
        if names == 0:
            self.locate_locate().click()
            self.locate_update().click()
            maps = self.locate_list(1)
            return maps
        else:
            maps = self.locate_list(1)
            return maps

    def send_locate_nearby(self, num):  # 定位附近地址
        sleep(2)
        nearby_name = self.locate_nearby(num)
        return nearby_name

    def send_locate_name(self, num):  # 定位收货地址
        locate_name = self.locate_name(num)
        return locate_name

    def send_locate_search(self, search=0):  # 区域切换并搜索定位
        data = config_yaml()
        if search == 0:
            self.locate_address(data['station'])
            self.locate_seek()
            self.locate_sure(data['stations'])
            locate_search = self.locate_sure_location()
            return locate_search
        else:
            locate_search = self.locate_sure_location()
            return locate_search

    def send_locate_login(self):  # 登录
        try:
            sleep(2)
            login = self.locate_login()
            if login.text == '登录':
                login.click()
                self.login()
        except NoSuchElementException:
            pass


if __name__ == '__main__':
    driver = wechat()
    name = SendLocate(driver)
    name.send_locate_add_location(women=1, num=0)