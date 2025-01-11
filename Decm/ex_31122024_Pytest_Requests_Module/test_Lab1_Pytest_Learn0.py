import pytest
import allure
import requests


@allure.title("TC1 - Verify that what is 2-2 == 0")
@allure.description("This is basic mathematics test")
@pytest.mark.smoke
def test_basic_math():
     assert 2-2 == 0

@allure.title("TC2 - Verify that 3-3 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0

@allure.title("TC3 - verify that 1-1 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub2():
    assert 1 - 1 == 0

@pytest.mark.skip(reason="Not working.skip it")
def test_sub3():
    assert 1-1 != 0
