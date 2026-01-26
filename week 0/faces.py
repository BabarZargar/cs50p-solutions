# in the main function we will take input and trigger emote through printing input
def main():
    x = input("Hi ")
    print(emote(x))




# in the emote function we will simply replace the old emojis to the new ones and return
def emote(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

main()
