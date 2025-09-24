
def myAtoi(s:str) -> int:
    cleaned_str = s.strip()
    if len(cleaned_str) <= 0:
        return 0
    sign = 1
    if cleaned_str[0] in ["-", "+"]:
        if cleaned_str[0] == "-":
            sign = -1
        cleaned_str = cleaned_str[1:]

    num = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for c in cleaned_str:
        if c not in digits:
            break
        if sign == -1 and (num * 10 + int(c)) > 2 ** 31:
            print("bro")
            return 2 ** 31 * sign #handle maxing neg
        elif sign != -1 and (num * 10 + int(c)) > 2 ** 31 - 1:
            print("not you bro")
            return 2 ** 31 -1
        if num == 0:
            num += int(c)
        else:
            num = num * 10 + int(c)

    return num * sign 


if __name__ == "__main__":
    print(myAtoi("1234"))
    print(myAtoi("    -1234"))
    print(myAtoi("1337c0d3"))
    print(myAtoi("+1"))
    print(myAtoi("-2147483648"))






