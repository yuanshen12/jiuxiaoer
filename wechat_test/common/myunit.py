import unittest
from wechat_test.common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        logging.info('=====setUp====')
        self.driver=appium_desired()

    @classmethod
    def tearDownClass(self) -> None:
        logging.info('====tearDown====')
        # sleep(5)
        self.driver.close_app()

class Start(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        self.driver.close_app()