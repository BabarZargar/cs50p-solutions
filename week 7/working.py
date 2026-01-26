import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$", s)

    if not matches:
        raise ValueError

    sh = int(matches.group(1))           #start hour
    sm = matches.group(2) or ":00"       #start minute or 0 min
    sap = matches.group(3)               #am or pm

    eh = int(matches.group(4))           #end hour
    em = matches.group(5) or ":00"       #end min or 0 min
    eap = matches.group(6)               #am or pm

    if sap == "AM" and sh == 12:
        sh = 0
    elif sap == "PM" and sh != 12:
        sh += 12

    if eap == "AM" and eh == 12:
        eh = 0
    elif eap == "PM" and eh != 12:
        eh += 12

    sm = sm[1:]
    em = em[1:]

    return f"{sh:02d}:{sm} to {eh:02d}:{em}"




if __name__ == "__main__":
    main()
