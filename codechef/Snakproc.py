def Solve(L, S):
    new_S = ""
    res = 'Valid'
    for i in S:
        if i!= '.':
            new_S += i 
            
    L = len(new_S)
    if L > 0:
        if new_S[0] == 'T' or new_S[L-1] == 'H':
            return 'Invalid'
        
        for i in range(L):
            if (i%2 ==0 and new_S[i] =='T') or (i%2 == 1 and new_S[i] == 'H'):
                return "Invalid"
    return res
    
   

if __name__ == "__main__":
    R = int(input())
    for r in range(R):
        L = int(input())
        S = input()
        print(Solve(L, S))
        

