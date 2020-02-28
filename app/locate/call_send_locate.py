from common.call_wechat import wechat
from app.locate.call_locate import Locate
from app.home.call_home import Home


class SendLocate(Locate):

    def __init__(self, driver):
        super().__init__(driver)
        Home(driver).home_locate().click()

    def send_locate(self):
        self.locate_address()


if __name__ == '__main__':
    driver = wechat()
    name = SendLocate(driver)
    name.send_locate()