x = 50
print("Amount Due:", x)

while x > 0:
    y = int(input("Insert coin: "))

    if y ==25:
        x -= y
        if x <= 0:
            print("Change owed:", -(x))
        else:
            print("Amount Due:", x)

    elif y == 10:
        x -= y
        if x <= 0:
            print("Change owed:", -(x))
        else:
            print("Amount Due:", x)
    elif y == 5:
        x -= y
        if x <= 0:
            print("Change owed:", -(x))
        else:
            print("Amount Due:", x)

    else:
        print("Amount Due:", x)

