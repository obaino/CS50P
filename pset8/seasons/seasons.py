# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import inflect, sys
from datetime import date


def main():
    p = inflect.engine()
    output = p.number_to_words(get_dob(), andword="")
    print(f"{output} minutes")


def get_dob():
    try:
        today = date.today()
        # create a list of integers from the "-" splitted date
        # and instanciate a date object from user's birthday
        bd = list(map(int, input("Date of birth: ").split("-")))
        dob = date(bd[0], bd[1], bd[2])
        # get timedifference between dates and return the tolal
        # in seconds, then minutes
        timedelta = today - dob
        return round(timedelta.total_seconds() / 60)
    except ValueError:
        exit("Invalid Date")


if __name__ == "__main__":
    main()
