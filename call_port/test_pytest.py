import pytest
import requests


@pytest.fixture(scope='module')
def setup_module():
    print('模块执行前')


def teardown_module():
    print('模块执行后')


def setup_function():
    print('执行前')


def teardown_function():
    print('执行后')


def login():
    print('传登录')


    yield
    print("执行teardown!")
    print('关闭浏览器')

def test_one():
    assert 9 in range(10)


def test_two(login):
    assert 7 not in range(8)


def test_three(login):
    x = 'yes'
    assert 'y' not in x


class Testclass:
    def setup_class(self):
        print('所有用例执行前类')

    def teardown_class(self):
        print("所有用例执行后类")

    def setup_method(self):
        print('每个模块前只执行一次')

    def teardown_method(self):
        print('每个模块后执行一次')

    def setup(self):
        print('执行前')

    def teardown(self):
        print('执行后')

    def test1(self):
        url = requests.get('https://m.jiuxiaoer.cn')
        code = url.status_code
        assert code == 200

    def test2(self):
        url = requests.get('https://e.jiuxiaoer.cn')
        content = url.content
        assert 'jiuxiaoer' in content

    def test3(self):
        url = requests.get('https://m.jiuxiaoer.cn')
        headers = url.headers
        assert 'jiuxiaoer.cn' in str(headers)

    def test4(self):
        url = requests.get('https://m.jiuxiaoer.cn')
        url_test = url.url
        assert 'https://m.jiuxiaoer.cn/' == url_test

    def test5(self):
        url = requests.get('https://m.jiuxiaoer.cn')
        encoding = url.encoding
        assert encoding == 'UTF-8'

    def test6(self):
        url = requests.get("https://m.jiuxiao2.cn/api/mobile-page-advert/list?siteId=25")
        headers = url.text
        assert '成功' in headers


if __name__ == "__main__":
    pytest.main('-s', 'test_pytest.py')

