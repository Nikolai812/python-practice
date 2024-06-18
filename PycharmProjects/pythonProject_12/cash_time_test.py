#import pytest
import pytest


@pytest.fixture
def number_of_desks():
    print("aaaa")
    yield
    print("aaayie")

@pytest.fixture
def customer_time_data():
    print("bbbbbb")
    yield
    print("bbbyie")

def test_cash_time(number_of_desks, customer_time_data):
    print("something")
