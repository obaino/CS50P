# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import inflect, sys
from datetime import date


def main():
    today = date.today()
    birthday = input("Date of birth: ")
    print(get_minutes(birthday, today))


def get_minutes(birthday, now):
    p = inflect.engine()
    try:
        bd = list(map(int, birthday.split("-")))
        date_of_birth = date(bd[0], bd[1], bd[2])
        timedelta = now - date_of_birth
        output = p.number_to_words(
            round(timedelta.total_seconds() / 60), andword=""
        ).capitalize()
        return f"{output} minutes"
    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
