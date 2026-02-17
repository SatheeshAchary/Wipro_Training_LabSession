from email.policy import strict
# #xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)

import pytest
from jinja2 import TemplateRuntimeError


@pytest.mark.xfail
def test_division():
    assert 10 / 0 == 5

@pytest.mark.xfail(reason="Bug #123 not fixed yet")
def test_login_with_invalid_password():
    assert False

@pytest.mark.xfail
def test_add():
    assert 2 + 2 == 4

"""
@pytest.mark.xfail(strict=True)
def test_add():
    assert 2 + 2 == 4
"""