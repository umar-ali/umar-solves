


def solve(n, A, B):
    setA = set(A)
    setB = set(B)
    setC = set()
    for i in setA:
        for j in setB:
            if (c:= i+j) not in setC:
                setC.add(c)
            if len(setC) >= 3:
                print("YES")
                return
    print("NO")
            
if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        solve(n, A, B)
        t-=1