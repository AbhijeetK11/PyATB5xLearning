import pytest

@pytest.fixture()
def crete_token():
    return "abc"


def crete_booking_id():
    assert crete_booking_id()
    return 1

def test_update_req_1(crete_token, create_booking_id):
    print("Token >", crete_token)
    print("booking ID >", create_booking_id)