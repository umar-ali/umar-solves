
def checkZero(A):
    z = [0] * len(A)
    if z == A:
        return True
    return False
    
def sub(A, count = 0):
    if checkZero(A):
        return count
    
    
    
def Solve(N, A):
    count = 0
    if checkZero(A):
        return count
    A.sort()
    for i in range(N):
        for j in range(j, )    
            
            
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(Solve(N, A))