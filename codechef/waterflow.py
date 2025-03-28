def Solve(W, X, Y, Z):
    unfilled = X - W
    waterflow = Y * Z 
    if unfilled > waterflow:
        return "unfilled"
    elif unfilled < waterflow:
        return "overflow"
        return "overflow"
    else:
        return "filled"
    
    

    
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        W, X, Y, Z = tuple(map(int, input().split()))
        print(Solve(W, X, Y, Z))