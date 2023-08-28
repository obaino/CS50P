# https://cs50.harvard.edu/python/2022/psets/6/pizza/

from sys import argv, exit
from tabulate import tabulate
import csv

def main():
    print(tabulate(get_menu(), headers="keys", tablefmt="grid"))

def get_menu():
    try:
        if len(argv) < 2:
            exit("Too few command-line arguments")
        elif len(argv) > 2:
            exit("Too many command-line arguments")
        else:
            with open(argv[1], "r") as file:
                if not argv[1].endswith(".csv"):
                    exit("Not a CSV file")
                else:
                    menu = []
                    reader = csv.DictReader(file)
                    # get the first row of csv as keys
                    key_1, key_2, key_3 = reader.fieldnames
                    for row in reader:
                        menu.append({key_1: row[key_1], key_2: row[key_2], key_3: row[key_3]})
                    return menu

    except FileNotFoundError:
        exit("File does not exist")

if __name__ == "__main__":
    main()