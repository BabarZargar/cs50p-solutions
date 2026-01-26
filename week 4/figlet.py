from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 1:
    str = input("Input: ")
    r = random.choice(list)
    figlet.setFont(font=r)

    print(figlet.renderText(str))

elif len(sys.argv) == 3:

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":

        f = sys.argv[2]

        if f not in list:
            print("Invalild usage")
            sys.exit(1)

        else:
            figlet.setFont(font=f)
            str = input("Input: ")
            print(figlet.renderText(str))


    else:
        print("Invalid usage")
        sys.exit(1)

elif len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit(1)




