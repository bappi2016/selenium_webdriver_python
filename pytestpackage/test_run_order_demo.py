import pytest

@pytest.mark.order6
def test_run_order_method_A(oneTimeSetUp, setUp):
    print("Running Method A")
@pytest.mark.order5
def test_run_order_method_B(oneTimeSetUp, setUp):
    print("Running Method B")
@pytest.mark.order4
def test_run_order_method_C(oneTimeSetUp, setUp):
    print("Running Method C")
@pytest.mark.order3
def test_run_order_method_D(oneTimeSetUp, setUp):
    print("Running Method D")
@pytest.mark.order2
def test_run_order_method_E(oneTimeSetUp, setUp):
    print("Running Method E")

@pytest.mark.order1
def test_run_order_method_F(oneTimeSetUp, setUp):
    print("Running Method F")