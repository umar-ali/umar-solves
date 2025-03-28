#Beat the odds
def isEven(n):
    return n%2 == 0
def Solve(N, A):
    cnt = 0
    for i in range(N):
        if A[i] & 1:
            cnt +=1
    return min(N-(N-cnt), N - cnt)
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(Solve(N, A))