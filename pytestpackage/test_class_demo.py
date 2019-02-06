import pytest


# first import the class which we will gonna test
from pytestpackage.class_to_test import SomeClassToTest
@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_method_A(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 20
        print("Running method A")
    def test_method_B(self):
        print("Running method B")