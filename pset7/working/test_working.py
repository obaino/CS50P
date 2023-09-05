import pytest
from working import convert


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
        convert("12:20 AM - 3:30 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")
        convert("12:61 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")


def test_time_output():
    assert convert("12:20 AM to 3:30 PM") == "00:20 to 15:30"
    assert convert("12:05 PM to 8:30 PM") == "12:05 to 20:30"
    assert convert("3 AM to 4:23 PM") == "03:00 to 16:23"
    assert convert("12:13 AM to 4 PM") == "00:13 to 16:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
