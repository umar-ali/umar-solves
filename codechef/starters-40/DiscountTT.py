def Solve(N, A, X, Y):
    B_Coupon = sum(A)
    A_Coupon = 0
    for i in range(N):
        if A[i] > Y:
            A_Coupon += A[i]-Y
    if B_Coupon > A_Coupon + X:
        return "COUPON"
    else:
        return "NO COUPON"
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, X, Y = tuple(map(int, input().split()))
        A = list(map(int, input().split()))
        print(Solve(N,A, X, Y))
       