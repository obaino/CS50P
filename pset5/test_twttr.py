# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten

def test_vowels():
    assert shorten("aeroplane") == "rpln"

def test_capital_vowels():
    assert shorten("BOLLOCKS") == "BLLCKS"

def test_numbers():
    assert shorten("aero123flot") == "r123flt"

def test_puntuation():
    assert shorten("b()()bies") == "b()()bs"