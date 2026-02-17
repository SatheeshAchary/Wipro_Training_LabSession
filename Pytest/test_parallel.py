import pytest
from test_Fixtures import api_url

def testCase1():
    print("Test Case 1 is passed!")

def testCase2():
    print("Test Case 1 is passed!")

def testCase3():
    print("Test Case 1 is passed!")

def testCase4():
    print("Test Case 1 is passed!")

def testLogin():
    print("Login test case is passed")

def test_api(api_url):
    assert "https" in api_url