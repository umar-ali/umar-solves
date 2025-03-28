def Solve(N, X, Y):
   
   
	
if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        N, X, Y = tuple(map(int, input().split()))
        print(f"Case #{i}: {Solve(N, X, Y)}")