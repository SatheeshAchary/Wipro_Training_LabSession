# Skipping --- if any testcase has a deffect then we can skip the that particular test case
# skip -- if the testcase are absolute
# Windows -- mobile - OS dependency

import pytest

def test_case1():
    print("TestCase1 is executed!")

@pytest.mark.skip
def testcase2():
    print("TestCase2 is executed!")

def test_Case3():
    print("TestCase3 is executed!")

