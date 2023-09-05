# rewritten for the test_plates.py
# https://cs50.harvard.edu/python/2022/psets/5/test_plates/


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        two_letters(s)
        and text_length(s)
        and check_digits_after_digit(s)
        and punctuation_check(s)
    )


def two_letters(text):
    return text[:2].isalpha()


def text_length(text):
    return 2 <= len(text) <= 6


def check_digits_after_digit(text):
    if text.isalpha():
        return True
    else:
        found_digit = False
        for c in text:
            if c.isdigit():
                found_digit = True
                idx = text.index(c)
                break

        if found_digit:
            if c == "0":
                return False
            if text[idx:].isdigit():
                return True
            else:
                return False


def punctuation_check(text):
    return not any (c in "'.,;:?! " for c in text)
    # for c in "'.,;:?! ":
    #     if c in text:
    #         return False
    # else:
    #     return True


if __name__ == "__main__":
    main()
