import csv
import sys

if len(sys.argv) < 3:
    print("Too few command line arguments")
    sys.exit(1)

elif len(sys.argv) > 3:
    print("Too many command line arguments")
    sys.exit(1)

else:
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    if not (inputfile.endswith(".csv") and outputfile.endswith(".csv")):
        print("Not a csv file")
        sys.exit(1)

    try:
        with open(inputfile) as infile, open(outputfile, "w") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()



            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({
                "first": first,
                "last": last,
                "house": row["house"]
            })

    except FileNotFoundError:
        sys.exit(1)


