def main():
    camel = input("camelCase: ")
    print("snake_case:", camel_to_snake(camel))

def camel_to_snake(camel):
    # create an empty str to store the result in it
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

main()
