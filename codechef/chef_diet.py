def Solve(N, K, A):
    remaining = 0
    for i in range(N):
        remaining += A[i]
        if remaining < K:
            return f"NO {i+1}"
        remaining -= K  
    return "YES"
        
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = tuple(map(int, input().split()))
        A = list(map(int, input().split()))
        print(Solve(N, K, A))