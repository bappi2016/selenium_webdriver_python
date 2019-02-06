import unittest
from unittestpackage.assert_demo import AssertDemo
from unittestpackage.testcasedemo import UnitTestDemo

# get all tests from AssertDemo and UnitTestDemo
tc1 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo)

# Create a test suite combining AssertDemo and UnitTestDemo
fuck_test = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(fuck_test)