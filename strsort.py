def strsort(word: str) -> str:
    sorted = []
    for letter in word:
        sorted.append(letter)
    sorted.sort()
    return "".join(sorted)


print(strsort("octopus"))