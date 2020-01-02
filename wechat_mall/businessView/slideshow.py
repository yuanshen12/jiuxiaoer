import logging
from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from selenium.webdriver.common.action_chains import ActionChains

# 轮播图
class slideshow(Common):
    One = (By.XPATH,'/html/body/section[1]/article[3]/ul/li[1]')
    Two = (By.XPATH,"/html/body/section[1]/article[3]/ul/li[2]")
    three = (By.XPATH,'/html/body/section[1]/article[1]/a[2]')
# 第一张轮播图
    def slideshow_one(self):
        logging.info('============slideshow_one==============')
        self.wait()
        self.driver.find_element(*self.One).click()
        title = self.driver.title
        return title
# 第二张轮播图
    def slideshow_two(self):
        logging.info('============slideshow_two==============')
        self.wait()
        # self.driver.find_element(*self.One).click()
        Two = self.driver.find_element(*self.Two)
        ActionChains(self.driver).key_up(Two).perform()
        title = self.driver.title
        return title
# 第三张轮播图
    def slideshow_three(self):
        logging.info('============slideshow_three==============')
        self.wait()
        self.driver.find_element(*self.three).click()
        title = self.driver.title
        return title
