def Solve(N, Nums):
    return max(Nums)
    
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        Nums = list(map(int, input().split()))
        print(Solve(N, Nums))