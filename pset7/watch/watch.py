# https://cs50.harvard.edu/python/2022/psets/7/watch/
# input url:
# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

import re, sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"src\=\"(http[s]?://www.youtube.com/embed/.+?)\""
    url_pattern = re.search(regex, s)
    if url_pattern:
        return url_pattern.group(1)
    else:
        return f"Cannot spot it"



if __name__ == "__main__":
    main()