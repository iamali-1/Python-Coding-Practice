# def even_odd_sums(lists):
#     final = []
#     odd = 0
#     even = 0
#     for num in range(len(lists)):
#         if num % 2 == 0:
#             even += lists[num]
#         elif num % 2 != 0:
#             odd += lists[num]
#     final.append(even)
#     final.append(odd)
#     return final


# print(even_odd_sums([10, 20, 30, 40, 50, 60]))


# def plus_minus(numbers):
#     total = numbers[0]
#     for index in range(1,len(numbers)):
#         if index % 2 == 1:
#             total += numbers[index]
#         else:
#             total -= numbers[index]
#     return total

# print(plus_minus([10, 20, 30, 40, 50, 60]))


# def mysum_bigger_than(*items):
#     first = items[0]
#     result = 0
#     for item in items:
#         if item > first:
#             result += item
#     return result


# print(mysum_bigger_than(10, 5, 20, 30, 6))


# def sum_numeric(*items):
#     result = 0
#     for item in items:
#         try:
#             result += int(item)
#         except (ValueError, TypeError):
#             continue
#     return result


# print(sum_numeric(10, 20, "a", "30", "bcd"))


# def list_dicts(data):
#     final = {}

#     for dictionaries in data:
#         if isinstance(dictionaries, dict):
#             for key, value in dictionaries.items():
#                 if key in final:
#                     if not isinstance(final[key], list):
#                         final[key] = [final[key]]
#                     final[key].append(value)
#                 else:
#                     final[key] = value
#     return final


# print(
#     list_dicts(
#         [
#             {"name": "Alice", "age": 25},
#             {"name": "Bob", "city": "New York"},
#             {"age": 30, "city": "London", "hobby": "Reading"},
#         ]
#     )
# )


# def lengthOfLastWord(s: str) -> str:
#     s = s.strip().split()
#     return len(s[-1])


# print(lengthOfLastWord("luffy is still joyboy"))
# print(lengthOfLastWord("Hello World"))
# print(lengthOfLastWord("   fly me   to   the moon  "))

# import operator
# from pprint import pprint

# def sorted_countries(items):
#     return (sorted(items,key=operator.itemgetter('name')))


# pprint(
#     sorted_countries(
#         [
#             {"name": "Canada", "size": 9984670, "population": 38250000},
#             {"name": "Italy", "size": 301340, "population": 59110000},
#             {"name": "United Kingdom", "size": 242495, "population": 67220000},
#             {"name": "France", "size": 551695, "population": 67390000},
#             {"name": "Germany", "size": 357022, "population": 83200000},
#             {"name": "Japan", "size": 377975, "population": 125700000},
#             {"name": "United States", "size": 9833517, "population": 331900000},
#         ]
#     )
# )


# def positive_negative(*nums):
#     return sorted([abs(n) for n in nums])

# print(positive_negative(-2,3,4,5,6,7,-5))


# import operator


# def vowels_sort(mostVowels):
#     vowels = "aeiou"
#     count = 0
#     count_list = []

#     for word in mostVowels:
#         for letter in word:
#             if letter in vowels:
#                 count += 1
#         count_list.append({"name": word, "count": count})
#         count = 0
#     return sorted(count_list, key=operator.itemgetter("count"))


# print(vowels_sort(["luffy", "is", "still", "joyboy"]))

# import operator


# def list_of_lists(items):
#     count = 0
#     count_list = []
#     for item in items:
#         for nums in item:
#             count += nums
#         count_list.append({"list": item, "count": count})
#         count = 0
#     return sorted(count_list, key=operator.itemgetter("count"))


# print(list_of_lists([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]))

# import operator


# def list_of_lists(items):
#     count = 0
#     count_list = []
#     for item in items:
#         count += len(item)
#         count_list.append({"list": item, "count": count})
#         count = 0
#     return sorted(count_list, key=operator.itemgetter("count"))


# print(list_of_lists([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]))


# def reverseVowels(s: str) -> str:
#     vowels = "aeiouAEIOU"
#     occurence = []
#     for letter in range(len(s) - 1, -1, -1):
#         if s[letter] in vowels:
#             occurence.append(s[letter])

#     result = ""
#     for letter in s:
#         if letter in vowels:
#             # pop from occurrence to reverse vowels
#             result += occurence.pop(0)
#         else:
#             result += letter

#     return result


# print(reverseVowels("leetcode"))
from collections import Counter

WORDS = ["this", "is", "an", "elementary", "test", "example"]


def most_repeating_letter_count(word):
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


print(most_repeating_word(WORDS))
