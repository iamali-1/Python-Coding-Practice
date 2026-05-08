def pig_latin(word: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels:
        word += "way"
    else:
        w = word[0]
        word = word[1:]
        word += w
        word += "ay"
    return word


print(pig_latin("python"))
