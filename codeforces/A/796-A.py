def Solve(x):
    y = 1
    while True:
        print(x & y , x ^ y)
        if x & y > 0 and x ^ y >0:
            return y 
        y+=
        

        

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x = int(input())
        print(Solve(x))