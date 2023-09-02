# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re, sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"https?://youtube.com/embed"
    result = re.search(regex, s)
    if result:
        return f"located. starts at {result.start()} ends at {result.end()}"
    else:
        return f"Cannot spot it"


...


if __name__ == "__main__":
    main()