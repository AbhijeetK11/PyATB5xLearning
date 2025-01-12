from http.client import responses

import pytest
import requests
from dotenv import load_dotenv
import os

from Decm.ex_31122024_Pytest_Requests_Module.test_lab_Pytest_Learn3_POST_Token2 import headers


@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username, password)
    print("Creating Token......")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content Type:" "application/json"}
    json_payload = {

        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=url,headers=headers,json=json_payload)
    token = response_data.json()["token"]
    print(token)

@pytest.fixture()
def create_booking_id():
    print("Create Booking ID!!")
    URL = "https://restful-booker.herokuapp.com/booking"
    json_payload = {
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
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id



@pytest.fixture()
def read_excel_file():
    pass

@pytest.fixture()
def read_csv_file_data():
    pass

@pytest.fixture()
def read_mysql_file_database():
    pass