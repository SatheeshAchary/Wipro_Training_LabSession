# 1.Write a test that is skipped because a feature is not implemented yet.
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_new_payment_feature():
    assert True

# 2. To run only in linux or macOS not in Windows (Skipping)
import sys

@pytest.mark.skipif(sys.platform.startswith("win"),
                    reason="Runs only on Linux")
def test_linux_only():
    assert True

# API Health Check (Dynamic Skip)

# If API status ≠ 200 → Skip dynamically
import requests

def test_api_health():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code != 200:
        pytest.skip("API is down, skipping test")

    assert response.status_code == 200

# Mark Failing Test as xfail (Bug #123)
@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 5 + 5 == 15

# 5.You have 5 parameterized cases.
# 2 are known bugs.
# Mark only those 2 cases as xfail without marking entire test.

@pytest.mark.parametrize("number, expected", [

    (2, True),
    (4, True),
    pytest.param(5, True, marks=pytest.mark.xfail(reason="Bug #101")),
    pytest.param(7, True, marks=pytest.mark.xfail(reason="Bug #102")),
    (8, True)
])
def test_even_number(number, expected):
    assert (number % 2 == 0) == expected
