def Solve(X, Y):
    if Y > X:
        return "YES"
    return "NO"
    
if __name__ == "__main__":
    X, Y = tuple(map(int, input().split()))
    print(Solve(X, Y))