# https://cs50.harvard.edu/python/2022/psets/6/scourgify/

from sys import argv, exit
import csv

def main():
   create_file(get_arguments())

def get_arguments():
    try:
        if len(argv) < 3:
            exit("Too few command-line arguments")
        elif len(argv) > 3:
            exit("Too many command-line arguments")
        else:
            return argv
    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")

def create_file(argv):
    with open(argv[1], "r") as file:
        reader = csv.DictReader(file)
        full_name, house = reader.fieldnames
        # print(f"the headers of {argv[1]} are {full_name} and {house}")
        with open(argv[2], "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                writer.writerow({"last": row[full_name].split(",")[0], "first": row[full_name].split(",")[1].lstrip(), "house": row[house]})
                # print(row)
                # keys = list(row.keys())
                # first_key = list(row.keys())[0]
                first_value, last_value = row[full_name].split(",")
                # second_key = list(row.keys())[1]
                # house_value = row[house]
                # print(f"keys are: {keys}")
                # print(f"first_key is: {full_name}, first_value is: {first_value}, last_value is: {last_value}")
                # print(f"second_key is: {house}, house_value is: {house_value}")

if __name__ == "__main__":
    main()