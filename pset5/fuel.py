# https://cs50.harvard.edu/python/2022/psets/3/fuel/
# rewritten for pset 5 test_fuel.py
# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

def main():
    while True:
        try:
            text = input("Fraction: ")
            print(gauge(convert(text)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x = int(fraction.split(sep="/")[0])
    y = int(fraction.split(sep="/")[1])
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return round(x / y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()