
def solve(N, A):
    if N ==1:
        return "NO"
    return "yes"
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = tuple(map(int, input().split()))
        print(solve(N,K))