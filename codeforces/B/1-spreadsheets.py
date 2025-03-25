import re

# #R23C55 -> BC23
# r = "23"
# c = "53"
# out = ""
# print(f"{ALPHABHETS[int(c)/26-1]}{ALPHABHETS[int(c)%26-1]}{r}")

# #BC23 -> R23C55
# c = "BC"
# r = "23"
ALPHABHETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def num_to_alpha(num):
    alpha = ""
    while num:
        rem = num % 26
        alpha = ALPHABHETS[rem - 1] + alpha
        num = num // 26
    return alpha


def alpha_to_num(alpha):
    num = 0
    l = len(alpha)
    for i, c in enumerate(alpha, 1):
        num += (26 ** (l - i)) * (ALPHABHETS.find(c) + 1)
        print(num)
    return num


def convert(cell: str) -> str:
    if matched := re.match(r"R([1-9]+)C([1-9]+)", cell):
        C = int(matched.group(2))
        col = f"{num_to_alpha(C)}{matched.group(1)}"
        return col
    elif matched := re.match(r"([A-Z]+)([1-9]+)", cell):
        col = alpha_to_num(matched.group(1))
        return f"R{matched.group(2)}C{col}"
    return cell


if __name__ == "__main__":
    test_cases = int(input())
    while test_cases:
        cell = input()
        print(convert(cell))
        test_cases -= 1
