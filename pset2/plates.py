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

# check if the first letters are alpha
def two_letters(text):
    return text[:2].isalpha()

# check the length of the string
def text_length(text):
    return 2 <= len(text) <= 6

# Check if the characters following a digit to the end of the string, are digits
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

# check if there is punctuation in text
def punctuation_check(text):
        return not any(c in "'.,;:?! " for c in text)
        # for c in "'.,;:?! ":
        #     if c in text:
        #         return False
        # else:
        #     return True

if __name__=="__main__":
    main()

# test = ["CS50", "ECTO88", "NRVOUS",  "CS05", "CS50P2", "PI3.14", "H", "OUTATIME", "CS50P", "HELLO"]

# for test_case in test:
#     print("Considering", test_case)
#     if is_valid(test_case):
#         print("The outcome of", test_case, "is Valid")
#         print("----")
#     else:
#         print("The outcome of", test_case, "is Invalid")
#         print("----")