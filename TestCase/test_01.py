from Base.BaseRunner import app
import pytest


def test_01():
    print(1)


def test_02(login):
    print(2)


def test_03(setup_module):
    print(3)


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_01.py'])
