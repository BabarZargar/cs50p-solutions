# main func takes input puts it into normalize func then checks the return value with if and elif statements to see if it starts with hello etc.

def main():
    str = input("Greeting: ")
    new_str = normalize(str)
    if new_str.startswith("hello"):
        print("$0")
    elif new_str.startswith("h"):
        print("$20")
    else:
        print("$100")

# normalize func strips whitespaces from the left and also lowercases everything
def normalize(n):
    return(n).lstrip().lower()



main()
