from datetime import date
import inflect
import sys


def main():
    dob = input("Date of Birth: ")
    minutes = get_minutes(dob)
    words = convert_to_words(minutes)
    print(words)


def get_minutes(dob):
    try:
        birth = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    delta = today - birth
    return delta.days * 24 * 60


def convert_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
