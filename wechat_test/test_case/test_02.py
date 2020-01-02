from wechat_test.common.myunit import StartEnd
from wechat_test.businessView.search import Search
import unittest
import logging

class SE(StartEnd):
    csv_file='../data/account.csv'

    def test_02(self):
        logging.info('======test_02=====')
        num = Search(self.driver)
        data = num.get_csv_data(self.csv_file, 2)
        search = num.Search_a()
        self.assertIn(data[1],search,msg="搜索指定酒")

    def test_03(self):
        logging.info('======test_03=====')
        num = Search(self.driver)
        self.assertTrue(num.Search_b(),msg="搜索页面加入购物车")

    def test_04(self):
        logging.info('======test_04=====')
        num = Search(self.driver)
        data = num.get_csv_data(self.csv_file, 4)
        sellte = num.Search_c()
        self.assertIn(data[6],sellte,msg="购物车进入结算页面")


if __name__ == '__main__':
    unittest.main()