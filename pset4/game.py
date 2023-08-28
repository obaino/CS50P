# https://cs50.harvard.edu/python/2022/psets/4/game/

from random import randint

def main():
    l = get_level()
    print("level is:", l)
    n = randint(1, l)
    print("number is:", n)
    g = get_guess()
    print("guess is:", g)

    while g != n:
        if g < n:
            print("Too small!")
        elif g > n:
            print("Too large!")
        g = get_guess()
    print("Just right!")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()
