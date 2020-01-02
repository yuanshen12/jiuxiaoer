from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Drink.switch_wine import Switch_wine
import unittest
import logging

class Test_C(StartEnd):
      def test_29(self):
            logging.info('======test_29=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Grape(),msg='断言从首页进入红酒页面成功')

      def test_30(self):
            logging.info('======test_30=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.TO_sales(),msg='断言切换销量排序成功')

      def test_31(self):
            logging.info('======test_31=====')
            L = Switch_wine(self.driver)
            self.assertGreaterEqual(L.prich_One(),L.prich_Two(),msg='断言切换价格从高到低切成功')

      def test_32(self):
            logging.info('======test_32=====')
            L = Switch_wine(self.driver)
            self.assertLessEqual(L.prich_Low(),L.prich_Two(),msg='断言切换价格从低到高成功')

      def test_33(self):
            logging.info('======test_33=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Comprehensive(),msg='断言切换综合排序成功')

      def test_34(self):
            logging.info('======test_34=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Brand(),msg='断言切换到筛选品牌成功')

      def test_35(self):
            logging.info('======test_35=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Prich_screen(),msg='断言切换到筛选价格成功')

      def test_36(self):
            logging.info('======test_36=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Type(),msg='断言切换到筛选类型成功')

      def test_37(self):
            logging.info('======test_37=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Place(),msg='断言切换到筛选产地成功')

      def test_38(self):
            logging.info('======test_38=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Ethyl(),msg='断言切换到筛选酒精度成功')

      def test_39(self):
            logging.info('======test_39=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Capacity(),msg='断言切换到筛选容量成功')

      def test_40(self):
            logging.info('======test_40=====')
            L = Switch_wine(self.driver)
            self.assertTrue(L.Reset(),msg='断言筛选页面重置成功')

      def test_41(self):
            logging.info('======test_41=====')
            L = Switch_wine(self.driver)
            suer = L.liquor_text()
            self.assertEqual(suer,L.TO_suer(),msg='断言切换到白酒页面成功')

      def test_42(self):
            logging.info('======test_42=====')
            L = Switch_wine(self.driver)
            suer = L.foreign_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到洋酒页面成功')

      def test_43(self):
            logging.info('======test_43=====')
            L = Switch_wine(self.driver)
            suer = L.beer_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到啤酒页面成功')

      def test_44(self):
            logging.info('======test_44=====')
            L = Switch_wine(self.driver)
            suer = L.wine_text()
            self.assertEqual(suer, L.TO_suer(), msg='断言切换到红酒页面成功')

      def test_45(self):
            logging.info('======test_45=====')
            L = Switch_wine(self.driver)
            suer = L.drunk_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到下酒菜页面成功')

      def test_46(self):
            logging.info('======test_46=====')
            L = Switch_wine(self.driver)
            suer = L.drinks_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到饮料页面成功')

if __name__ == '__main__':
    unittest.main()