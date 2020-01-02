from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.discover import discover
import unittest
import logging

class Test_H(StartEnd):

      def test_95(self):
            logging.info('======test_95=====')
            L = discover(self.driver)
            self.assertTrue(L.Qiehuan(1))

      def test_96(self):
            logging.info('======test_97=====')
            L = discover(self.driver)
            self.assertTrue(L.Qiehuan(2))

      def test_97(self):
            logging.info('======test_98=====')
            L = discover(self.driver)
            self.assertTrue(L.Qiehuan(0))

      def test_98(self):
            logging.info('======test_95=====')
            L = discover(self.driver)
            self.assertTrue(L.Faxian())

      def test_99(self):
            logging.info('======test_96=====')
            L = discover(self.driver)
            SUAN = L.Xiangqin()
            self.assertEqual(L.Xiang(),SUAN,)



if __name__ == '__main__':
    unittest.main()