# https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from plates import is_valid

def test_text_length():
    assert is_valid("OUTATIME") == False

def test_first_two_letters():
    assert is_valid("11") == False
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("AA") == True

def test_letter_among_digits():
    assert is_valid("CS50P2") == False

def test_zero_first_digit():
    assert is_valid("CS05") == False

def test_all_letters():
    assert is_valid("HELLO") == True

def test_no_panctuation():
    assert is_valid("PI3.14") == False