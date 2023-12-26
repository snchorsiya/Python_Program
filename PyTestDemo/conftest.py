import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Shaatal", "Chorsiya", "QATest.com"]


@pytest.fixture(params=[("chrome", "Sheetal", "Chorsiya"), ("firefox", "qaTest"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
