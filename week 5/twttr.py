def main():
     vowel = input("Input: ")
     output = shorten(vowel)
     print("Output:", output)


def shorten(word):
    allvowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u",]
    for x in allvowels:
        word = word.replace(x, "")
    return(word)


if __name__ == "__main__":
    main()
