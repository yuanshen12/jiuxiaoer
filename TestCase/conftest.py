import pytest
from Base.BaseRunner import app
from PageOject.Home.home import Home


@pytest.fixture()
def login():
    print("需要登录")


@pytest.fixture()
def setup_module(self):
    Home(self.driver).call_locate()
