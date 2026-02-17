# Grouping can be divided into two types
# Sanity grouping -- to check the quality of the code written
# Sanity testing checks whether a small part of application works after minor changes.
"""
After small bug fix

After small code change

Before doing full testing

Regression testing ---
Regression testing checks whether new changes broke old functionality.
Example:

Developer adds new payment method.

Regression testing checks:

Login works?

Add to cart works?

Payment works?

Logout works?
"""

import pytest

import pytest

@pytest.mark.sanity
def test_login():
    assert True

@pytest.mark.regression
def test_add_to_cart():
    assert True

@pytest.mark.regression
def test_payment():
    assert True
