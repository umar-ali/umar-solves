#max diff
def Solve(N, S):
    if S<= N:
        return S
    return N * 2 - S
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, S = tuple(map(int, input().split()))
        print(Solve(N, S)) 