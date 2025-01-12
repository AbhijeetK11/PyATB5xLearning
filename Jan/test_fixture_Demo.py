from types import new_class

import pytest

@pytest.fixture()
def is_marries_before_run():
    return True


def test_update(is_marries_before_run):
    assert is_marries_before_run == False