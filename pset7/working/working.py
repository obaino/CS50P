# https://cs50.harvard.edu/python/2022/psets/7/working/

import re, sys

def main():
    # print(convert(input("Hours: ")))
    times = ["10:00 AM", "4:00 PM", "1 PM", "11:00 PM"]
    for time in times:
        print(f"input time is: {time}, standard time is: {standard(time)}")


# def convert(s):
    

def standard(time):
    print(len(time.split(":")))
    if len(time.split(":")) > 1:
        return time.split(":")

if __name__ == "__main__":
    main()