import pytest
from Base.BaseOperate import Operate
from Base.BaseRunner import TestCase
import allure
import time


@allure.story("定位模块")
@pytest.mark.app
class TestLocate(TestCase):

    @pytest.mark.smoking
    def test_01(self):
        path = "../Xls/locate.xls"
        name = "my"
        data = Operate(self.driver).get_element_operate(path, name)
        time.sleep(5)
        assert data is True


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_01.py"])