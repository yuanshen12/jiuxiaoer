from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.locate import locate,receipt_new,cut
import unittest
import pytest
import logging


class Test_A(StartEnd):

    @unittest.skipUnless('test_01', u"为False的时候跳过")
    def test_01(self):
        logging.info('======test_01=====')
        title = self.driver.title
        L = locate(self.driver)
        L.location_determine()
        self.assertIn(L.location_text(),title,msg='判断首页定位与定位页面一致')

    @unittest.skipUnless('test_02', u"为False的时候跳过")
    def test_02(self):
        logging.info('======test_02=====')
        L = locate(self.driver)
        P = L.current_text()
        L.location_current()
        self.assertEqual(L.locate_text(),P,msg='判断当前定位是否切换成功')

    @unittest.skipUnless('test_03', u"为False的时候跳过")
    def test_03(self):
        logging.info('======test_03=====')
        L = locate(self.driver)
        L.location_determine()
        P = L.receipt_text()
        L.location_receipt()
        self.assertIn(L.locate_text(),P,msg= '判断收货定位是否切换成功')

    @unittest.skipUnless('test_04', u"为False的时候跳过")
    def test_04(self):
        logging.info('======test_04=====')
        L = locate(self.driver)
        L.location_determine()
        P = L.near_text()
        L.lacation_near()
        self.assertEqual(L.locate_text(),P,msg='判断附近定位是否切换成功')

    @unittest.skipUnless('test_05', u"为False的时候跳过")
    def test_05(self):
        logging.info('======test_05=====')
        L = locate(self.driver)
        L.location_determine()
        P = receipt_new(self.driver)
        self.assertTrue(P.receipt(),msg='判断新增收货地址成功')

    @unittest.skipUnless('test_06', u"为False的时候跳过")
    def test_06(self):
        logging.info('======test_06=====')
        P = receipt_new(self.driver)
        self.assertTrue(P.delete_open(),msg='判断删除收货地址成功')

    @unittest.skipUnless('test_07', u"为False的时候跳过")
    def test_07(self):
        logging.info('======test_07=====')
        L = locate(self.driver)
        L.location_determine()
        P = cut(self.driver)
        self.assertTrue(P.cut_open(),msg='切换区域成功')

    @unittest.skipUnless('test_08', u"为False的时候跳过")
    def test_08(self):
        logging.info('======test_08=====')
        P = cut(self.driver)
        self.assertTrue(P.cut_seeks(),msg='搜索并选择地址成功')

    @unittest.skipUnless('test_09', u"为False的时候跳过")
    def test_09(self):
        logging.info('======test_09=====')
        P = cut(self.driver)
        self.assertTrue(P.cut_map(),msg='切换地图选择地址成功')

if __name__ == '__main__':
    unittest.main()


