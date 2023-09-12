import pytest
from seasons import get_dob, find_minutes

def test_birthday():
    assert get_dob("1972-02-27") == "1972-02-27"