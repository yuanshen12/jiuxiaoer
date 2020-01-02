from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Drink.switch_beer import Switch
from wechat_mall.common.common_fun import Common
import unittest
import logging

class Tset_B(StartEnd):

    def test_10(self):
        logging.info('======test_10=====')
        L = Switch(self.driver)
        suer = L.Beer_text()
        Common.wait(self)
        self.assertEqual(suer, L.TO_suer(), msg='断言从首页进入啤酒页面成功')

    def test_11(self):
        logging.info('======test_11=====')
        L = Switch(self.driver)
        self.assertTrue(L.TO_sales(), msg='断言切换销量排序成功')

    def test_12(self):
        logging.info('======test_12=====')
        L = Switch(self.driver)
        self.assertGreater(L.prich_One(), L.prich_Two(), msg='断言切换价格从高到低切成功')

    def test_13(self):
        logging.info('======test_13=====')
        L = Switch(self.driver)
        self.assertLessEqual(L.prich_Low(), L.prich_Two(), msg='断言切换价格从低到高成功')

    def test_14(self):
        logging.info('======test_14=====')
        L = Switch(self.driver)
        self.assertTrue(L.Comprehensive(), msg='断言切换综合排序成功')

    def test_15(self):
        logging.info('======test_15=====')
        L = Switch(self.driver)
        self.assertTrue(L.Brand(), msg='断言切换到筛选品牌成功')

    def test_16(self):
        logging.info('======test_16=====')
        L = Switch(self.driver)
        self.assertTrue(L.Prich_screen(), msg='断言切换到筛选价格成功')

    def test_17(self):
        logging.info('======test_17=====')
        L = Switch(self.driver)
        self.assertTrue(L.Type(), msg='断言切换到筛选类型成功')

    def test_18(self):
        logging.info('======test_18=====')
        L = Switch(self.driver)
        self.assertTrue(L.Place(), msg='断言切换到筛选产地成功')

    def test_19(self):
        logging.info('======test_19=====')
        L = Switch(self.driver)
        self.assertTrue(L.Ethyl(), msg='断言切换到筛选酒精度成功')

    def test_20(self):
        logging.info('======test_20=====')
        L = Switch(self.driver)
        self.assertTrue(L.Malt(), msg='断言切换到筛选麦芽度成功')

    def test_21(self):
        logging.info('======test_21=====')
        L = Switch(self.driver)
        self.assertTrue(L.Capacity(), msg='断言切换到筛选容量成功')

    def test_22(self):
        logging.info('======test_22=====')
        L = Switch(self.driver)
        self.assertTrue(L.Reset(), msg='断言筛选页面重置成功')

    def test_23(self):
        logging.info('======test_23=====')
        L = Switch(self.driver)
        suer = L.wine_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到红酒页面成功')

    def test_24(self):
        logging.info('======test_12=====')
        L = Switch(self.driver)
        suer = L.liquor_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到白酒页面成功')

    def test_25(self):
        logging.info('======test_13=====')
        L = Switch(self.driver)
        suer = L.foreign_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到洋酒页面成功')

    def test_26(self):
        logging.info('======test_14=====')
        L = Switch(self.driver)
        suer = L.beer_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到啤酒页面成功')

    def test_27(self):
        logging.info('======test_15=====')
        L = Switch(self.driver)
        suer = L.drunk_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到下酒菜页面成功')

    def test_28(self):
        logging.info('======test_16=====')
        L = Switch(self.driver)
        suer = L.drinks_text()
        self.assertEqual(suer, L.TO_suer(), msg='断言切换到饮料页面成功')


if __name__ == '__main__':
    unittest.main()