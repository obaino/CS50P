
import pytest
from working import convert

def test_time_input():
    with pytest.raises(ValueError):
        convert("17 AM")
        convert("12:61 PM")

def test_time_output():
    assert convert("10:30 PM") == "22:30"
    assert convert("10 PM") == "22:00"
    assert convert("12:19 AM") == "00:19"

