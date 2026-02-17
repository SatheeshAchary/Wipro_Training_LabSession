"""
What Are Assertions?

An assertion is a statement that verifies whether a condition is True or False.

If the condition is:

✅ True → Test PASSES

❌ False → Test FAILS

In simple words:

Assertion checks whether expected result equals actual result.
"""

def test_add():
    assert 2 + 2 == 4


def test_string():
    name = "ramesh"
    assert name.upper() == "RAMESH"

def test_even():
    number = 6
    assert number % 2 == 0

import requests

def test_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
