# https://cs50.harvard.edu/python/2022/psets/3/outdated/


def main():
    y, m, d = date()
    print(f"{y}-{m:02}-{d:02}")

def date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                month_day, year = date.split(", ")
                month, day = month_day.split(" ")
                month = months.index(month.capitalize()) + 1
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                return int(year), int(month), int(day)
        except (ValueError, NameError, KeyError):
            pass

if __name__ == "__main__":
    main()