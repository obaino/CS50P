# https://cs50.harvard.edu/python/2022/psets/7/working/

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"^(?P<hours1>0?[1-9]|1[0-2])(?::(?P<minutes1>[0-5][0-9]))? (?P<ap_1>AM|PM) to (?P<hours2>0?[1-9]|1[0-2])(?::(?P<minutes2>[0-5][0-9]))? (?P<ap_2>AM|PM)$"
    if time := re.search(regex, s, flags=re.IGNORECASE):
        hours1, minutes1, ap_1, hours2, minutes2, ap_2 = time.groups()
        return f"{standard_time(hours1, minutes1, ap_1)} to {standard_time(hours2, minutes2, ap_2)}"
    else:
        raise ValueError


def standard_time(hours, minutes, ap):
    if minutes == None:
        minutes = "00"
    if ap == "PM":
        if hours == "12":
            hours == "12"
        else:
            hours = int(hours) + 12
    else:
        if hours == "12":
            hours = "00"
        else:
            hours = int(hours)
    return f"{hours:02}:{minutes}"


if __name__ == "__main__":
    main()
