from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.activity import activity
import unittest
import logging

class Test_G(StartEnd):

      def test_81(self):
            logging.info('======test_82=====')
            L = activity(self.driver)
            self.assertTrue(L.deles(),msg='清空购物车')

      def test_82(self):
            logging.info('======test_82=====')
            L = activity(self.driver)
            self.assertIn('帮你挑',L.Suer(),msg='首页新用户首单页面')

      def test_83(self):
            logging.info('======test_83=====')
            L = activity(self.driver)
            self.assertIn('帮你挑', L.Goddes(), msg='首页女神专区')

      def test_84(self):
            logging.info('======test_84=====')
            L = activity(self.driver)
            Foods = L.Foods()
            self.assertIn(L.Food(),Foods,msg='首页饮料小食')

      def test_85(self):
            logging.info('======test_85=====')
            L = activity(self.driver)
            self.assertTrue(L.Pot(),msg='首页酒友圈')

      # def test_86(self):
      #       logging.info('======test_86=====')
      #       L = activity(self.driver)
      #       self.assertTrue(L.New(),msg='首页进入新用户首单')
      #
      # def test_87(self):
      #       logging.info('======test_87=====')
      #       L = activity(self.driver)
      #       self.assertTrue(L.Full(),msg='首页进入下单满减')
      #
      # def test_88(self):
      #       logging.info('======test_89=====')
      #       L  = activity(self.driver)
      #       self.assertTrue(L.Hot(),msg='首页进入热销')

      # def test_89(self):
      #       logging.info('======test_91=====')
      #       L = activity(self.driver)
      #       suer = L.num(1, 1)
      #       self.assertEqual(L.num_d(4, 1), suer,msg='首页进入啤酒专题')
      #
      # def test_90(self):
      #       logging.info('======test_91=====')
      #       L = activity(self.driver)
      #       suer = L.num(4, 2)
      #       self.assertEqual(L.num_d(7, 2), suer,msg='首页进入红酒专题')
      #
      # def test_91(self):
      #       logging.info('======test_91=====')
      #       L = activity(self.driver)
      #       suer = L.num(7, 3)
      #       self.assertEqual(L.num_d(10, 3), suer,msg='首页进入白酒专题')
      #
      # def test_92(self):
      #       logging.info('======test_92=====')
      #       L = activity(self.driver)
      #       suer = L.num(10, 4)
      #       self.assertEqual(L.num_d(13, 4), suer, msg='首页进入洋酒专题')

      # def test_93(self):
      #       logging.info('======test_93=====')
      #       L = activity(self.driver)
      #       gouwu = L.Gouwu()
      #       self.assertEqual(L.Gouwu_C(),gouwu,msg='加入购物车')
      #
      # def test_94(self):
      #       logging.info('======test_93=====')
      #       L = activity(self.driver)
      #       J = L.jiesuan()
      #       self.assertEqual(L.Jin(),J,msg='结算')



if __name__ == '__main__':
    unittest.main()