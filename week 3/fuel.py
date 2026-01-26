# main loop which will prompt for a required fraction
while True:
    i = input("Fraction: ")

# if user doesnt input a fraction in the form of /
    if "/" not in i:
        continue

# splitting the input before and after /
    n, d = i.split("/")

    try: # trying if the values can be converted into integers
        N = int(n)
        D = int(d)
        if N > D: # not accepting values like 5/4
            pass
        else:
            value = round(N / D * 100, 2)

            if value < 0: # we dont want -ve fractions
                continue

            elif value <= 1:
                print("E")

            elif value >= 99:
                print("F")

            else:
                print(f"{round((N/D)*100)}%")

            break
        
    except (ValueError, ZeroDivisionError):
        pass









