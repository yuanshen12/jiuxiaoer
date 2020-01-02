from wechat_test.businessView.me import Me
from wechat_test.common.myunit import StartEnd
import unittest
import logging

class Delete(StartEnd):
    csv_file = '../data/account.csv'

    def test_22(self):
        logging.info('======test_22=====')
        num = Me(self.driver)
        self.assertEqual(num.me_A(),1,msg="删除收货地址")

if __name__ == '__main__':
    unittest.main()