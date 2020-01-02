from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Me.Me_to import Me_to
import unittest
import logging

class Test_J(StartEnd):

      def test_110(self):
            logging.info('======test_110=====')
            L = Me_to(self.driver)
            self.assertTrue(L.Chengzhangzhi(),msg='成长值')

      def test_111(self):
            logging.info('======test_111=====')
            L = Me_to(self.driver)
            self.assertTrue(L.Jifen(),msg= '积分')

      def test_112(self):
            logging.info('======test_112=====')
            L = Me_to(self.driver)
            self.assertTrue(L.Xiangxi(),msg='积分详细')

      def test_113(self):
            logging.info('======test_113=====')
            L = Me_to(self.driver)
            self.assertTrue(L.Youhuijuan(), msg='优惠劵')

      def test_114(self):
            logging.info('======test_114=====')
            L = Me_to(self.driver)
            self.assertTrue(L.Y_xiangqin(), msg='优惠劵详细')


if __name__ == '__main__':
    unittest.main()