from wechat_test.common.myunit import StartEnd
from wechat_test.businessView.search import Search
import unittest
import logging

class Seek(StartEnd):
    csv_file='../data/account.csv'

    def test_05(self):
        logging.info('======test_05=====')
        num = Search(self.driver)
        data = num.get_csv_data(self.csv_file, 4)
        sellte = num.Search_d()
        self.assertIn(data[6], sellte,msg="搜索页面加入购物车立即购买结算")

    def test_06(self):
        logging.info('======test_06=====')
        num = Search(self.driver)
        data = num.get_csv_data(self.csv_file, 2)
        self.assertIn(data[1],num.Search_e(),msg="检查搜索历史")

    def test_07(self):
        logging.info('======test_07=====')
        num = Search(self.driver)
        self.assertTrue(num.Search_f(),msg="清空搜索历史")

    def test_08(self):
        logging.info('======test_08=====')
        num = Search(self.driver)
        data = num.get_csv_data(self.csv_file, 4)
        sellte = num.Search_g()
        self.assertIn(data[6], sellte,msg="搜索页面点击去结算")



if __name__ == '__main__':
    unittest.main()