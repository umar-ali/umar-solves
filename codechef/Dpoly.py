

def Solve(N, A):
    if N <=1:
        return 0
    i = N-1
    while A[i] == 0:
        if i == 0:
            break
        i -= 1
    return i
    
        
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(Solve(N, A))