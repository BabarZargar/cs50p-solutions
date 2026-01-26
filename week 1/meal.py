# we use if elilf statements to print the meal time

def main():
    time = input("What time is it? ")
    timenew = convert(time)

    if 7.0 <= timenew <= 8.0:
        print("breakfast time")

    elif 12.0 <= timenew <= 13.0:
        print("lunch time")

    elif 18.0 <= timenew <= 19.0:
        print("dinner time")

# we split the time and convert into a format that we can use easily in the main function for if elif statements

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60

if __name__ == "__main__":
   main()

