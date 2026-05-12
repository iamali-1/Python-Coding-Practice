# def pig_latin(word: str) -> str:
#     vowels = 'aeiuoAEIOU'
#     is_capitalized = word[0].isupper()
#     word_lower = word.lower()
#     if word_lower[0] in vowels:
#         result = word_lower + 'way'
#     else:
#         result = word_lower[1:] + word_lower[0] + 'ay'

#     if is_capitalized:
#         result = result.capitalize()

#     return result


# print(pig_latin("Python"))


def alternate_pig_latin(word: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    found_vowels = [letter for letter in word.lower() if letter in vowels]

    if len(found_vowels) >= 2:
        return word + "way"

    return word[1:] + word[0] + "ay"



print(alternate_pig_latin("wine"))
