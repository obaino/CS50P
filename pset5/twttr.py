# rewritten for the test_twttr.py

def main():
    text = input("Input: ")
    print("Output: ", end="")
    print(shorten(text))

def shorten(word):
    shortened_text = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            shortened_text += c
    return shortened_text

if __name__ == "__main__":
    main()