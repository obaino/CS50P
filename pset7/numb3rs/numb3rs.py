# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re, sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    regex = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(regex, ip)
    if match:
        for n in match.groups():
            # print(n)
            if int(n) <= 255:
                continue
            else:
                return False
        return True 
    else:
        return False

if __name__ == "__main__":
    main()