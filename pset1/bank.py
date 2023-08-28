def main():
    greeting = input("Greeting: ")
    starts_with(greeting)

def starts_with(text):
    if text.strip().lower().startswith('hello'):
        print('$0')
    elif text.strip().lower().startswith('h'):
        print('$20')
    else:
        print('$100')

main()