import pytest
from fuel import convert, gauge

def test_no_fraction():
    with pytest.raises(ValueError):
        convert("682")

    with pytest.raises(ValueError):
        convert("cat")


def test_not_int():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_greater_than_one():
    with pytest.raises(ValueError):
        convert("5/4")

def test_negative():
     with pytest.raises(ValueError):
         convert("-1/2")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_value():
    assert convert("3/4") == 75.0



def test_end():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_ans():
    assert gauge(75.0) == "75.0%"

