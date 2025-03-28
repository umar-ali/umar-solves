def Solve(X, Y):
    count = 0
    if X != Y:
        if X > Y:
            diff = X - Y
            d = diff % 2
            count += (diff//2) + d
            if d:
                count += 1            
        if Y > X :
            diff = Y - X
            count+=diff
            
    return count

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        X, Y = tuple(map(int, input().split()))
        print(Solve(X, Y))