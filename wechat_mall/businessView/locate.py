import logging
from time import sleep
from selenium.webdriver.common.by import By
from wechat_mall.common.Login import Login
from wechat_mall.common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions

class locate(Common):
    locate_go = (By.CLASS_NAME,'location-btn')  # 地址
    locate_p = (By.CLASS_NAME, "address-name")
    likexiadan = (By.XPATH,"//*[contains(text(), '手动切换站点')]")
    queding = (By.XPATH,"//*[contains(text(), '确认')]")
    location_1 = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[7]/li[5]/div")
    determine = (By.ID,'com.tencent.mm:id/b29')  # 地址弹窗
    current = (By.XPATH,'/html/body/sub-head/div[1]')  # 标题
    current_sure = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[1]')  #当前
    receipt = (By.XPATH,'/html/body/div[2]/div[2]/div[3]')  # 收货
    new = (By.XPATH,'/html/body/div[2]/div[3]') # 新增
    near = (By.XPATH,'/html/body/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]')  # 附近

    # 首页定位标签
    def locate_text(self):
        self.wait_time(5)
        try:
            self.driver.find_element(*self.locate_go).text
        except:
            self.driver.find_element(*self.likexiadan).click()
            self.wait_time(3)
            self.driver.find_element(*self.queding).click()
        self.wait_time(3)
        locate_text = self.driver.find_element(*self.locate_go).text
        return locate_text

    # 定位首页标签
    def location_text(self):
        self.wait()
        location_text = self.driver.find_element(*self.locate_p).text
        return location_text

    # 进入定位页面并解除定位弹屏
    def location_determine(self):
        logging.info('============location_determine==============')
        self.wait_time(5)
        locate_go = self.driver.find_element(*self.locate_go)
        TouchActions(self.driver).tap(locate_go).perform()
        try:
            self.driver.switch_to.context('NATIVE_APP')
            determine = self.driver.find_element(*self.determine)
        except NoSuchElementException:
            logging.info('no determine')
        else:
            determine.click()
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

    # 当前定位标签
    def current_text(self):
        current_text = self.driver.find_element(*self.current_sure).text
        return current_text

    # 进入当前定位
    def location_current(self):
        logging.info('============location_current==============')
        current_sure = self.driver.find_element(*self.current_sure)
        TouchActions(self.driver).tap(current_sure).perform()

    # 收货定位标签
    def receipt_text(self):
        self.wait()
        receipt_text = self.driver.find_element(*self.receipt).text
        return receipt_text

    # 收货
    def location_receipt(self):
        logging.info('============location_receipt==============')
        self.driver.find_element(*self.receipt).click()

    def near_text(self):
        near_text = self.driver.find_element(*self.near).text
        return near_text

    # 附近
    def lacation_near(self):
        logging.info('============lacation_near==============')
        self.driver.find_element(*self.near).click()

# 新增收货地址
class receipt_new(Common):
    # 地址新增
    new = (By.XPATH, '/html/body/div[2]/div[3]')  # 新增
    name = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/input')
    Phone = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/input')
    Locate = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[5]/div[2]/input')
    company = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[7]/div/div/div/div[2]')
    suer = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div')
    receipt_1 = (By.XPATH, '/html/body/div[2]/div[2]/div[3]')  # 收货
    text = (By.XPATH,'/html/body/div[2]/div[2]/div[3]')
    # 地址删除
    me = (By.XPATH, '/html/body/div[10]/div/div[2]/div[6]/div[1]')
    location = (By.XPATH, "//*[contains(text(), '地址管理')]")
    delete = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[5]/i[2]')
    suer_1 = (By.XPATH, "//*[contains(text(), '确定')]")
    home = (By.CLASS_NAME, 'nav-item')

    # 新增收货地址
    def receipt_new(self):
            logging.info('============receipt_new==============')
            self.driver.find_element(*self.name).send_keys('技术测试')
            phone = self.driver.find_element(*self.Phone)
            phone.clear()
            phone.send_keys('13558252700')
            self.driver.find_element(*self.Locate).send_keys('3F')
            self.driver.find_element(*self.company).click()
            self.driver.find_element(*self.suer).click()

    def receipt(self):
        logging.info('============receipt==============')
        self.driver.find_element(*self.new).click()
        try:
            self.receipt_new()
        except:
            return False
        else:
            self.wait_time(15)
            self.driver.find_element(*self.receipt_1).click()
            return True

    # 删除收货地址
    def delete_open(self):
        logging.info('============delete==============')
        try:
            self.driver.find_element(*self.me).click()
            try:
                self.driver.find_element(*self.location).click()
            except:
                self.Swipe(1)
                self.driver.find_element(*self.location).click()
            self.wait_time(2)
            self.driver.find_element(*self.delete).click()
            self.driver.find_element(*self.suer_1).click()
            self.driver.keyevent(4)
            self.driver.find_element(*self.home).click()
        except:
            return False
        else:
            return True

# 切换区域
class cut(Common):
    locate = (By.CLASS_NAME, "address-name")
    location = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[7]/li[5]/div")
    suer = (By.XPATH,'/html/body/div[2]/div[2]/div[3]')
    shut = (By.CLASS_NAME,'modal-close')
    ctiy = (By.XPATH, "/html/body/div[3]/div[1]/div/input")
    nanning = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[14]/li[2]/div")
    seek = (By.XPATH, "/html/body/sub-head/div[3]/input")
    suer_one = (By.XPATH, "/html/body/search-win/div[4]/div/div[2]/div[2]/div[2]")
    locate_go = (By.ID, 'cityName')  # 地址

    map = (By.XPATH,'/html/body/sub-head/div[5]')
    map_locate = (By.XPATH,'//*[@id="map"]/button/span')
    map_suer = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/ul/li[1]/div[1]')

    def cut_open(self):
        logging.info('============cut_open==============')
        self.driver.find_element(*self.locate).click()
        location = self.driver.find_element(*self.location)
        TouchActions(self.driver).tap(location).perform()
        try:
            suer = self.driver.find_element(*self.suer)
            TouchActions(self.driver).tap(suer).perform()
            self.driver.find_element(*self.shut).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.cut_out()
            return True

    # 回退区域
    def cut_out(self):
        logging.info('============cut_out==============')
        locate = self.driver.find_element(*self.locate)
        TouchActions(self.driver).tap(locate).perform()
        self.driver.find_element(*self.ctiy).send_keys('南宁')
        nanning = self.driver.find_element(*self.nanning)
        TouchActions(self.driver).tap(nanning).perform()

    # 输入搜索并回退
    def cut_seek(self):
        self.driver.find_element(*self.seek).click()
        self.driver.find_element(*self.seek).send_keys("火车站")
        self.wait()
        self.driver.find_element(*self.suer_one).click()

    def cut_seeks(self):
        logging.info('============cut_seeks==============')
        try:
            self.cut_seek()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.driver.find_element(*self.locate_go).click()
            return True

    def cut_map(self):
        logging.info('============cut_map==============')
        try:
            self.driver.find_element(*self.map).click()
            self.driver.find_element(*self.map_locate).click()
            self.driver.find_element(*self.map_suer).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.wait()
            self.driver.find_element(*self.locate_go).click()
            return True


if __name__ == '__main__':
    L = receipt_new(open())
    L.receipt()

