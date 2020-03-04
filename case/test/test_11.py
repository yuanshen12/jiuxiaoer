import pytest


#  文件名以test_.py开头，类以test开头，函数和方法以test开头

def locate(age):
    return age * 1.25


@pytest.mark.slow
def test_01():
    assert locate(10) == 12


@pytest.mark.case
class TestClass:

    def test_location(self):
        h = "酒小二"
        assert '三' in h


# 模块级
# def setup_module():
#     print("模块级")
#
#
# def teardown_module():
#     print("模块结束")
#
#
# def setup_function():
#     print("函数级")
#
#
# def test_02():
#     assert 0 == 1
