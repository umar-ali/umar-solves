def reverse(x: int) -> int:
    rev_num = 0
    max_int32 = 2**31 - 1
    min_int32 = 2**31

    pos = x >= 0
    i = 0
    x = abs(x)
    while x != 0:
        lt_dig = x % 10
        x //= 10
        # print(num,lt_dig)
        if pos and (rev_num * 10) + lt_dig > max_int32:
            return 0
        if not pos and (rev_num * 10) + lt_dig > min_int32:
            return 0
        rev_num = (rev_num * 10) + lt_dig
        # print(rev_num)
    sign = 1 if pos else -1
    return rev_num * sign


if __name__ == "__main__":
    x = 123
    print(reverse(x=123))