# def pig_latin(word: str) -> str:
#     vowels = ["a", "e", "i", "o", "u"]
#     if word[0] in vowels:
#         word += "way"
#     else:
#         w = word[0]
#         word = word[1:]
#         word += w
#         word += "ay"
#     return word


# print(pig_latin("python"))

def pig_latin(word: str) -> str:

    small_vowels = ["a", "e", "i", "o", "u"]
    capital_vowels = ["A", "E", "I", "O", "U"]
    if word[0] in small_vowels:
        word += "way"
    elif word[0] in capital_vowels:
        word += "way"
        word = word.upper()

    else:
        w = word[0]
        word = word[1:]
        word += w
        word += "ay"
        if w.isupper():
            word = word.upper()

    return word


print(pig_latin("Python"))
