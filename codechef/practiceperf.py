def Solve(P):
    count = 0
    for i in P:
        if i >= 10:
            count+=1
    return count
    
    
if __name__ == "__main__":
    P = list(map(int, input().split()))
    print(Solve(P))