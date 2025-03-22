def solve(lv: int, kayaks: list[int], catamarans: list[int]) -> tuple[int]:
    maxi, k, c, s = 0, 0, 0, 0
    kayaks.sort()
    catamarans.sort()

    k = min(len(kayaks), v)
    for i in range(k):
        s += kayaks[i]
    c = min(len(catamarans), (v - k) // 2)
    for i in range(c):
        s += catamarans[i]

    if s > maxi:
        maxi = s
        bk = k
        bc = c

    while k and c < len(catamarans):
        k -= 1
        s -= kayaks[k]
        if (k + (c + 1) * 2) <= v:
            s += catamarans[c]
            c += 1
        if s > maxi:
            maxi = s
            bk = k
            bc = c
    return maxi, 0
    



if __name__ == "__main__":
    k = list()
    c = list()
    n, v = list(map(int, input().split()))
    while n:
        wv, vc = tuple(map(int, input().split()))
        if wv == 1:
            k.append(vc)
        if wv == 2:
            c.append(vc)
        n-=1
    print(v,k,c)
    max, opt = solve(v, k, c)
    print(f"{max}\n{opt}")

