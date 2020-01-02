from wechat_mall.common.myunit import StartEnd
from wechat_mall.businessView.Me.Me_five import Me_five
import unittest
import logging

class Test_N(StartEnd):

      def test_126(self):
            logging.info('======test_126=====')
            L = Me_five(self.driver)
            L.open()
            self.assertTrue(L.Bangzhu(),msg='帮助中心')

if __name__ == '__main__':
    unittest.main()