def Solve(X, Y, Z):
    return (X-Y) * Z
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        X, Y, Z = tuple(map(int, input().split()))
        print(Solve(X, Y, Z))