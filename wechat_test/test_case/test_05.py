from wechat_test.businessView.drink import Drink
from wechat_test.common.TMS import TMS
from wechat_test.common.desired_caps import appium_desired
import unittest
import logging

class State(unittest.TestCase):
    csv_file = '../data/account.csv'

    def test_13(self):
        logging.info('======test_13=====')
        driver = appium_desired()
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 4)
        B = num.drink_A()
        self.assertIn(data[6], B, msg="马上喝购买成功")

    def test_14(self):
        driver = appium_desired()
        logging.info('======test_14=====')
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 7)
        B = num.drink_B()
        self.assertIn(data[1],B, msg="检测待响应状态")

    # def test_15(self):
    #     logging.info('======test_15=====')
    #     num = TMS(self)
    #     num.Tms(1)

    def test_16(self):
        logging.info('======test_16=====')
        P = TMS(self)
        P.Tms(1)
        driver = appium_desired()
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 7)
        C = num.drink_C()
        self.assertIn(data[3],C, msg="检测待发货状态")

    # def test_17(self):
    #     logging.info('======test_17=====')
    #     num = TMS(self)
    #     num.Tms(2)

    def test_18(self):
        logging.info('======test_18=====')
        P = TMS(self)
        P.Tms(2)
        driver = appium_desired()
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 7)
        C = num.drink_C()
        self.assertIn(data[4], C, msg="检测待收货状态")

    # def test_19(self):
    #     logging.info('======test_19=====')
    #     num = TMS(self)
    #     num.Tms(3)

    def test_20(self):
        logging.info('======test_20=====')
        P = TMS(self)
        P.Tms(3)
        driver = appium_desired()
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 7)
        C = num.drink_C()
        self.assertIn(data[5], C, msg="检测交易已完成状态")

    def test_21(self):
        logging.info('======test_21=====')
        driver = appium_desired()
        num = Drink(driver)
        data = num.get_csv_data(self.csv_file, 7)
        E = num.drink_E()
        self.assertIn(data[2], E, msg="检测待付款状态")

if __name__ == '__main__':
    unittest.main()