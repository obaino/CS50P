def main():
    x, y, z = input("Exrpession: ").split(' ')
    print(float(outcome(x, y, z)))

def outcome(a,b,c):
    a, c = int(a), int(c)
    match b:
        case "+":
            return a + c
        case "-":
            return a - c
        case "*":
            return a * c
        case "/":
            return a / c

main()