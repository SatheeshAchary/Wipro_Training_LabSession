"""
What is Parametrization in Pytest?

Parametrization means:

Running the same test function multiple times with different inputs.

Instead of writing multiple test functions ❌
We write one test function and pass multiple data sets
"""

import pytest

@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (2, 3, 5),
    (4, 5, 9)
])
def test_add(a, b, result):
    assert a + b == result


@pytest.mark.parametrize("number", [2, 4, 6, 8])
def test_even_number(number):
    assert number % 2 == 0


@pytest.mark.parametrize("payload", [
    {"name": "Satheesh", "age": 22},
    {"name": "Dhanush", "age": 18}
])

def checkAge(payload):
    assert payload["age"] >= 18
