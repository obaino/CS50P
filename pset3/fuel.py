# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def main():
    outcome = round(fraction() * 100)
    if outcome <= 1:
        print("E")
    elif outcome >= 99:
        print("F")
    else:
        print(f"{outcome}%")

def fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator = int(fraction.split(sep="/")[0])
            denominator = int(fraction.split(sep="/")[1])
            # if numerator > denominator:
            #     raise ValueError
            if numerator <= denominator:
                return numerator / denominator
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()