# https://cs50.harvard.edu/python/2022/psets/7/working/

import re, sys

def main():
    print(standard(input("Hours: ")))
    # print(convert(input("Hours: ")))

    # test standard function
    # times = ["2:00 AM", "8 AM", "9:00 AM", "10:00 AM", "4:00 PM", "1 PM", "10 PM", "11:00 PM"]
    # for time in times:
    #     print(f"input time is: {time}, standard time is: {standard(time)}")
    #     print("----" * 12)


# def convert(s):
    

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