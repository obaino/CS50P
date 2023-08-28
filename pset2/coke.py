# this is the solution submitted

amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    while True:
        coins = int(input("Insert Coin: "))
        # if coins  == 25 or coins == 10 or coins == 5:
        if coins in [5, 10, 25]:
            break
        else:
            print("Amount Due:", amount_due)
    amount_due -= coins
print("Change Owed:", abs(amount_due))
