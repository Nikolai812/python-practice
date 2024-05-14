import pytest

# Fixture without yield
@pytest.fixture
def setup_fixture_without_yield():
    print("Setup code (without yield)")
    return "fixture_value"

def test_function_without_yield(setup_fixture_without_yield):
    print("Test function (without yield)")
    assert setup_fixture_without_yield == "fixture_value"

# Fixture with yield
@pytest.fixture
def setup_fixture_with_yield():
    print("Setup code (with yield)")
    yield "fixture_value"
    print("Teardown code (with yield)")

def test_function_with_yield(setup_fixture_with_yield):
    print("Test function (with yield)")
    assert setup_fixture_with_yield == "fixture_value"