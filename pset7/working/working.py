# https://cs50.harvard.edu/python/2022/psets/7/working/

import re, sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = r"^(?P<hr_1>0?[1-9]|1[0-2])(?::(?P<min_1>[0-5][0-9]))? (?P<ap_1>AM|PM) to (?P<hr_2>0?[1-9]|1[0-2])(?::(?P<min_2>[0-5][0-9]))? (?P<ap_2>AM|PM)$"
    if time := re.search(regex, s, flags=re.IGNORECASE):
        hr_1, min_1, ap_1, hr_2, min_2, ap_2 = time.groups()
        print(hr_1, min_1, ap_1, hr_2, min_2, ap_2)

        # if time.group(2) == None:
        #     new_time = f"{time.group(1)}:00 {time.group(3)}"
        # else:
        #     new_time = f"{time.group(1)}:{time.group(2)} {time.group(3)}"
        # hours = int(new_time.split(":")[0])
        # minutes = new_time.split(":")[1]
        # if minutes[-2:] == "PM":
        #     hours += 12
        #     output_time = f"{hours}:{minutes[:-3]}"
        # elif hours == 12:
        #     output_time = f"00:{minutes[:-3]}"
        # else:
        #     output_time = f"{hours:02}:{minutes[:-3]}"

        # return output_time
    else:
        raise ValueError
    
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