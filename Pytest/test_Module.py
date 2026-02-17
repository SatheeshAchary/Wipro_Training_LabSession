# Module level - run once per program (Run only when opening the file and closing the file) it will be printed at first and last

def setup_module(func):
    print("Open the DB Connection")

def teardown_module(func):
    print("Closing the DB Connection")

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
