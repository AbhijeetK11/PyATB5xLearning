import pytest

@pytest.fixture()
def crete_token():
    return "abc"


def crete_booking_id():
    assert crete_booking_id()
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

def test_put(crete_token, create_booking_id):
    print(crete_token)
    print(create_booking_id)

def test_put2(crete_token, create_booking_id, read_excel_file):
    print(crete_token)
    print(create_booking_id)
    print(read_excel_file)




