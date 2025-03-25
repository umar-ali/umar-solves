#work smarter, not harder
import math

def solve():
    l,v_1, v_2 = tuple([int(x) for x in input().split()])
    tort_t = math.ceil(l/v_1)
    hare_t = math.ceil(l/v_2)
    #print(f"____{hare_t} {tort_t}_____")
    df_t = tort_t - hare_t
    if df_t >= 1:
        return abs(df_t - 1)
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        print(solve())


