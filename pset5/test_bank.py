# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value

def test_hello():
    assert value("hello") or value ("HELLO") == 0

def test_h():
    assert value("how") == 20

def test_neither():
    assert value("what") == 100

def test_spaces():
    assert value("how are you") == 20