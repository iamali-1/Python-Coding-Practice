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


def list_dicts(data):
    final = {}
    repeat = []
    for dictionaries in data:
        if isinstance(dictionaries, dict):
            for key, value in dictionaries.items():
                if key in final:
                    if not isinstance(final[key], list):
                        final[key] = [final[key]]
                    final[key].append(value)
                else:
                    final[key] = value
    return final


print(
    list_dicts(
        [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "city": "New York"},
            {"age": 30, "city": "London", "hobby": "Reading"},
        ]
    )
)
