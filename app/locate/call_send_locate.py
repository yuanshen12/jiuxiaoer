from common.call_wechat import wechat
from app.locate.call_locate import Locate
from app.home.call_home import Home
from time import sleep


class SendLocate(Locate):

    def __init__(self, driver):
        super().__init__(driver)
        sleep(2)
        home = Home(self.driver)
        home.home_locate().click()

    def send_locate_info(self):  # 定位页面确定当前位置
        try:
            self.locate_again()
            self.locate_info()
        except:
            return False
        else:
            return True

    def send_locate_sure(self):  # 区域切换并搜索定位
        self.locate_address()
        self.locate_sure()
        locate = Home(self.driver)
        return locate.home_locate()

    def send_locate_map(self):  # 定位地图模式
        try:
            self.locate_locate()
            self.locate_update()
            self.locate_list(1)
        except:
            return False
        else:
            return True

    def send_locate_name(self):  # 定位收货地址
        try:
            num = 0
            while num < 3:
                try:
                    self.locate_name(num)
                except:
                    self.locate_location_sure()
                num += 1
        except:
            return False
        else:
            return True

    def send_locate_nearby(self):  # 定位附近地址
        self.locate_nearby(1)
        home = Home(self.driver)
        names = home.home_locate()
        return names

    def send_locate_add(self):  # 定位新增地址
        self.locate_add()
        self.locate_adds(self)


if __name__ == '__main__':
    driver = wechat()
    name = SendLocate(driver)
    name.send_locate_add()