import time

from selenium import webdriver
import allure
import pytest

@allure.title("open the ap.vmo.com")
@pytest.mark.regression
def test_vmo_login(wedriver=None):
    driver = wedriver
    driver.get("https://app.vmo.com")
    time.sleep()