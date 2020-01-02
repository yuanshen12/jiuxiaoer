import unittest
from wechat_mall.common.Login import Login
import logging
from time import sleep


# CON_LOG='../config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()

class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        logging.info('=====setUp====')
        self.driver=Login().open()

    @classmethod
    def tearDownClass(self) -> None:
        logging.info('====tearDown====')
        sleep(10)
        self.driver.close_app()
