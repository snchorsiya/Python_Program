# Any pytest file should start with test_ or end with _test pytest method names should start with test Any code
# should be wrapped in method only run in command >> py.test >> py.test -v >> py.test -v -s >> py.test test_demo2.py
# -v -s >> py.test -k CreditCard -v -s Method name should have sense -k stands for method names execution,
# -s logs in out put -v stands for more info metadata you can run specific file with py.test <filename> You can mark
# (tag) tests @pytest.mark.smoke and then run with -m You can skip test with @pytest.mark.skip @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test case- conftest file to generalize fixture and make it
# available to all test case
# data driven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
# pytest -v -s --html=report.html generated html report

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


def test_secondGreetCreditCard():
    print("Hello Python")
    a = 5
    b = 10
    c = a + b
    print(c)
    assert c == 15, "Test pass."


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
