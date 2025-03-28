def Solve():
    N, Q = tuple(map(int, input().split()))

    Dic = dict()
    for i in range(N-1):
        P, C = tuple(map(int, input().split()))
        mx = max(P, C)
        mn = min(P, C)
        if mn not in Dic.keys():
            Dic[mn] = [mx]
        else:
            Dic[mn].append(mx)

    Queries = []
    for q in range(Q):
        Queries.append(input())

    FullyFilled = set()
    halfFilled = set()
    for q in Queries:
        
    return 0


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        result = Solve()
        print(f"Case #{i}: {result}")