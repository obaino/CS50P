
import pytest
from working import convert, standard

def test_time_input():
    with pytest.raises(ValueError):
        convert("9:00 PM - 8:00 AM")
        convert("8 AM to 12:61 PM")

def test_time_output():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

