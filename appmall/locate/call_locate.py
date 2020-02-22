from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_wechat import wechat
from common.call_common import Login
from appmall.home.call_home import Home


# 首页进入的定位页面
class Locate(Login):
    call_address = (By.ID, "com.callme.mall:id/station")  # 定位切换区域
    call_seek = (By.ID, "com.callme.mall:id/content")  # 定位搜索区域
    call_search = (By.ID, "com.callme.mall:id/addreLayout")  # 确定贵阳站
    call_home = (By.ID, "com.callme.mall:id/ll_tap")  # 首页菜单

    def __init__(self, driver):
        super().__init__(driver)
        Home(driver).home_locate()

    def locate_address(self):  # 定位区域
        data = Login.get_data(1)
        self.wait(EC.presence_of_element_located, self.call_address).click()
        self.wait(EC.presence_of_element_located, self.call_seek).send_keys(data[1])
        names = self.driver.find_element_by_id(self.call_search[1]).text
        # names = self.wait(EC.presence_of_element_located, self.call_search).text
        print(names)


if __name__ == "__main__":
    name = Locate(driver=wechat())
    name.locate_address()