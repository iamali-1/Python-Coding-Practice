# db = {}


# def signup():
#     username = input("Enter User Name: ")
#     password = input("Enter Password: ")
#     if username not in db:
#         db[username] = password
#         print(username, password)
#     return "Signup Successful!"


# print(signup())

# print(db)


# def login():
#     username = input("Enter User Name: ")
#     password = input("Enter Password: ")

#     if username in db and db[username] == password:
#         print(username, password)
#         return "Login Successful!"
#     else:
#         return "Wrong Credentials. Try Again With Correct Credentials."


# print(login())

# from datetime import date
# import random


# def family():
#     familiy_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
#     age = 0
#     birth_dates = {}
#     for name in familiy_names:
#         year = random.randint(1970, 2010)
#         month = random.randint(1, 12)
#         day = random.randint(1, 28)
#         if name not in birth_dates:
#             birth_dates[name] = date(year, month, day)
#     for key, value in birth_dates.items():
#         print(f"{key}: {value}")

#     user_input = input("Enter Name of a Person in Your Family: ")
#     if user_input in birth_dates:
#         today = date.today()
#         birthdate = birth_dates[user_input]
#         age = (
#             today.year
#             - birthdate.year
#             - (
#                 (today.month, today.day)
#                 < (
#                     birthdate.month,
#                     birthdate.day,
#                 )
#             )
#         )

#         print(f"{user_input}'s Age is {age} Years.")
#     else:
#         return "Name Not Found on the Family List."


# print(family())

# from pprint import pprint


# def get_rainfall():
#     rainfall_data = {}

#     while True:
#         city = input("Enter City Name: ").strip()

#         if city == "":
#             break
#         while True:
#             rainfall_input = (input("Enter Rainfall: ")).strip()
#             if rainfall_input.isdigit():
#                 rainfall = int(rainfall_input)
#                 break
#             else:
#                 print("Invalid Input. Numbers Only.")

#         if city in rainfall_data:
#             rainfall_data[city] += rainfall
#         else:
#             rainfall_data[city] = rainfall

#     for key, value in rainfall_data.items():
#         pprint(f"City: {key}, Rainfall: {value}mm.")


# print(get_rainfall())


# def dictduff(d1, d2):
#     final = {}
#     all_keys = set(d1.keys()).union(d2.keys())
#     print(all_keys)
#     for key in all_keys:
#         if d1.get(key) != d2.get(key):
#             final[key] = [d1.get(key), d2.get(key)]
#     return final


# print(dictduff({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 4}))


# def mergedict(*dicts):

#     result = {}
#     for d in dicts:
#         result.update(d)
#     return result


# print(mergedict({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 4, "e": 5}))


# def evenArguments(*arguments):
#     final = {}
#     keys = []
#     values = []
#     for even in range(len(arguments)):
#         if even % 2 == 0:
#             keys.append(arguments[even])
#         elif even % 2 != 0:
#             values.append(arguments[even])

#     for i in range(len(keys)):
#         final[keys[i]] = values[i]
#     return final


# print(evenArguments("a", 1, "b", 2, "c", 3))
import random


def decidingfunction(d1):
    output = {}
    for key, value in d1.items():
        output[key] = random.choice([True, False])
    return output


def dictpartition(d, f):
    d1 = {}
    d2 = {}
    result = f(d)
    for key, value in d.items():
        if result[key] is True:
            d1[key] = d[key]
        elif result[key] is False:
            d2[key] = d[key]
    return d1, d2


print(dictpartition({"a": 1, "b": 2, "c": 3, "d": 4}, decidingfunction))
