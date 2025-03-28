def Solve(X, Y, Z):
    totalMoney = X * 5 + Y * 10
    return totalMoney // Z
    
    
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        X, Y, Z = tuple(map(int, input().split()))
        print(Solve(X, Y, Z))