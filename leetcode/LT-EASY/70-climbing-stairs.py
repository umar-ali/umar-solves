
def _climb(n:int, m:dict = {}) -> int:
    if n <= 2:
        return n
    if n not in m:
        m[n] = _climb(n-1, m) + _climb(n-2, m)
    return m[n]

def climbStairs(n:int) -> int:
    return _climb(n)


if __name__ == "__main__":
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(4))
    print(climbStairs(5))
    print(climbStairs(44))

