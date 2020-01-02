from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.sousou import sousou
import unittest
import logging

class Test_N(StartEnd):

      def test_127(self):
            logging.info('======test_127=====')
            L = sousou(self.driver)
            T = L.Sou_qingouwuche()
            self.assertEqual(L.Sou_jiarugouwuche(),T)

      def test_128(self):
          logging.info('======test_128=====')
          L = sousou(self.driver)
          T = L.Jiesuan()
          self.assertEqual(L.Jiesuan1(), T)


if __name__ == '__main__':
    unittest.main()