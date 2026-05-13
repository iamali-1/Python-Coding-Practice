# def strsort(word: str) -> str:
#     sorted = []
#     for letter in word:
#         sorted.append(letter)
#     sorted.sort()
#     return "".join(sorted)


# print(strsort("octopus"))

def strsort(text: str) -> str:
    result = []
    words = text.lower().split(" ")
    
    for word in words:
        sorted_word = "".join(sorted(word)).capitalize()
        result.append(sorted_word)

    return ", ".join(result)

print(strsort("Tom Dick Harry"))
