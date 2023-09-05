import pytest
from um import count


# Test cases for the count function
def test_count_no_matches():
    assert count("This is a test sentence.") == 0


def test_count_single_match():
    assert count("The word um is in this sentence.") == 1


def test_count_multiple_matches():
    assert count("Um um um, multiple um's in this sentence.") == 4


def test_count_case_insensitive():
    assert count("UM is not the same as um.") == 2


def test_count_word_boundaries():
    assert count("Umbrella is not the same as a drum.") == 0
