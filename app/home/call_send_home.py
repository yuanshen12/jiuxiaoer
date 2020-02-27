from app.home.call_home import Home
from common.call_wechat import wechat


class SendHome(Home):

    def send_home(self):
        self.home_locate().click()


if __name__ == "__main__":
    driver = wechat()
    name = SendHome(driver)
    name.send_home()