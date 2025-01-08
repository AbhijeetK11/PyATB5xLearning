import pytest
import allure

@allure.title("Verify that the create booking, with invalid data is working")
@allure.description("Positive test case for create booking check")
@pytest.mark.positive
def test_create_booking_negative_1():
    print("This is the test case Number four")
    assert 1 + 2 == 3

@allure.title("Verify that the create booking, with invalid data is working")
@allure.description("negative test case for create booking check")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("This is the test case Number Five")
    assert 3 * 2 == 7

