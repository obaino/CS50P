import pytest
from jar import Jar

def test_init():
    jar = Jar(12, 0)
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(8)

def test_withdraw():
    jar = Jar(12, 12)
    jar.withdraw(7)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(8)