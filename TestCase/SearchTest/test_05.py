import pytest
from Base.BaseRunner import TestCase
from PageOject.Home.home import Home
from time import sleep


class TestLocate(TestCase):

    def test_05(self):
        Home(self.driver).home_locate()
        print(5)
        sleep(5)


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_05.py"])