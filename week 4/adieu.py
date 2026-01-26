import inflect

p = inflect.engine()
names = []
while True:
    try:
        name = input("Name: ")
        names.append(name) #This will stop rewriting the list and actually put names in it

    except EOFError:
            print("")
            print(f"Adieu, adieu, to {p.join(names)}") #p.join doesnt work like print so I have to use f"" in order to print the message and then handle the list of names
            break


