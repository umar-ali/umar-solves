def rank(P, Q):
    if P < Q:
        return 'P'
    elif P >  Q:
        return 'Q'
    else:
        return 'TIE'
        
def Solve(pA, pB, qA, qB):
    p = max(pA, pB)
    q = max(qA, qB)
    res = rank(p, q)
    return res

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        pA, pB, qA, qB = tuple(map(int, input().split()))
        print(Solve(pA, pB, qA, qB))