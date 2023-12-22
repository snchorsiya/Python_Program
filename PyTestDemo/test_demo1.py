# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# run in command >> py.test >> py.test -v >> py.test -v -s >> py.test test_demo2.py -v -s >> py.test -k CreditCard -v -s
# Method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
# you can run specific file with py.test <filename>

def test_firstProgram():
    print("Hello")


def test_secondGreetCreditCard():
    print("Hello Python")
    a = 5
    b = 10
    c = a + b
    print(c)
    assert c == 15, "Test pass."