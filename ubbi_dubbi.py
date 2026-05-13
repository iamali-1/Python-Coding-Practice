def ubbi_dubbi(word: str) -> str:
    final = ""
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            final += "ub"

        final += letter

    return final


print(ubbi_dubbi("milk"))
