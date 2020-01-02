from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Me.personal import Geren
import unittest
import logging

class Test_J(StartEnd):

      def test_105(self):
            logging.info('======test_105=====')
            L = Geren(self.driver)
            EL = L.Nicheng()
            self.assertEqual('道德许可',EL,msg='改昵称')

      def test_106(self):
            logging.info('======test_106=====')
            L = Geren(self.driver)
            EL = L.Xinbie()
            self.assertEqual('女', EL,msg='改性别')

      def test_107(self):
            logging.info('======test_107=====')
            L = Geren(self.driver)
            EL = L.Shengri()
            self.assertIn(EL,L.Shengre(),msg='改生日')

      def test_108(self):
            logging.info('======test_108=====')
            L = Geren(self.driver)
            EL = L.Xinqu()
            self.assertEqual(EL,'健康饮酒')

      def test_109(self):
            logging.info('======test_109=====')
            L = Geren(self.driver)
            self.assertTrue(L.Xinqu_S())


if __name__ == '__main__':
    unittest.main()