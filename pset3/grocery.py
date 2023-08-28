# https://cs50.harvard.edu/python/2022/psets/3/grocery/

def main():
    grocery_list()


def grocery_list():
    items_dictionary = {}
    while True:
        try:
            item = input().upper()
            if item in items_dictionary:
                items_dictionary[item] += 1
            else:
                items_dictionary[item] = 1
        except EOFError:
            for key, value in sorted(items_dictionary.items()):
                print(value, key)
            break

if __name__ == "__main__":
    main()
