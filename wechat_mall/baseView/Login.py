from selenium import webdriver
from appium import webdriver
from wechat_mall.common import comm
from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions

def open(self):     #     打开微商城
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'LKX7N17B09002482',
        'platformVersion': '9',
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'noReset': 'True',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True',
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_android_uiautomator('text(\"叫酒开发\")').click()
    self.driver.find_element_by_android_uiautomator('text(\"测试商城\")').click()

def scation(self):    #     手动定位
    try:
        self.driver.find_element_by_android_uiautomator('text(\"手动选择站点\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()
        self.driver.find_element_by_id("newCloseBtn").click()
    except :
        self.driver.find_element_by_id('android:id/text1')

def advertisement(self):    #    去广告
    wait(self)
    try:
        webview(self)
        self.driver.find_element_by_id("newCloseBtn").click()
    except:
        self.driver.find_element_by_id("newCloseBtn").click()


def scation_open(self):   #    手动定位和去广告进入微商城
    try:
        advertisement(self)
    except:
        pass



def webview(self):   #     切换到webview
    self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  #    切换WEBWIEW
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])  # 切换窗口

def scation_guiyang(self):    #    切换到贵阳站
    webview(self)
    wait(self)
    self.driver.find_element_by_id('cityName').click()
    self.driver.find_element_by_xpath('/html/body/sub-head/div[1]').click()    #    选址
    el = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[7]/li[5]/div')
    TouchActions(self.driver).tap(el).perform()    #    tap点击选址
    self.driver.find_element_by_xpath('/html/body/sub-head/div[3]/input').send_keys(comm.station)     #    输入火车站
    sleep(2)
    self.driver.find_element_by_xpath('/html/body/search-win/div[4]/div/div[2]/div[2]/div[2]').click()   #   选定地址

def scation_page(self):    # 判断是否是贵阳站，不是选择贵阳站
    try:
        wait(self)
        title = self.driver.title
        if comm.guiyang not in title:
            scation_guiyang(self)
            advertisement(self)
        else:
            pass
    except:
        pass



def search(self):     #    搜索
    webview(self)
    self.driver.find_element_by_xpath('//*[@id="header"]/aside[2]/input').click()    #    点击搜索框
    self.driver.find_element_by_xpath('/html/body/header/div[1]/div/input').send_keys(comm.seek)     #    输入配置信息
    sleep(1)
    self.driver.press_keycode(66)
 #   self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/ul/li[1]').click()    #    确定搜索物品

def shopping(self):    #    购物
    self.driver.find_element_by_xpath('/html/body/section/article/ul/li[2]/a/div[5]/aside/div[1]').click()
    self.driver.find_element_by_xpath('//*[@id="TripBook"]/aside/div[1]/a').click()
    self.driver.find_element_by_xpath('/html/body/nav/article/aside[1]/div[1]/div').click()

def to_be(self):    #    待完善
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/input').send_keys('自动化下单')
    sleep(2)
    phone = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/input')
    phone.clear()
    phone.send_keys('13558252700')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[5]/div[2]/input').send_keys('3号楼305')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[7]/div/div/div/div[2]').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div').click()

def to(self):    #    已存在地址
    sleep(2)
    self.driver.find_element_by_xpath('//*[@id="app"]//div/div/div[2]/div').click()



def settle(self):  # 结算页面
    driver = self.driver
    wait(self)
    driver.find_element_by_xpath('//*[@id="section"]/div[1]/div/div[2]/div/div').click()  # 送达时间
    sleep(2)
    ell = driver.find_element_by_xpath('//*[@id="userPickTime"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]')
    TouchActions(self.driver).tap(ell).perform()  # tap点击选址
    sleep(2)
    driver.find_element_by_xpath('//*[@id="userPickTime"]/div/div[2]/div/div[3]/button').click()  # 确定时间
    sleep(2)
    driver.find_element_by_xpath('//*[@id="section"]/div[3]/div[2]').click()  # 打开选址
    sleep(2)
    try:
        to_be(self)
    except:
        to(self)
    wait(self)
    driver.swipe(int(1048) / 2, int(3760) / 2, int(1048) / 2, int(1920) / 4, duration=sleep(1))  # 滑动屏幕
    wait(self)
    driver.find_element_by_xpath('//*[@id="section"]/div[6]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="footer"]/a').click()

def equel(self):    # 点击确认订单
    self.driver.find_element_by_xpath('//*[@id="popups"]/div/div[1]')

def overtime(self):
    self.driver.find_element_by_xpath("/html/body/section/div[2]/div[1]").click()

def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def screenshots(self):
    self.driver.swipe(int(1048) / 2, int(3760) / 2, int(1048) / 2, int(1920) / 4, duration=sleep(1))  # 滑动屏幕
    sleep(2)
    self.driver.swipe(int(1048) / 2, int(3760) / 2, int(1048) / 2, int(1920) / 4, duration=sleep(1))  # 滑动屏幕

def screen(self):
    self.driver.find_element_by_xpath('/html/body/nav[2]/ul/li[3]/a').click()  # 点击筛选
    sleep(1)
    self.driver.find_element_by_xpath('//*[@id="-2"]/aside[2]/div[9]').click()  # 点击燕京
    self.driver.find_element_by_xpath("//*[@id='doc-mix-offcanvas']/aside[2]/div[2]/a").click()  # 点击确定

def wait(self):   #  等待
    self.driver.current_activity
    self.driver.wait_activity(".base.ui.MainActivity", 15)

def shoppings(self):
    self.driver.find_element_by_xpath('/html/body/section/article/ul/li[7]/a/div[5]/aside/div[1]').click()  # 点击加入购物车
    self.driver.find_element_by_xpath('//*[@id="TripBook"]/aside/div[1]/a').click()  # 加入购物车
    sleep(2)
    self.driver.find_element_by_xpath('/html/body/nav[1]/article/aside[1]/div[1]/span').click()  # 打开购物车

def screenshots(self):
    try:
        self.driver.find_element_by_id("kwsss").send_keys("selenium")
        self.driver.find_element_by_id("su1").click()
    except:
        self.driver.get_screenshot_as_file("../APPTest/screenshots/error_png.png")




if __name__ == '__main__':
 #  scation_open()
   swipeUp(driver=483,t=500,n=1)
