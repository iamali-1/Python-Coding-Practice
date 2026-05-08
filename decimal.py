from decimal import Decimal


def decimal(a: str, b: str):

    dec_a = Decimal(a)
    dec_b = Decimal(b)

    return dec_a + dec_b


print(decimal("0.1", "0.2"))
