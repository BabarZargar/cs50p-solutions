import sys


if len(sys.argv) == 1:
    print("Too few command line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command line arguments")
    sys.exit(1)

else:
    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        with open(filename) as file:
            n = 0
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                n += 1

            print(n)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)





