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


# def alternate_pig_latin(word: str) -> str:
#     vowels = {"a", "e", "i", "o", "u"}
#     found_vowels = [letter for letter in word.lower() if letter in vowels]

#     if len(found_vowels) >= 2:
#         return word + "way"

#     return word[1:] + word[0] + "ay"

# print(alternate_pig_latin("wine"))


# def pl_sentence(sentence: str) -> str:
#     vowels = ["a", "e", "i", "o", "u"]
#     new_word = None
#     splitted = sentence.split(" ")
#     new_splitted = []

#     for word in splitted:
#         w = word[0]
#         if w in vowels:
#             new_word = word + "way"
#             new_splitted.append(new_word)
#         elif w not in vowels:
#             new_word = word[1:] + w + "ay"
#             new_splitted.append(new_word)
#     new_string = " ".join(new_splitted)
#     return new_string


# print(pl_sentence("this is a test translation"))


def transpose(alphabets: list) -> list:
    split_words = [s.split() for s in alphabets]

    transposed = zip(*split_words)

    return [" ".join(words) for words in transposed]


print(transpose(["abc def ghi", "jkl mno pqr", "stu vwx yz"]))
