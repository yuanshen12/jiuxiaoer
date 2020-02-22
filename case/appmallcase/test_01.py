from appmall.home.call_home import Home
from appmall.locate.call_locate import Locate
from common.call_statend import TestCase
import pytest


class TestHome(TestCase):

    def test_1(self):
        name = Home(self.driver)
        with pytest.raises(None, message="Exceptions ZeroDivisionError") as exinfo:
            name.home_cart()
        assert exinfo.value is None

    def test_2(self, locate):
        name = Locate(self.driver)
        names = name.call_seek(locate)


if __name__ == "__main__":
    pytest.main(['-s', '-q', 'test_01.py'])