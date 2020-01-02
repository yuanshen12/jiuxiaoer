from wechat_test.common.desired_caps import appium_desired
from wechat_test.businessView.scation import Scation
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
from wechat_test.common.TMS import TMS
import re


class Reduced(Common):
    csv_file='../data/account.csv'  # 参数路径

    reduced_a = (By.XPATH, "/html/body/section[3]/article/a[3]")  # 首页进入热销推荐
    reduced_b = (By.XPATH, "//*[@id='paddingTop']/section/div[3]/div/div[2]/span[2]")  # 选择数量触发满赠活动
    reduced_c = (By.XPATH, "//*[contains(text(), '立即购买')]")  # 选择立即购买
    reduced_d = (By.XPATH, "/html/body/section/article/ul/li[7]/a/div[5]/aside/div[1]")  # 点击加号
    reduced_e = (By.XPATH, "//*[contains(text(), '立即购买')]")  # 马上喝点立即购买
    reduced_f = (By.XPATH, "/html/body/div[2]")  # 提交订单详情
    reduced_g = (By.XPATH, "/html/body/div[3]/div[2]") # 逛逛
    reduced_h = (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]") # 订单状态
    reduced_j = (By.CLASS_NAME, "android.widget.Button")  # 点击确定
    reduced_k = (By.XPATH, "//*[contains(text(), '我的积分')]")  # 选择我的积分
    reduced_l = (By.CLASS_NAME, "change-number")  # 积分
    reduced_z = (By.CLASS_NAME, "level-two")  # 时间
    reduced_v = (By.XPATH, "//*[contains(text(), '等级')]")  # 选择我的成长值
    reduced_n = (By.CLASS_NAME, "add-number")  # 成长值
    reduced_m = (By.XPATH, "//*[contains(text(), '张')]")  # 选择我的优惠券
    reduced_i = (By.ID, "list")  # 优惠券
    reduced_o = (By.CLASS_NAME, "btn")  # 查看订单详情
    reduced_p = (By.CLASS_NAME, "list")  # 商品详情赠品
    reduced_s = (By.XPATH,"/html/body/div[2]/div[2]/p[2]/span")  # 商品详情金额


    def reduced(self,mun=()):
        try:
            num = Scation(self.driver)
            num.login_guiyang()
        except:
            num = Scation(self.driver)
            num.login_guiyang()
        self.Swipe(1)
        self.driver.find_element(*self.reduced_a).click()
        self.Time(3)
        self.driver.find_element(*self.reduced_b).click()
        self.driver.find_element(*self.reduced_c).click()
        self.settle(1)
        if mun != 1:
            P = TMS(self)
            P.Tms(4)

    def reduced_A(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(4)
        self.driver.find_element(*self.reduced_k).click()
        text_jifen = self.driver.find_elements(*self.reduced_l)[0].text
        text_jifen1 = self.driver.find_elements(*self.reduced_l)[1].text
        one = int(text_jifen)
        two = int(text_jifen1)
        if one == 21 or two == 21:
            return True
        else:
            return False

    def reduced_B(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(4)
        self.driver.find_element(*self.reduced_v).click()
        text_chengzhangzhi = self.driver.find_element(*self.reduced_n).text
        text_text_chengzhangzhi1 = self.driver.find_elements(*self.reduced_n)[1].text
        one = int(text_chengzhangzhi)
        two = int(text_text_chengzhangzhi1)
        if one == 21 or two == 21:
            return True
        else:
            return False

    def reduced_C(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.base(4)
        self.driver.find_element(*self.reduced_m).click()
        text_youhuijuan = self.driver.find_element(*self.reduced_i).text
        one = "自动化红酒卷"
        if one in text_youhuijuan:
            return True
        else:
            return False

    def reduced_D(self):
        self.Time(5)
        self.driver.find_element(*self.reduced_o).click()
        list = self.driver.find_element(*self.reduced_p).text
        zengping = "赠品"
        if zengping in list:
            return True
        else:
            return False

    def reduced_E(self):
        self.Time(5)
        jine = self.driver.find_element(*self.reduced_s).text
        num = re.findall(r"\d",jine)
        mun = ""
        for i in num:
            mun += i
        return int(mun[:-2])

    def reduced_F(self):
        self.driver.find_element(*self.reduced_o).click()
        list = self.driver.find_element(*self.reduced_p).text
        zengping = "赠品"
        if zengping not in list:
            return True
        else:
            return False

    def reduced_G(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.Swipe(1)
        self.driver.find_element(*self.reduced_a).click()
        self.Time(3)
        self.driver.find_element(*self.reduced_b).click()
        try:
            self.driver.find_element(*self.reduced_c).click()
            return False
        except:
            return True

    def reduced_H(self):
        num = Scation(self.driver)
        num.login_guiyang()
        self.Swipe(1)
        self.driver.find_element(*self.reduced_a).click()
        self.Time(3)
        self.driver.find_element(*self.reduced_b).click()
        try:
            self.driver.find_element(*self.reduced_c).click()
            return True
        except:
            return False

if __name__ == '__main__':
        driver = appium_desired()
        num = Reduced(driver)
        # num.reduced(1)
        num.reduced_A()