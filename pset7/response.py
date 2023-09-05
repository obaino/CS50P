# https://cs50.harvard.edu/python/2022/psets/7/response/

import validators


def main():
    email = input("What's your email address? ")
    print(validate(email))


def validate(text):
    if validators.email(text):
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
