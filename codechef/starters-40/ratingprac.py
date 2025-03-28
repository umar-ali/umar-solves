def Solve(N, D):
    for i in range(1,N):
        if D[i-1] > D[i]:
            return "No"
    return "Yes"
        
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        D = list(map(int, input().split()))
        print(Solve(N, D))