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


def plus_minus(numbers):
    total = numbers[0]
    for index in range(1,len(numbers)):
        if index % 2 == 1:
            total += numbers[index]
        else:
            total -= numbers[index]
    return total

print(plus_minus([10, 20, 30, 40, 50, 60]))
