def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print("$", amount, sep = "")


def value(greeting):
    new_greeting = normalize(greeting)
    if new_greeting.startswith("hello"):
        return(0)
    elif new_greeting.startswith("h"):
        return(20)
    else:
        return(100)

def normalize(n):
    return(n).lstrip().lower()


if __name__ == "__main__":
    main()
