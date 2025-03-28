def Solve(N):
    return int(N/2) + 1

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(Solve(N))
    