import pytest
from Base.BaseOperate import Operate
from Base.BaseRunner import TestCase
import allure
import time


@allure.story("个人中心")
@pytest.mark.app
class TestMy(TestCase):

    @pytest.mark.smoking
    def test_01(self):
        path = "../Xls/locate.xls"
        name = "my"
        data = Operate(self.driver).get_element_operate(path, name)
        time.sleep(5)
        assert data is True


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_05.py"])