def main():
    vowel = input("Input: ")
    output = noVowel(vowel)
    print("Output:", output)

def noVowel(n):
    allvowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u", ]
    for x in allvowels:
        n = n.replace(x, "")
    return(n)

main()



