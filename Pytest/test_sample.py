# test_sample.py
def setup_function(func):
    print("Opening the Browser")

def teardown_function(func):
    print("Closing the Browser")


def test_addition():
    a = 5
    b = 3
    assert a + b == 8


def test_subtraction():
    x = 10
    y = 4
    assert x - y == 6


def test_string():
    name = "Ramesh"
    assert name.upper() == "RAMESH"
