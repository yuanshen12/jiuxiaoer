from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Me.Me_three import Me_three
import unittest
import logging

class Test_L(StartEnd):

      def test_115(self):
            logging.info('======test_115=====')
            L = Me_three(self.driver)
            EL = L.Wo()
            self.assertEqual(L.Wo_ding(),EL, msg='优惠劵详细')

      def test_116(self):
            logging.info('======test_116=====')
            L = Me_three(self.driver)
            EL = L.Daifu(0)
            self.assertEqual(L.Daifu_A(0),EL, msg='优惠劵详细')

      def test_117(self):
            logging.info('======test_117=====')
            L = Me_three(self.driver)
            EL = L.Daifu(1)
            self.assertEqual(L.Daifu_A(1), EL, msg='优惠劵详细')

      def test_118(self):
            logging.info('======test_118=====')
            L = Me_three(self.driver)
            EL = L.Daifu(2)
            self.assertEqual(L.Daifu_A(2), EL, msg='优惠劵详细')

      def test_119(self):
            logging.info('======test_119=====')
            L = Me_three(self.driver)
            EL = L.Daifu(3)
            self.assertEqual(L.Daifu_A(3), EL, msg='优惠劵详细')

if __name__ == '__main__':
    unittest.main()