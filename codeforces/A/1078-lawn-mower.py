
def solve(n:int, w:int):
    d, m = divmod(n, w)
    return (w-1) * d  + m


def run():
    t = int(input())
    while t > 0:
        n, w = tuple(map(int, input().split(" ")))
        print(solve(n, w))
        t-=1

def samples():
    print(solve(9, 3))
    print(solve(13, 4))
    print(solve(15, 14))
    print(solve(20, 1))
    print(solve(1000, 42))


if __name__ == "__main__":
    run()
    #samples()

