def Solve(N, K, A):
    res = ""
    for i in range(N):
        if A[i] <= K:
            res += '1'
            K-= A[i]
        else:
            res += '0'
    return res
 
    
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = tuple(map(int, input().split()))
        A = list(map(int, input().split()))
        print(Solve(N, K, A))