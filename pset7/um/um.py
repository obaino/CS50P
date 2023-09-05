# https://cs50.harvard.edu/python/2022/psets/7/um/

import re

def main():
    print(count(input("Text: ")))

    # # test phrases
    # test_phrases = [
    #     "hello, um, everybody",
    #     "trumpet",
    #     "the, um, tin drum",
    #     "little drummer boy",
    #     "UM, may I have your, um, attention plesase",
    #     "um?",
    #     "Um, thanks for the album.",
    #     "Um, thanks, um...",
    # ]
    # # test the phrases
    # for test_phrase in test_phrases:
    #     print(test_phrase)
    #     print(count(test_phrase))
    #     print("---" * 14)



def count(s):
    return len(re.findall(r"\bum\b", s, flags=re.IGNORECASE))

if __name__ == "__main__":
    main()