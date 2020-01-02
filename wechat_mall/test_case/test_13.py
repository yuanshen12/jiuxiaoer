from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Me.Me_four import Me_four
import unittest
import logging

class Test_M(StartEnd):

      def test_120(self):
            logging.info('======test_120=====')
            L = Me_four(self.driver)
            L.open()
            self.assertTrue(L.Zuji(1),msg='我的足迹')

      def test_121(self):
            logging.info('======test_121=====')
            L = Me_four(self.driver)
            self.assertTrue(L.Zuji(2),msg='我的收藏')

      def test_123(self):
            logging.info('======test_123=====')
            L = Me_four(self.driver)
            self.assertTrue(L.Zuji(3),msg='我的问答')

      def test_124(self):
            logging.info('======test_124=====')
            L = Me_four(self.driver)
            self.assertTrue(L.Zuji(4),msg='我的会员')

      def test_125(self):
            logging.info('======test_125=====')
            L = Me_four(self.driver)
            self.assertTrue(L.Zuji(5),msg='我的发票')

      def test_126(self):
            logging.info('======test_126=====')
            L = Me_four(self.driver)
            self.assertTrue(L.Zuji(6),msg='地址管理')

if __name__ == '__main__':
    unittest.main()