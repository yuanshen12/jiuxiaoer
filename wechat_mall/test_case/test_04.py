from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Drink.switch_liquor import Switch_liquor
import unittest
import logging

class Test_D(StartEnd):
      def test_47(self):
            logging.info('======test_47=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Spilits(),msg='断言从首页进入白酒页面成功')

      def test_48(self):
            logging.info('======test_48=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.TO_sales(),msg='断言切换销量排序成功')

      def test_49(self):
            logging.info('======test_49=====')
            L = Switch_liquor(self.driver)
            self.assertGreaterEqual(L.prich_One(),L.prich_Two(),msg='断言切换价格从高到低切成功')

      def test_50(self):
            logging.info('======test_50=====')
            L = Switch_liquor(self.driver)
            self.assertLessEqual(L.prich_Low(),L.prich_Two(),msg='断言切换价格从低到高成功')

      def test_51(self):
            logging.info('======test_51=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Comprehensive(),msg='断言切换综合排序成功')

      def test_52(self):
            logging.info('======test_52=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Brand(),msg='断言切换到筛选品牌成功')

      def test_53(self):
            logging.info('======test_53=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Prich_screen(),msg='断言切换到筛选价格成功')


      def test_54(self):
            logging.info('======test_54=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Place(),msg='断言切换到筛选产地成功')

      def test_55(self):
            logging.info('======test_55=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Ethyl(),msg='断言切换到筛选酒精度成功')

      def test_56(self):
            logging.info('======test_56=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Capacity(),msg='断言切换到筛选容量成功')

      def test_57(self):
            logging.info('======test_57=====')
            L = Switch_liquor(self.driver)
            self.assertTrue(L.Reset(),msg='断言筛选页面重置成功')

      def test_58(self):
            logging.info('======test_58=====')
            L = Switch_liquor(self.driver)
            suer = L.wine_text()
            self.assertEqual(suer, L.TO_suer(), msg='断言切换到红酒页面成功')

      def test_59(self):
            logging.info('======test_59=====')
            L = Switch_liquor(self.driver)
            suer = L.liquor_text()
            self.assertEqual(suer,L.TO_suer(),msg='断言切换到白酒页面成功')

      def test_60(self):
            logging.info('======test_60=====')
            L = Switch_liquor(self.driver)
            suer = L.foreign_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到洋酒页面成功')

      def test_61(self):
            logging.info('======test_61=====')
            L = Switch_liquor(self.driver)
            suer = L.beer_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到啤酒页面成功')

      def test_62(self):
            logging.info('======test_62=====')
            L = Switch_liquor(self.driver)
            suer = L.drunk_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到下酒菜页面成功')

      def test_63(self):
            logging.info('======test_63=====')
            L = Switch_liquor(self.driver)
            suer = L.drinks_text()
            self.assertEqual(suer, L.TO_suer(),msg='断言切换到饮料页面成功')

if __name__ == '__main__':
    unittest.main()