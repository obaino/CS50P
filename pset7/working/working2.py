# https://cs50.harvard.edu/python/2022/psets/7/working/
# another way which converts time from 12h to 24h format
# it has integrated standard function to convert function

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
            if time.group(2) == None:
                new_time = f"{time.group(1)}:00 {time.group(3)}"
            else:
                new_time = f"{time.group(1)}:{time.group(2)} {time.group(3)}"
            hours = int(new_time.split(":")[0])
            minutes = new_time.split(":")[1]
            if minutes[-2:] == "PM":
                hours += 12
                output_time = f"{hours}:{minutes[:-3]}"
            elif hours == 12:
                output_time = f"00:{minutes[:-3]}"
            else:
                output_time = f"{hours:02}:{minutes[:-3]}"

            return output_time
        else:
            raise ValueError
    except ValueError:
        exit()

if __name__ == "__main__":
    main()