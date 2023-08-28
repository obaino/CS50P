def main():
    text = input("Enter your text: ")
    convert(text)

def convert(a):
    a = a.replace(":)", "🙂").replace(":(", "🙁")
    print(a)

main()