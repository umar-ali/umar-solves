def Solve(N, S):
    
    #swap 
    oden = N % 2
    S = list(S)
    for i in range(0,N-1, 2):
        temp = S[i]
        S[i] = S[i + 1]
        S[i + 1]  = temp
    #ALPHA CIPHER
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    for i in range(N):
        c = S[i]
        S[i] = ALPHA[ 25 - ALPHA.find(c)]    
    res = ""
    for i in S:
        res += i
        
    return res
        
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        print(Solve(N, S))