def main():
     value = convert()
     ans = gauge(value)
     print(ans)




def convert():
    while True:
        fraction = input("Fraction: ")


        if "/" not in fraction:
            continue


        n, d = fraction.split("/")

        try:
            N = int(n)
            D = int(d)
            if N > D:
                pass
            else:
                value = round(N / D * 100, 2)

                if value < 0:
                    continue

                else:
                    return value

        except (ValueError, ZeroDivisionError):
            pass


def gauge(value):
    if value <= 1:
            return "E"

    elif value >= 99:
            return "F"

    else:
            return(f"{value}%")


if __name__ == "__main__":
    main()
