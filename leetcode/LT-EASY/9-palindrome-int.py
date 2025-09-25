


def isPalindrome(x:int) -> bool:
    s = str(x)
    ln = len(s)
    if ln == 1:
        return True
    m = ln // 2 
    l = s[:m]
    r = s[m+(ln % 2):][::-1]
    return l == r


if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(1))
    print(isPalindrome(12))
    print(isPalindrome(1221))
    print(isPalindrome(1245))
    print(isPalindrome(-121))

