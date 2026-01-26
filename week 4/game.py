import random

#get valid level
while True:
    try:
        l = int(input("Level: "))
        if l > 0: #accounting for non postive level
            break
        else:
            continue

    except ValueError:
         pass

#generate randint once and dont put it in any loop
n = random.randint(1, l)

#get valid guess then compare with n
while True:
    try:
        g = int(input("Guess: "))
        if g > 0: #accounting for non positive guess
            pass
        else:
            continue

    except ValueError:
        continue

    else:
        if g < n:
            print("Too small!")

        elif g > n:
            print("Too large!")

        else:
            print("Just right!")
            break
