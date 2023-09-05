# https://cs50.harvard.edu/python/2022/psets/7/um/

import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum\b", s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
