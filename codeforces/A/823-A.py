def Solve():
    n, c = tuple(map(int, input().split()))
    if n<=1 and n>=100:
        return 0
    a = list(map(int, input().split()))
    m1 = t1 = len(a)
    m2 = 0
    cnt = dict()
    orbits = set(a)
    
    for i in orbits:
        cnt[i] = a.count(i)
    for i in orbits:
        if cnt[i] > 1:
            m2+=c
            t1-=cnt[i]
    if m2+t1 > m1:
        return m1
    return m2+t1
    

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        print(Solve())