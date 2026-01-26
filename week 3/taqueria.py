def main():
    d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    i = 0 #i = 0 before the loop begins so it doesnt keep resetting

    while True:

        try:
            snack = input("Item: ")
            snacknew = snack.title()

            if snacknew in d:

                i = i + d[snacknew]
                print("Total: $",f"{i:.2f}", sep = "")

            else:
                continue



        except EOFError: #to handle ctrl d
            print("") #skips to the next line
            break


main()
