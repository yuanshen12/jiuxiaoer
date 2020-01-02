from wechat_mall.baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from wechat_mall.common.Login import Login
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')

    advertisement = (By.ID, 'newCloseBtn')
    locate = (By.ID, 'com.tencent.mm:id/b29')

    shouuye = (By.XPATH,"//*[contains(text(), '首页')]")
    fianax = (By.XPATH,"//*[contains(text(), '发现')]")
    mashanghe = (By.XPATH,"//*[contains(text(), '马上喝')]")
    dingdan = (By.XPATH,"/html/body/div[10]/div/div[2]/div[5]")
    wode = (By.XPATH,"//*[contains(text(), '我的')]")
    shanchu = (By.XPATH,"//*[contains(text(), '删除')]")
    kong = (By.XPATH,'/html/body/div[1]')


    def check_cancelBtn(self):
        logging.info('==========check_cancelBtn=========')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('=========check skipBtn=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot' %module)
        return self.driver.get_screenshot_as_file(image_file)


    def check_market_ad(self):
        logging.info('====check_market_ad====')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader,1):
                if index == line:
                    return row

    #appium 隐式等待
    def wait(self):
        try:
            self.driver.wait_activity(".base.ui.MainActivity", 15)
        except:
            self.getScreenShot()


    def webview(self):  # 切换到webview
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  # 切换WEBWIEW
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[1])  # 切换窗口

    # 弹屏去广告
    def advertisement_open(self):
        logging.info('==========advertisement=========')
        try:
            advertisement = self.driver.find_element(*self.advertisement)
        except NoSuchElementException:
            logging.info('no advertisement')
        else:
            advertisement.click()

    # 去地理位置授权
    def lacote_sure(self):
        logging.info('==========locate=========')
        try:
            locate = self.driver.find_element(*self.locate)
        except NoSuchElementException:
            logging.info('no locate')
        else:
            locate.click()

    def Swipe(self,num):
        one = 0
        while num > one:
            self.driver.swipe(int(1048) / 2, int(3000) / 2, int(1048) / 2, int(2500) / 4, duration=time.sleep(1))  # 滑动屏幕
            self.wait_time(5)
            one += 1

    #appium 隐式等待
    def wait_time(self,T):
        self.driver.wait_activity(".base.ui.MainActivity", T)

    # 底部五个标题栏切换
    def base(self,sum):
            if sum == 0:
                self.driver.find_element(*self.shouuye).click()
            elif sum == 1:
                self.driver.find_element(*self.fianax).click()
            elif sum == 2:
                self.driver.find_element(*self.mashanghe).click()
            elif sum == 3:
                self.driver.find_element(*self.dingdan).click()
            elif sum == 4:
                self.driver.find_element(*self.wode).click()

    def gouwu_shanchu(self):
        T = 0
        while T < 10:
            self.wait_time(2)
            P = self.driver.find_element(*self.kong).text
            Q = "随便逛逛"
            if Q not in P:
                self.wait_time(2)
                self.driver.swipe(int(900), int(700), int(300), int(700), duration=time.sleep(0.2))  # 滑动屏幕
                self.wait_time(2)
                try:
                    self.driver.find_element(*self.shanchu).click()
                except:
                    T
                else:
                    T += 1
            else:
                break










if __name__ == '__main__':
    Login()
