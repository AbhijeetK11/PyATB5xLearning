import pytest
import allure
import requests

@allure.title("Verify the Get request for Restful Booker")
@allure.description("This is the test case Booking id 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
   URL = "https://restful-booker.herokuapp.com/booking/1"
   response_data = requests.get(url=URL)
   print("response_data.text")
   assert response_data.status_code == 200

@allure.title("Verify the Get request for Restful Booker")
@allure.description("This is the test case Booking id -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative():
   URL = "https://restful-booker.herokuapp.com/booking/1"
   response_data = requests.get(url=URL)
   print("response_data.text")
   assert response_data.status_code == 404
