from appium import webdriver
import yaml
import logging
import logging.config
import os
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
from  wechat_test.businessView.operation_web import Operation


CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class TMS(Common):
    # TMS
    search_h = (By.ID, "android:id/button2")  # TMS暂不设置
    search_j = (By.ID, "com.callme.business.test.online:id/rb_shop")  # TMS选择门店
    search_g = (By.ID, "com.callme.business.test.online:id/rb_deliver")  # TMS选择配送员
    search_k = (By.ID, "com.callme.business.test.online:id/et_account")  # TMS输入登录的手机号
    search_z = (By.ID, "com.callme.business.test.online:id/et_password")  # TMS输入登录密码
    search_l = (By.ID, "com.callme.business.test.online:id/btn_login")  # TMS点击登录
    search_a = (By.ID, "com.callme.business.test.online:id/more")  # TMS打开设置
    search_b = (By.ID, "com.callme.business.test.online:id/tv_exit")  # TMS退出登录
    search_c = (By.ID, "com.callme.business.test.online:id/btn_positive")  # TMS确定
    search_cc = (By.ID,'android:id/button2')  # 暂不设置
    search_d = (By.ID, "com.callme.business.test.online:id/ll_service")  # TMS进入门店订单
    search_dd = (By.ID, "com.callme.business.test.online:id/tv_name")  # TMS进入门店订单
    search_e = (By.ID, "com.callme.business.test.online:id/btn_take_order")  # TMS接单
    search_f = (By.ID, "com.callme.business.test.online:id/btn_positive")  # TMS确定
    search_q = (By.ID, "com.callme.business.test.online:id/tv_red_dot")  # TMS配送员点进配送单
    search_qq = (By.ID, "com.callme.business.test.online:id/iv_service")  # TMS配送员点进配送单
    search_w = (By.ID, "com.callme.business.test.online:id/btn_scan_code")  # TMS配送员扫码出库
    search_r = (By.ID, "com.callme.business.test.online:id/btn_stock_right")  # TMS配送员确认出库
    search_t = (By.ID, "com.callme.business.test.online:id/btn_positive")  # TMS配送员确定
    search_y = (By.ID, "com.callme.business.test.online:id/btn_out_complete")  # TMS配送员开始配送
    search_u = (By.ID, "com.callme.business.test.online:id/tab_delivering")  # TMS配送员我的配送
    search_i = (By.ID, "com.callme.business.test.online:id/btn_confirm")  # TMS配送员确定送达
    search_o = (By.ID, "com.callme.business.test.online:id/btn_positive")  # 确定
    search_p = (By.ID, "com.callme.business.test.online:id/tab_cash")  # TMS配送员现金支付
    search_x = (By.ID, "com.callme.business.test.online:id/btn_scan_code")  # TMS配送员客户支付现金
    search_v = (By.ID, "com.callme.business.test.online:id/btn_positive")  # TMS配送员已送达


    def Tms(self,num):
            with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
                data=yaml.safe_load(file)

            desired_caps={}
            desired_caps['platformName']=data['platformName']
            desired_caps['platformVersion']=data['platformVersion']
            desired_caps['deviceName']=data['deviceName']

            base_dir = os.path.dirname(os.path.dirname(__file__))
            app_path = os.path.join(base_dir, 'app', data['appname_tms'])
            desired_caps['app']=app_path

            desired_caps['appPackage']=data['appPackage_tms']
            desired_caps['appActivity']=data['appActivity_tms']
            desired_caps['noReset']=data['noReset']

            desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
            desired_caps['resetKeyboard']=data['resetKeyboard']

            logging.info('start app...')
            self.driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
            self.driver.implicitly_wait(8)
            try:
                self.Time(5)
                self.driver.find_element(*self.search_cc).click()
            except:
                pass
            if num == 1:
                self.Tms_c()
            elif num == 2:
                self.Tms_y()
            elif num == 3:
                self.Tms_f(1)
            elif num == 4:
                self.Tms_c()
                self.Tms_y()
                self.Tms_f(0)
            # return self.driver.close_app()


    def Tms_a(self,pthon):
            self.driver.find_element(*self.search_j).click()
            TMS = self.driver.find_element(*self.search_k)
            TMS.clear()
            TMS.send_keys(pthon)
            TMSpass = self.driver.find_element(*self.search_z)
            TMSpass.clear()
            TMSpass.send_keys(123456)
            self.driver.find_element(*self.search_l).click()
            try:
                self.driver.find_element(*self.search_cc).click()
            except:
                pass

    # 从web端获取手机号码
    def Tms_b(self):
        num = Operation(self.driver)
        P = num.operation()
        self.Tms_a(P)

    def Tms_c(self):
        try:
            self.Tms_b()
        except:
            self.driver.find_element(*self.search_a).click()
            self.driver.find_element(*self.search_b).click()
            self.driver.find_element(*self.search_c).click()
            self.Tms_b()
        self.Time(3)
        self.driver.find_elements(*self.search_d)[0].click()
        self.driver.find_element(*self.search_e).click()
        self.driver.find_element(*self.search_f).click()
        self.driver.keyevent(4)

    def Tms_d(self):
        try:
            self.driver.find_element(*self.search_a).click()
            self.driver.find_element(*self.search_b).click()
            self.driver.find_element(*self.search_c).click()
            self.Tms_e()
        except:
            self.Tms_e()

    def Tms_e(self):
        self.driver.find_element(*self.search_g).click()
        TMS = self.driver.find_element(*self.search_k)
        TMS.clear()
        TMS.send_keys(13558252700)
        TMSpass = self.driver.find_element(*self.search_z)
        TMSpass.clear()
        TMSpass.send_keys(123456)
        self.driver.find_element(*self.search_l).click()
        try:
            self.driver.find_element(*self.search_cc).click()
        except:
            pass

    def Tms_y(self):
        self.Time(5)
        self.Tms_d()
        self.Time(5)
        try:
            self.driver.find_element(*self.search_q).click()
        except:
            self.driver.find_element(*self.search_qq).click()
        self.Time(5)
        try:
            self.Swipe(10)
        except:
            pass
        self.driver.find_element(*self.search_w).click()
        self.driver.find_element(*self.search_r).click()
        self.driver.find_element(*self.search_t).click()
        self.driver.find_element(*self.search_y).click()

    def Tms_f(self,num):
        if num == 1:
            self.Tms_d()
        if num == 1:
            self.driver.find_element(*self.search_q).click()
        self.driver.find_element(*self.search_u).click()
        try:
            self.Swipe(5)
        except:
            pass
        self.driver.find_element(*self.search_i).click()
        try:
            self.driver.find_element(*self.search_o).click()
        except:
            pass
        self.driver.find_element(*self.search_p).click()
        self.driver.find_element(*self.search_x).click()
        self.driver.find_element(*self.search_v).click()

if __name__ == '__main__':
    TMS(Common).Tms(2)