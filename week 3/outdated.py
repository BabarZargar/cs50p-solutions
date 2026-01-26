l = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
        elif "," in date:
            month, dayyear = date.split(" ", 1)
            d, y = dayyear.split(", ")
            m = l.index(month) + 1
            d = int(d)
            y = int(y)

        else:
            continue

        if not (1 <= m <= 12 and 1 <= d <= 31):
            continue

        break

    except(ValueError, IndexError):
        pass

print(f"{y:04}-{m:02}-{d:02}")









