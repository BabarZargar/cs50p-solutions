def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

# we want the tip upto two decimal places
    print(f"Leave ${tip:.2f}")

#clean the string and put it into another variable then convert new str into float
def dollars_to_float(d):

    dd = d.replace("$", "")
    return float(dd)

#clean the string with another variable, convert str to float then return float/100
def percent_to_float(p):

    pp = p.replace("%", "")
    pp = float(pp)
    return pp/100


main()
