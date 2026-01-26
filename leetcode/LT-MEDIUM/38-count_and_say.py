


def countAndSay(n:int) -> int:
    res = "1"
    for i in range(n-1):
        j = 1
        count = 1
        newRes = ""
        while j < len(res):
            if res[j] == res[j-1]:
                   count += 1
            else:
                newRes += (str(count) + res[j-1])
                count = 1
            j += 1
        res  = newRes + str(count) + res[j-1]
    return res


if __name__ == "__main__":
    for i in range(1, 6):
        print(countAndSay(i))

