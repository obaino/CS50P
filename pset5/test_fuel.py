# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

import pytest
from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_y_less_than_x():
    with pytest.raises(ValueError):
        convert("3/2")

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(5) == "5%"
    assert gauge(80) == "80%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"