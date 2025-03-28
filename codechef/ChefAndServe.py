def Solve(A, B, K):
    totalPoints = A + B
    if totalPoints % K == 0:
        nexturn = (totalPoints % K) % 2
        print(nexturn)
        
    else:
        turn = (totalPoints % (2*K))
        if turn < K:
            nexturn = 0
        if turn > K :
            nexturn = 1
        print(nexturn)
    if nexturn >0:
        return "cook"
    return "chef"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B, K = tuple(map(int, input().split()))
        print(Solve(A, B, K))