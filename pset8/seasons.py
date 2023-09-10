# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import re, inflect
from datetime import datetime, date


def main():
    p = inflect.engine()
    output = p.number_to_words(time_difference(get_birthday()), andword="")
    print(f"{output} minutes")


def get_birthday():
    regex = r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b"
    user_bd = input("Date of birth: ")
    if match := re.match(regex, user_bd):
        year, month, day = map(int, match.groups())
        birthday = datetime(year, month, day)
    else:
        exit("Invalid Date")
    return birthday


def time_difference(birthday):
    today = datetime.combine(date.today(), datetime.min.time())
    timedelta = today - birthday
    return round(timedelta.total_seconds() / 60)


if __name__ == "__main__":
    main()
