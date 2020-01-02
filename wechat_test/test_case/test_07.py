from wechat_test.businessView.reduced_web import Reduced_web
from wechat_test.businessView.reduced import Reduced
from wechat_test.common.desired_caps import appium_desired
import unittest
import logging

class Gift(unittest.TestCase):
    csv_file = '../data/account.csv'

    def test_23(self):
        logging.info('======test_23=====')
        num = Reduced_web(self)
        num.reduced(0)
        try:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        except:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        try:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_A(),msg='满减满赠送积分')
        except:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_A(), msg='满减满赠送积分')

    def test_24(self):
        logging.info('======test_24=====')
        num = Reduced_web(self)
        num.reduced(1)
        try:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        except:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        try:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_B(), msg='满减满赠送成长值')
        except:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_B(), msg='满减满赠送成长值')

    def test_25(self):
        logging.info('======test_25=====')
        num = Reduced_web(self)
        num.reduced(2)
        try:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        except:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced()
        try:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_C(), msg='满减满赠送优惠券')
        except:
            driver = appium_desired()
            Q = Reduced(driver)
            self.assertTrue(Q.reduced_C(), msg='满减满赠送优惠券')

    def test_26(self):
        logging.info('======test_26=====')
        num = Reduced_web(self)
        num.reduced(3)
        driver = appium_desired()
        P = Reduced(driver)
        P.reduced(1)
        self.assertTrue(P.reduced_D(),msg="满减满赠送赠品")

    def test_27(self):
        logging.info('======test_27=====')
        num = Reduced_web(self)
        num.reduced(4)
        driver = appium_desired()
        P = Reduced(driver)
        P.reduced(1)
        self.assertEqual(60,P.reduced_E(),msg="满减满赠减一百")

    def test_28(self):
        logging.info('======test_28=====')
        num = Reduced_web(self)
        num.reduced(5)
        driver = appium_desired()
        P = Reduced(driver)
        P.reduced(1)
        self.assertEqual(80,P.reduced_E(),msg="满减满赠减一百(打折)")

    def test_29(self):
        logging.info('======test_29=====')
        num = Reduced_web(self)
        num.reduced(6)
        driver = appium_desired()
        try:
            P = Reduced(driver)
            P.reduced(1)
        except:
            driver = appium_desired()
            P = Reduced(driver)
            P.reduced(1)
        self.assertTrue(P.reduced_F(), msg="选择赠品为零时自动下架")

    def test_30(self):
        logging.info('======test_30=====')
        num = Reduced_web(self)
        num.reduced(7)
        driver = appium_desired()
        P = Reduced(driver)
        P.reduced(1)
        self.assertTrue(P.reduced_D(), msg="不选择赠品为零时自动下架，活动不会自动下架")

    def test_31(self):
        logging.info('======test_31=====')
        num = Reduced_web(self)
        num.reduced(8)
        driver = appium_desired()
        P = Reduced(driver)
        self.assertTrue(P.reduced_G(),msg='仅限新用户参与')

    def test_32(self):
        logging.info('======test_32=====')
        num = Reduced_web(self)
        num.reduced(9)
        driver = appium_desired()
        P = Reduced(driver)
        self.assertTrue(P.reduced_H(),msg='删除活动成功')


if __name__ == '__main__':
    unittest.main()

