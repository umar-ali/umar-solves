def Solve(n, a
    cnt = 0
    for i in a:
        if i & 1 == 0:
            cnt += 1
    return cnt
            
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
       n = int(input())
       a = list(map(int, input().split()))
       print(Solve(n, a))