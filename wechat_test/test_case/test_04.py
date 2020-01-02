from wechat_test.common.myunit import StartEnd
from wechat_test.businessView.switch import Switch,Switch_comprehensive,Switch_screen
import unittest
import logging

class Drink(StartEnd):
    csv_file = '../data/account.csv'

    def test_09(self):
        logging.info('======test_09=====')
        num = Switch(self.driver)
        num.Switch_A(1)
        self.assertTrue(num.Switch_B(),msg="马上喝酒类切换")

    def test_10(self):
        logging.info('======test_10=====')
        num = Switch_comprehensive(self.driver)
        self.assertTrue(num.Switch_A(),msg="马上喝排序切换")

    def test_11(self):
        logging.info('======test_11=====')
        num = Switch_screen(self.driver)
        self.assertTrue(num.Switch_A(),msg="马上喝筛选切换")

    def test_12(self):
        logging.info('======test_12=====')
        num = Switch_screen(self.driver)
        data = num.get_csv_data(self.csv_file, 4)
        B = num.Switch_B()
        self.assertIn(data[6],B,msg="马上喝加入购物立即购买")

if __name__ == '__main__':
    unittest.main()