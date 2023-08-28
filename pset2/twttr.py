
def main():
    text = input("Input: ")
    print("Output: ", end="")
    no_vowels(text)

def no_vowels(text):
    for c in text:
        vowels = ["a", "e", "i", "o", "u"]
        if c.lower() not in vowels:
            print(c, end="")
    print()

main()