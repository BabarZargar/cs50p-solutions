import pytest
from working import convert


def test_basic_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"


def test_no_minutes_start():
    assert convert("10 AM to 3:30 PM") == "10:00 to 15:30"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_same_period():
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_lowercase():
    with pytest.raises(ValueError):
        convert("9 am to 5 pm")

