import csv
from tabulate import tabulate
import sys

if len(sys.argv) == 1:
    print("Too few command line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command line arguments")
    sys.exit(1)

else:
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)

    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
