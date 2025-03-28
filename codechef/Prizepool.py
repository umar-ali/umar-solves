def Solve(X, Y):
    return X*10 + Y * 90
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        X, Y = tuple(map(int, input().split()))
        print(Solve(X, Y))