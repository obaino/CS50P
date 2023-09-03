# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    regex = r"src\=\"(http[s]?://(?:www.)?youtube.com/embed/.+?)\""
    if url_pattern := re.search(regex, s):
        long_url = url_pattern.group(1)
        # capture the string after the "embed/"
        short_url = re.search(r"embed/(.+)$", long_url).group(1)
        return f"https://youtu.be/{short_url}"

if __name__ == "__main__":
    main()