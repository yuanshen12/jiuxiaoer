import logging
from selenium.webdriver.common.by import By
from wechat_mall.common.common_fun import Common
from wechat_mall.common.Login import Login


# 从首页进入指定的酒类
class Open(Common):
    # 啤酒
    beer = (By.XPATH,"//*[contains(text(), '啤酒')]")
    beer_open = (By.XPATH,'/html/body/nav[2]/ul/li[1]/a')
    # 葡萄酒
    wine = (By.XPATH,"//*[contains(text(), '葡萄酒')]")
    wine_open = (By.XPATH,'/html/body/nav[2]/ul/li[1]/a')
    # 白酒
    liquor = (By.XPATH, "//*[contains(text(), '白酒')]")
    liquor_open = (By.XPATH, '/html/body/nav[2]/ul/li[1]/a')
    # 洋酒
    foreign = (By.XPATH, "//*[contains(text(), '洋酒')]")
    foreign_open = (By.XPATH, '/html/body/nav[2]/ul/li[1]/a')


    def Beer_open(self):
        logging.info('============Beer_open==============')
        try:
            self.driver.find_element(*self.beer).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.driver.find_element(*self.beer_open)
            return True


    def Wine_open(self):
        logging.info('============Wine_open==============')
        try:
            self.driver.find_element(*self.wine).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.driver.find_element(*self.wine_open)
            return True

    def Liquor_open(self):
        logging.info('============Liquor_open==============')
        try:
            self.driver.find_element(*self.liquor).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.driver.find_element(*self.liquor_open)
            return True

    def Foreign_open(self):
        logging.info('============Foreign_open==============')
        try:
            self.driver.find_element(*self.foreign).click()
        except:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.driver.find_element(*self.foreign_open)
            return True


if __name__ == '__main__':
    driver = appium_desired()
    L = Open(driver)
    L.Beer_open()


