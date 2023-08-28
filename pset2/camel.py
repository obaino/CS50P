
name = input("camelCase: ")
print("snake_case:", end="")
for c in name:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.swapcase(), end="")
print()
