# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

def main():
    l = get_level()
    score = 0
    for _ in range(10):
        a = get_integer(l)
        b = get_integer(l)
        counter = 1
        while counter < 4:
            try:
                result = int(input(f"{a} + {b} = "))
                if result != a + b:
                    raise ValueError
                else:
                    score += 1
                    break
            except ValueError:
                counter += 1
                print("EEE")
                if counter == 4:
                    print(f"{a} + {b} = {a + b}")
                pass
    print("Score:", score)


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l in range(1, 4):
                return l
        except ValueError:
            pass

def get_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()