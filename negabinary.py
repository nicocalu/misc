# negative base counting


def toNegabinary(i: int) -> str:
    """Decimal to negabinary"""

    if i == 0:
        digits = ["0"]

    else:
        digits = []

        while i != 0:
            i, remainder = divmod(i, -2)

            if remainder < 0:
                i, remainder = i + 1, remainder + 2

            digits.append(str(remainder))
    return "".join(digits[::-1])


def fromNegabinary(b: bytes) -> int:
    """Negabinary to Decimal"""
    if not isinstance(b, str):
        b = bin(b)

    bs = b[2::]

    if bs == "0":
        return 0

    else:
        s = 0

        ls = [(-2) ** i for i in range(len(bs))]

        for i in range(len(bs)):

            s += ls[i] * int(bs[len(bs) - 1 - i])

    return int(s)


def BtoNB(value: int) -> int:
    """decimal integer to integer in negabinary"""

    Schroeppel2 = 2863311530

    return (value + Schroeppel2) ^ Schroeppel2


print(BtoNB(10))
