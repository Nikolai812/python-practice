import pytest


@pytest.fixture()
def fxt_test_1():
    print("before 1")
    yield "f_t_1"
    print("after_1")


def test_dummy(fxt_test_1):
    print('running test_dummy')
    assert add(2, 3) == 5


@pytest.mark.parametrize("x, y, expected_value",
                         [(1, 2, 3),
                          (2, 4, 6)]
                         )
def test_dummy_param(x, y, expected_value, fxt_test_1):
    print
    assert add(x, y) == expected_value, "expected value"


# Test that is expected to fail because the feature is not implemented yet
@pytest.mark.xfail(reason="Feature not implemented")
def test_not_implemented_feature():
    assert False, "This feature is not yet implemented"


@pytest.mark.xfail(reason="Known bug in version 1.0", raises=ZeroDivisionError)
def test_known_bug():
    result = 1 / 0
    assert 1 + 1 == 2

#@pytest.Class()
def test_divide_by_zero():
    # Using pytest.raises to check for the ValueError exception
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # Optionally check the exception message
    assert str(excinfo.value) == "Cannot divide by zero"

# Function that raises an exception
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def add(x, y):
    return x + y
