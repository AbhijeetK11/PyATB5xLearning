from http.client import responses
from typing import assert_type

import allure
import pytest
import requests

#pip install allure requests

#To make a request

@allure.title("TC#1 -Create booking ID crud positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud

def test_create_booking_positive_tc1():
    base_url= "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
     #base_path_put = "/booking/1"

    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    responses_data = requests.post(url=full_url,headers=headers, json=payload)

    ##status code verification

    assert responses_data.status_code ==200
    ##Booking id>0, firstname=jim

    response_data_json = responses_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_data_json["bookingid"] ["firstname"]
    assert firstname == "jim"
    assert type(firstname) == str

    lastname = response_data_json["bookingid"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = responses_data.elapsed.total_seconds()
    assert time < 3

@allure.title("TC2 -Create booking crud Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url + base_path
        headers = {"Content-Type": "application/json"}
        json_payload = {}

        response = requests.post(url=URL, headers=headers, json=json_payload)
        assert response.status_code == 500
        assert response.text == "Internal Server Error"
