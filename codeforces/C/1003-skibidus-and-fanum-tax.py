
def solve(n, a, b):
    for i in range(1,n):
        if a[i-1] > a[i]:
            if b-a[i-1] <= a[i]:
                print("nah")
                a[i-1] = b-a[i-1]
            elif b-a[i] >= a[i-1]:
                print("bro")
                a[i] = b-a[i]
    
    for i in range(1, n):
        if a[i-1] > a[i]:
            print("NO")
            return
    print("YES")
            
    

if __name__ == "__main__":
    t = int(input())
    while t:
        n, m = tuple(map(int, input().split()))
        a = list(map(int, input().split()))
        b = int(input()) #m = 1
        solve(n, a, b)
        t-=1