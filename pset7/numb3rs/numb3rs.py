# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re, sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # regex = "([0-9]{3})\.([0-9]{3})\.([0-9]{3})\.([0-9]{3})"
    regex = "\d{1-3}\.\d{1-3}\.\d{1-3}\.\d{1-3}"
    result = re.match(regex, ip)
    return result


if __name__ == "__main__":
    main()