def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum():
      if 2 <= len(s) <= 6:
          if s[0:1].isalpha():

              return True


if __name__ == "__main__":
    main()
