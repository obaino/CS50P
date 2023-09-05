# https://cs50.harvard.edu/python/2022/psets/7/working/
# Converts time from 12h to 24h format using a dedicated
# standard function

import re, sys


def main():
    try:
        hour1, hour2 = input(("Hours: ")).split(" to ")
        print(f"{convert(hour1)} to {convert(hour2)}")
    except ValueError:
        exit()


def convert(s):
    regex = r"^(0?[1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    try:
        if time := re.search(regex, s):
            if time.group(2) == None:  # time format is: hh AM/PM
                new_time = f"{time.group(1)}:00 {time.group(3)}"
            else:  # time format is: hh:mm AM/PM
                new_time = f"{time.group(1)}:{time.group(2)} {time.group(3)}"
            return standard(new_time)
        else:
            raise ValueError
    except ValueError:
        exit()


def standard(time):
    output_time = ""
    if len(time.split(":")) > 1:
        hours = int(time.split(":")[0])
        minutes = time.split(":")[1]
        if minutes[-2:] == "PM":
            hours += 12
            output_time = f"{hours}:{minutes[:-3]}"
        else:
            output_time = f"{hours:02}:{minutes[:-3]}"
    else:
        hours = int(time.split(" ")[0])
        if time[-2:] == "PM":
            hours += 12
            output_time = f"{hours}:00"
        else:
            output_time = f"{hours:02}:00"
    return output_time


if __name__ == "__main__":
    main()
