def name_pyramid(name: str) -> str:
    n = ""
    for index, letters in enumerate(name):
        n += letters
        print(index, n)


name_pyramid("Ali")


def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)
hex_output()