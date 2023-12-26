import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "This is a failed test case"


@pytest.mark.xfail
def test_secondCreditCard():
    print("Welcome to pytest.")

