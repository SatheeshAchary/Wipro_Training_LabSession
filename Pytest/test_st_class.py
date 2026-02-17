# Class based is used to inside the class
# It is also same as the module type run at first and last of the program

class Testclass:

    def setup_class(cls):
        print("API Auth is open for username and password")

    def teardown_class(cls):
        print("API Auth is closed")

    def setup_method(method):
        print("Opening the Browser")

    def teardown_method(method):
        print("Closing the Browser")

    def test_addition(self):
        a = 5
        b = 3
        assert a + b == 8

    def test_subtraction(self):
        x = 10
        y = 4
        assert x - y == 6

    def test_string(self):
        name = "Ramesh"
        assert name.upper() == "RAMESH"

a = Testclass()
