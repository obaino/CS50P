# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import inflect, sys
from datetime import date


def main():
    p = inflect.engine()
    output = p.number_to_words(find_minutes(get_dob()), andword="")
    print(f"{output} minutes")


def get_dob():
    # create a list of integers from the "-" splitted date
    dob = list(map(int, input("Date of birth: ").split("-")))
    if not dob:
        raise ValueError
        exit("bye")
    else:
        # return an instanciated date object
        return date(dob[0], dob[1], dob[2])


def find_minutes(birthday):
    today = date.today()
    timedelta = today - birthday
    return round(timedelta.total_seconds() / 60)


if __name__ == "__main__":
    main()
