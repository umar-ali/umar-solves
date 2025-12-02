

def mySqrt(x:int) -> int:
    n = 0
    while n * n <= x:
        n+=1
    return n  - 1


if __name__ == "__main__":
    print(mySqrt(25)) #5
    print(mySqrt(35)) #5
    print(mySqrt(8)) #2
    print(mySqrt(4)) #2
