

def isHappy(n:int) -> bool:
    vis = set()

    while n != 1 and n not in vis:
        vis.add(n)
        sum_of_sqrs = 0
        while n > 0 :
            n, last = divmod(n, 10)
            sum_of_sqrs += last * last
        n = sum_of_sqrs
    return n == 1

if __name__ == "__main__":
    print(isHappy(19))
