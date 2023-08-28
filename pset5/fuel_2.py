# https://cs50.harvard.edu/python/2022/psets/3/fuel/
# rewritten for test_fuel.py

def main():
    while True:
        try:
            text = input("Fraction: ")
            x = int(text.split(sep="/")[0])
            y = int(text.split(sep="/")[1])
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            else:
                outcome = x / y
                break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(convert(outcome)))

def convert(fraction):
    return round(fraction * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()