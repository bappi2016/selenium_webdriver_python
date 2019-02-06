import pytest
@pytest.yield_fixture()# yield_fixture will run the method twice as setup and teardown
def setUp():
    print("Running Method Level setUp")
    yield
    print("Running Method Level teardown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser):#This fixture gets the browser value from another fixture
    # which is reading the command line option.
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running Tests of FF")
    else:
        print("Running Tests on chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")