import pytest
from seasons import get_minutes
from datetime import date, timedelta


def test_get_minutes():
    assert get_minutes(str(date.today()-timedelta(days=365)), date.today()) == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_minutes(str(date.today()-timedelta(days=730)), date.today()) == "One million, fifty-one thousand, two hundred minutes"

def test_System_Exit():
    # with pytest.raises(SystemExit):
    #     get_minutes("spam", date.today())
    with pytest.raises(SystemExit):
        get_minutes("2024-09-10", date.today())
    with pytest.raises(SystemExit):
        get_minutes("2023-13-10", date.today())
    with pytest.raises(SystemExit):
        get_minutes("2023-12-32", date.today())
    with pytest.raises(SystemExit):
        get_minutes("nikos-nk-kn", date.today())
    with pytest.raises(SystemExit):
        get_minutes(" 2022-13-12", date.today())