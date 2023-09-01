
from numb3rs import validate

def test_strings():
    assert validate("cat") == False

def test_digits():
    assert validate("1.2.2") == False
    assert validate("2342.12.0.1") == False
    assert validate("123.123.124.123.123") == False

def test_over255():
    assert validate("1000.2.3.4") == False
    assert validate("127.0.425.8") == False
    assert validate("255.255.155.255") == True