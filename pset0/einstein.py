def main():
    m = int(input("m: "))
    print("E:", energy(m))

def energy(mass):
    return mass * pow(300000000, 2)

main()