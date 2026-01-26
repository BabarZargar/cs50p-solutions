# we split the users input into three variables and then with some if elif statements we decide which operation the user is trying to do.

calculate = input("Expression: ")
x, y, z = calculate.split(" ")


if y == "+":
    print(float(x) + float(z))

elif y == "-":
    print(float(x) - float(z))

elif y == "*":
    print(float(x) * float(z))

elif y == "/":
    print(float(x) / float(z))

else:
    print("ERROR")
