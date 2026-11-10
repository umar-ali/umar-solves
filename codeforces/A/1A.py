#A Theatre Square

def solve(n:int, m:int, a:int) -> int:
    l_tiles = (n + a - 1) // a #instead of import math; math.ceil(n, a)
    h_tiles = (m + a - 1) // a #instead of import math; math.ceil(m, a)

    return l_tiles * h_tiles


if __name__ == "__main__":
    n, m, a = tuple(map(int, input().split(" ")))
    print(solve(n, m, a))
