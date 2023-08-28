# https://cs50.harvard.edu/python/2022/psets/4/adieu/
# https://pypi.org/project/inflect/

import inflect

p = inflect.engine()

def main():
    print("Adieu, adieu, to " + p.join(get_names()))

def get_names():
    names_list = []
    while True:
        try:
            name = input("Name: ")
            names_list.append(name)
        except EOFError:
            print()
            break
    return names_list

if __name__ == "__main__":
    main()