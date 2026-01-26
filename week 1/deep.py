# main func asks the question gives it to normalize func then checks if the ans is right print yes otherwise prints no.

def main():
    ans = input("what is the answer to the life's greatest question? ")
    newans = normalize(ans)
    match newans:
        case "42" | "fortytwo":
            print("yes")
        case _:
            print("no")

# normalize func removes spaces and '-' and it also lowercases everything

def normalize(n):
    return(n).replace(" ", "").replace("-", "").lower()



main()
