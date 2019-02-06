import pytest

@pytest.fixture() # fixture() define the preparation needed to run a test
def setUp(): # setup shows note before a test begin
    print("Run Once before every method to know the test start here")
def test_methodA(setUp): # told method a its under setup block which means
    #setUp() will run before these two methods run every time, here setup is act like a guard
    print("Running Method A")

def test_methodB(setUp):
    print("Running Method B")