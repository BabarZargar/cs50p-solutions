import random


def main():
    score = 0
    l = get_level()

    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        attempt = 0
        while attempt < 3:
            try:
                ans = int(input(f"{x} + {y} = "))

            except ValueError:
                print("EEE")
                attempt += 1
                continue

            if ans == x + y:
                score += 1
                break

            else:
                print("EEE")
                attempt += 1
                continue

        if attempt == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l in (1, 2, 3):
                return(l)
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)




if __name__ == "__main__":
    main()
