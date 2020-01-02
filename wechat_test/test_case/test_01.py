from wechat_test.common.myunit import StartEnd
from wechat_test.businessView.scation import Scation
import unittest
import logging

class Location(StartEnd):
    csv_file='../data/account.csv'

    def test_01(self):
        logging.info('======test_scation=====')
        num = Scation(self.driver)
        data = num.get_csv_data(self.csv_file,1)
        guiyang = num.scation_guiyang()
        self.assertIn(data[1],guiyang,msg='切换定位至贵阳站')

if __name__ == '__main__':
    unittest.main()