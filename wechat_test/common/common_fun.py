from wechat_test.baseView.baseView import BaseView
from wechat_test.common.desired_caps import appium_desired
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    csv_file='../data/account.csv'  # 参数路径

    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')

    sction = (By.XPATH, "//*[contains(text(), '手动选择站点')]")
    sction_user = (By.XPATH, "//*[contains(text(), '确认')]")
    sction_id = (By.ID, "newCloseBtn")

    shanchu = (By.XPATH, "//*[contains(text(), '删除')]")
    kong = (By.XPATH, '/html/body/div[1]')
    delivery = (By.XPATH, '/html/body/div[1]')

    delivery_text = (By.XPATH, '//*[@id="section"]/div[1]/div/div[2]/div/div')  # 送达时间text
    delivery_user = (By.XPATH, '//*[@id="userPickTime"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]')  # 选择时间
    delivery_users = (By.XPATH, '//*[@id="userPickTime"]/div/div[2]/div/div[3]/button')  # 确定时间
    receiving = (By.XPATH, '//*[@id="section"]/div[3]')  # 收货地址
    receiving_a = (By.XPATH, '//*[@id="app"]/div/div')  # 收货页面
    receiving_f = (By.XPATH, "//*[contains(text(), '使用已有收货地址')]")  # 进入已有收货地址
    receiving_name = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/input')  # 收货地址姓名
    receiving_phone = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/input')  # 收货地址电话
    receiving_c = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[5]/div[2]/input')  # 收货地址
    receiving_d = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[7]/div/div/div/div[2]')  # 选择公司
    receiving_e = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div')  # 确定地址
    receiving_g = (By.XPATH, '//*[@id="section"]/div[6]/div[2]/div/div[2]')  # 选择货到付款
    receiving_j = (By.XPATH,'//*[@id="section"]/div[7]/div[1]/div/div[2]/a/div/span')  # 优惠券
    receiving_k = (By.XPATH,'//*[@id="list"]/div/div[2]')  # 选择优惠券
    receiving_h = (By.XPATH, '//*[@id="footer"]/a')  # 提交订单

    shouuye = (By.XPATH, "//*[contains(text(), '首页')]")
    fianax = (By.XPATH, "//*[contains(text(), '发现')]")
    mashanghe = (By.XPATH, "//*[contains(text(), '马上喝')]")
    dingdan = (By.XPATH, "/html/body/div[10]/div/div[2]/div[5]")
    wode = (By.XPATH, "//*[contains(text(), '我的')]")


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
        self.driver.get_screenshot_as_file(image_file)

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
        with open(csv_file,'r', encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def Time(self,time):  # 隐式等待
        self.driver.wait_activity(".base.ui.MainActivity", time)

    def Swipe(self,num):
        one = 0
        while num > one:
            self.driver.swipe(int(1048)/2,int(3000)/2,int(1048)/2,int(2500)/4,duration=time.sleep(1))  # 滑动屏幕
            self.Time(2)
            one += 1

    def webview(self,Handles):  # 切换webview页面
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        self.Time(5)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[Handles])

    def advertisement(self):  # 去广告
        try:
            self.driver.find_element(*self.sction_id).click()
        except:
            pass

    def login_test(self):  # 登录到首页
        logging.info('=====login_test======')
        self.Time(5)
        self.webview(1)
        title = self.driver.title
        Title = ["酒小二","正在进入商城"]
        if Title[0] in title:
            pass
        elif Title[1] in title:
            self.driver.find_element(*self.sction).click()
            self.Time(3)
            self.driver.find_element(*self.sction_user).click()
        self.advertisement()

    def gouwu_shanchu(self):  # 清空购物车
        data = Common.get_csv_data(self,self.csv_file,3)
        T = 0
        while T < 10:
            self.Time(2)
            P = self.driver.find_element(*self.kong).text
            if data[1] not in P:
                self.Time(2)
                self.driver.swipe(int(900), int(700), int(300), int(700), duration=time.sleep(0.2))  # 滑动屏幕
                self.Time(2)
                try:
                    self.driver.find_element(*self.shanchu).click()
                except:
                    T
                else:
                    T += 1
            else:
                break

    def settle(self,P):  # 结算页面
        data = Common.get_csv_data(self, self.csv_file, 4)
        self.Time(5)
        num = self.driver.find_element(*self.delivery_text).text
        if data[1] == num:
            pass
        else:
            self.Time(5)
            self.driver.find_element(*self.delivery_text).click()
            self.Time(5)
            user = self.driver.find_element(*self.delivery_user)
            TouchActions(self.driver).tap(user).perform()
            self.Time(5)
            self.driver.find_element(*self.delivery_users).click()
        receiving_text = self.driver.find_element(*self.receiving).text
        if data[2] in receiving_text:
            pass
        else:
            self.driver.find_element(*self.receiving).click()
            self.Time(5)
            receiving_a_text = self.driver.find_element(*self.receiving_a).text
            if data[3] in receiving_a_text:
                self.driver.find_element(*self.receiving_name).send_keys(data[4])
                self.Time(3)
                phone = self.driver.find_element(*self.receiving_phone)
                phone.clear()
                phone.send_keys(data[2])
                self.driver.find_element(*self.receiving_c).send_keys(data[5])
                self.driver.find_element(*self.receiving_d).click()
                self.driver.find_element(*self.receiving_e).click()
        if P == 1:
            try:
                self.driver.find_element(*self.receiving_g).click()
            except:
                self.Swipe(1)
                self.driver.find_element(*self.receiving_g).click()
        elif P == 0:
            pass
        self.Time(5)
        youhuijuan = self.driver.find_element(*self.receiving_j).text
        Q = "张可用"
        if Q in youhuijuan:
            self.Swipe(1)
            self.driver.find_element(*self.receiving_j).click()
            num = self.driver.find_element(*self.receiving_k).text
            mun = "自动化红酒卷"
            if mun in num:
                self.driver.find_element(*self.receiving_k).click()
        self.driver.find_element(*self.receiving_h).click()
        self.Time(5)

    def base(self,sum):  # 首页选择菜单
            if sum == 0:
                self.driver.find_element(*self.shouuye).click()
            elif sum == 1:
                self.driver.find_element(*self.fianax).click()
            elif sum == 2:
                try:
                    self.driver.find_element(*self.mashanghe).click()
                except:
                    self.driver.find_element(*self.mashanghe).click()
            elif sum == 3:
                try:
                    self.driver.find_element(*self.dingdan).click()
                except:
                    self.driver.find_element(*self.dingdan).click()
            elif sum == 4:
                try:
                    self.driver.find_element(*self.wode).click()
                except:
                    self.driver.find_element(*self.wode).click()


if __name__ == '__main__':
     driver = appium_desired()
     num = Common(driver)
     num.login_test()






