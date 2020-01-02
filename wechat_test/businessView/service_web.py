from selenium import webdriver
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
from time import sleep

class Service(Common):
    csv_file='../data/account.csv'  # 参数路径

    service_a = (By.XPATH,"/html/body/form/div[1]/div/div[2]")  # 选择用户名
    service_b = (By.XPATH,'//*[@id="userName"]')  # 输入用户名
    service_c = (By.XPATH,'//*[@id="password"]')  # 输入密码
    service_d = (By.XPATH,'/html/body/form/div[6]')  # 登录
    service_e = (By.XPATH,'//*[@id="top_tabs_box"]/div/div/iframe')  # 切换iframe
    service_f = (By.XPATH,'//*[@id="search_form"]/div[3]/div[1]/div/input')  # 输入手机号
    service_g = (By.XPATH,'//*[@id="search_form"]/div[5]/button[2]')  # 查询
    service_h = (By.XPATH,'/html/body/div/div[1]/div[2]/table/tbody/tr[1]')  # 获取列表进行定位
    service_j = (By.XPATH,'/html/body/div')  # 列表数量
    service_k = (By.XPATH,'//*[@id="search_form"]/div[1]/div[1]/div/div[2]/i')  # 待处理


    service_ = (By.XPATH,'/html/body/div/div[1]/div[2]/table/tbody/tr[1]/td[11]/div')  # 领取任务


    def service(self):
        data = Common.get_csv_data(self,self.csv_file,5)
        print(data)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data[1])
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.service_a).click()
        sleep(2)
        self.driver.find_element(*self.service_b).send_keys(data[2])
        self.driver.find_element(*self.service_c).send_keys(data[3])
        sleep(5)
        self.driver.find_element(*self.service_d).click()
        iframe = self.driver.find_element(*self.service_e)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*self.service_h)
        self.driver.find_element(*self.service_f).send_keys(data[4])
        self.driver.find_element(*self.service_g).click()
        # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        num = self.driver.find_element(*self.service_j).text
        element = self.driver.find_element(*self.service_j)
        # 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.service_k).click()

        print(num)

        sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    T = Service(Common)
    T.service()