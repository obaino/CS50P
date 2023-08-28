# https://cs50.harvard.edu/python/2022/psets/6/lines/

from sys import argv, exit

def main():
    print(count_lines(get_arg()))

def get_arg():
    try:
        if len(argv) < 2:
            exit("Too few command-line arguments")
        elif len(argv) > 2:
            exit("Too many command-line arguments")
        else:
            with open(argv[1], "r") as file:
                if not argv[1][-3:] == ".py":
                    exit("Not a Python file")
                else:
                    lines = file.readlines()
                    return lines
    except FileNotFoundError:
        exit("File does not exist")

def count_lines(lines):
    counter = 0
    for line in lines:
        if not line.lstrip().startswith("#") and line.lstrip():
            counter += 1
    return counter

if __name__ == "__main__":
    main()