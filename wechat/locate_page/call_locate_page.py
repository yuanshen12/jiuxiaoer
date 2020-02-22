from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.call_wechat import wechat
from common.call_common import Login
from wechat.home.call_home import Home
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
    call_locate = (By.CLASS_NAME, 'addr')  # 定位页面附近地址（1,2,……）

    call_name = (By.CLASS_NAME, "name")  # 区域页面选择区域
    call_back = (By.CLASS_NAME, "back")  # 区域页面点击返回
    call_search = (By.XPATH, "/html/body/div[3]/div[1]/div/input")  # 区域页面输入搜索
    call_names = (By.CLASS_NAME, "scroll-container")  # 区域页面搜索结果

    call_cancel = (By.CLASS_NAME, "cancel-btn")  # 搜索页面点击取消
    call_history = (By.CLASS_NAME, "list")  # 搜索页面获取历史搜索
    call_map_one = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]")  # 搜索页面地图模式（右上角）
    call_map_two = (By.XPATH, "/html/body/search-win/div[2]/span[2]")  # 搜索页面地图模式（中间）

    call_map_city = (By.CLASS_NAME, "city")  # 地图模式点开区域
    call_map_item = (By.CLASS_NAME, "item")  # 地图模式选择区域
    call_map_seek = (By.XPATH, "//*[@id='app']/div/div/div[1]/div[1]/div[3]/input")  # 地图模式搜索
    call_map_locate = (By.XPATH, "/html/body/div/div/div/div/div[2]/button")  # 地图模式定位按钮
    call_map_first = (By.CLASS_NAME, "first")  # 地图模式选择当前定位位置

    call_take = (By.CLASS_NAME, "modal-msg")  # 定位页面收货地址超范围

    call_add_locate = (By.XPATH, "//*[@id='app']/div/div/div[1]/div/div[1]/div[2]/input")  # 定位页面新增地址姓名
    call_add_circle = (By.CLASS_NAME, "circle")  # 定位页面新增地址性别
    call_add_phone = (By.XPATH, "//*[@id='app']/div/div/div[1]/div/div[3]/div[2]/input")  # 定位页面新增地址电话
    call_add_arrow = (By.CLASS_NAME, "icon-next_arrow")  # 定位页面新增地址地址
    call_add_tablet = (By.XPATH, "//*[@id='app']/div/div/div[1]/div/div[5]/div[2]/input")  # 定位页面新增地址门牌
    call_add_item = (By.CLASS_NAME, "item")  # 定位页面新增地址标签
    call_add_save = (By.CLASS_NAME, "sumbit-btn")  # 定位页面新增地址保存

    def __init__(self, driver):
        super().__init__(driver)
        self.login()
        Home(driver).home_location()

    # 定位页面操作
    def locate_address(self):  # 定位页面选择区域(0,1,2,3……）
        self.wait(EC.element_to_be_clickable, self.call_address).click()

    def locate_seek(self):  # 定位页面点进搜索
        self.wait(EC.element_to_be_clickable, self.call_seek).click()

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

    #  定位页面点开新增地址（name姓名，phone手机号，tablet门牌默认为空，item默认0为家，sex默认0为男）
    def locate_add(self, name=(), phone=(), tablet=(), item=0, sex=0):
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_element_located, self.call_add).click()
            except:
                pass
            else:
                break
        self.wait(EC.presence_of_element_located, self.call_add_locate).send_keys(name)
        if sex == 1:
            self.wait(EC.presence_of_element_located, self.call_add_circle).click()
        phones = self.wait(EC.presence_of_element_located, self.call_add_phone)
        phones.clear()
        phones.send_keys(phone)
        self.wait(EC.element_to_be_clickable, self.call_add_arrow).click()
        self.locate_map_first()
        self.wait(EC.presence_of_element_located, self.call_add_tablet).send_keys(tablet)
        self.wait(EC.presence_of_all_elements_located, self.call_add_item)[item].click()
        self.wait(EC.element_to_be_clickable, self.call_add_save).click()

    def locate_locate(self, num):  # 定位页面选择附近地址（1,2,3……）
        while True:
            try:
                self.swipe(600, 1000, 600, 600, 500)
                self.wait(EC.presence_of_all_elements_located, self.call_locate)[num].click()
            except:
                pass
            else:
                break

    #  区域页面操作
    def locate_option(self, num):  # 区域页面选择区域名(1,2……）
        self.locate_address()
        while True:
            try:
                name = self.wait(EC.presence_of_all_elements_located, self.call_name)[num]
                TouchActions(self.driver).tap(name).perform()
                self.swipe(600, 1000, 600, 600, 500)
            except:
                pass
            else:
                break

    def locate_back(self):  # 区域页面点击返回
        self.locate_address()
        self.wait(EC.element_to_be_clickable, self.call_back).click()

    def locate_search(self, num):  # 区域页面返回搜索结果
        self.locate_address()
        self.wait(EC.presence_of_element_located, self.call_search).send_keys(num)
        name = self.wait(EC.presence_of_element_located, self.call_names).text
        return name

    #  搜索页面操作
    def locate_seeks(self, num):  # 搜索页面输入地址
        self.locate_seek()
        self.wait(EC.presence_of_element_located, self.call_input).send_keys(num)

    def locate_cancel(self):  # 搜索页面点击取消
        self.locate_seek()
        self.wait(EC.presence_of_element_located, self.call_cancel).click()

    def locate_history(self):  # 搜索页面获取历史搜索
        self.locate_seek()
        name = self.wait(EC.presence_of_element_located, self.call_history).text
        return name

    def locate_seek_map(self, num):  # 搜索页面地图模式（0表示右上角，1表示中间）
        self.locate_seek()
        if num == 0:
            self.wait(EC.presence_of_element_located, self.call_map_one).click()
        elif num == 1:
            self.wait(EC.presence_of_element_located, self.call_map_two).click()

    #  地图模式操作
    def locate_map_option(self, num):  # 地图模式选择区域
        self.locate_map()
        self.wait(EC.element_to_be_clickable, self.call_map_city).click()
        self.wait(EC.presence_of_all_elements_located, self.call_map_item)[num].click()

    def locate_map_seek(self, num):  # 地图模式搜索（输入地址）
        self.locate_map()
        self.wait(EC.presence_of_element_located, self.call_map_seek).send_keys(num)

    def locate_map_locate(self):  # 地图模式定位按钮
        self.wait(EC.element_to_be_clickable, self.call_map_locate).click()

    def locate_map_first(self):  # 地图模式选择当前定位位置
        name = self.wait(EC.element_to_be_clickable, self.call_map_first)
        if name.text == "定位中...":
            sleep(2)
            name.click()
        else:
            name.click()

    #  收货地址操作
    def locate_take_location(self, num):  # 定位页面收货地址超范围返回值
        self.locate_location(num)
        try:
            name = self.wait(EC.presence_of_element_located, self.call_take).text
            return name
        except:
            return False


if __name__ == '__main__':
    driver = wechat()
    PI = Locate(driver)
    PI.locate_add(name='张三', phone=13558252700, tablet='305')
