from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.indent import indent
import unittest
import logging

class Test_I(StartEnd):

      def test_100(self):
            logging.info('======test_100=====')
            L = indent(self.driver)
            L.open()
            self.assertTrue(L.qiehuan(1),msg='切换代付款')

      def test_101(self):
            logging.info('======test_101=====')
            L = indent(self.driver)
            self.assertTrue(L.qiehuan(2),msg='切换待收货')

      def test_102(self):
            logging.info('======test_102=====')
            L = indent(self.driver)
            self.assertTrue(L.qiehuan(3),msg='切换待收货')

      def test_103(self):
            logging.info('======test_103=====')
            L = indent(self.driver)
            self.assertTrue(L.qiehuan(4),msg='切换待评价')

      def test_104(self):
            logging.info('======test_103=====')
            L = indent(self.driver)
            self.assertTrue(L.like(),msg='没有订单进入立即下单')

if __name__ == '__main__':
    unittest.main()