#Vdates

def Solve(D, L, R):
    if D < L :
        return "Too Early"
    if L <= D <= R:
        return "Take second dose now"
    if D > R :
        return "Too Late"
    
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        D, L, R = tuple(map(int, input().split()))
        print(Solve(D, L, R))
        