import allure
import pytest


class TestReport:

    @allure.title('第一步')
    def test_01(self):
        print('test_01')
        assert 1

    @allure.title('第二步')
    def test_02(self):
        print('test_02')
        assert 1

    @allure.title('第三步')
    def test_03(self):
        print('test_03')
        assert 0, '出错'