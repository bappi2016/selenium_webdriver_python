import  pytest

@pytest.yield_fixture()
def setUp():
    print("Run conftest demo 2 setup method")
    yield
    print("Run conftest demo 2 teardown method")

def test_method_A(setUp):
    print("Run conftest demo 2 mehtod A")
def test_method_B(setUp):
    print("Run conftest demo 2 mehtod B")
