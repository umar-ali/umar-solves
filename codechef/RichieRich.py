import math
def Solve(A, B, X):
    need = B - A 
    Years = need // X
    return Years
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B, X = tuple(map(int, input().split()))
        print(Solve(A, B, X))