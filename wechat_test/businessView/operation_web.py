from selenium import webdriver
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
import re

class Operation(Common):
    csv_file='../data/account.csv'  # 参数路径

    operation_a = (By.ID,"userName")  # 选择用户名
    operation_b = (By.ID,'password')  # 输入密码
    operation_c = (By.ID,'randCode')  # 输验证码
    operation_d = (By.ID,'but_login')  # 登录
    operation_e = (By.XPATH,'//*[@id="page-wrapper"]/div[1]/nav/ul/li[1]/a')  # 点击门店用户信息
    operation_f = (By.XPATH,'//*[@id="page-wrapper"]/div[1]/nav/ul/li[1]/ul/li[2]/a')  # 选择门店个人信息
    operation_g = (By.XPATH,'/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')  # 切换iframe
    operation_h = (By.XPATH,'//*[@id="formobj"]/fieldset/div[3]')  # 获取手机号码
    operation_j = (By.LINK_TEXT,'系统管理')  # 系统管理
    operation_k = (By.LINK_TEXT,'系统日志')  # 系统日志
    operation_z = (By.XPATH,'//*[@id="wrapper"]/nav/div[2]/div[2]')  # 系统日志

    service_ = (By.XPATH,'/html/body/div/div[1]/div[2]/table/tbody/tr[1]/td[11]/div')  # 领取任务

    def operation(self):
        data = Common.get_csv_data(self, self.csv_file, 8)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data[1])
        self.driver.implicitly_wait(30)
        try:
            self.operations()
        except:
            data = Common.get_csv_data(self, self.csv_file, 8)
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(data[1])
            self.driver.implicitly_wait(30)
            self.operations()
        self.driver.find_element(*self.operation_e).click()
        self.driver.find_element(*self.operation_f).click()
        iframe = self.driver.find_element(*self.operation_g)
        self.driver.switch_to.frame(iframe)
        T = self.driver.find_element(*self.operation_h).text
        lists = re.findall(r"\d", T)
        num = ""
        for i in lists:
            num += i
        self.driver.quit()
        return num


    def operations(self):
        data = Common.get_csv_data(self, self.csv_file, 8)
        self.driver.find_element(*self.operation_a).send_keys(data[2])
        self.driver.find_element(*self.operation_b).send_keys(data[3])
        self.driver.find_element(*self.operation_c).send_keys(data[4])
        self.driver.find_element(*self.operation_d).click()

if __name__ == '__main__':
    T = Operation(Common)
    T.operation()