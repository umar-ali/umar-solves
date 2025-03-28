import math
def Score(Rs, Rh, MN):
    sc = 0

    for i in range(len(MN)):
        d = math.sqrt(MN[i][0]**2 + MN[i][1]**2)
        print(d)
        if Rs - Rh <= d <= Rs+Rh:
            sc+=1

    return sc
def Solve():
    Rs, Rh = tuple(map(int, input().split()))
    N = int(input())
    Ns = list()
    for i in range(N):
        Ns.append(tuple(map(int, input().split())))
        
    M = int(input())   
    Ms = list()
    for i in range(M):
        Ms.append(tuple(map(int, input().split())))
    scn = Score(Rs,Rh,Ns)
    scm = Score(Rs,Rh,Ms)
    return str(scn)+" "+str(scm)
    
        
if __name__ == "__main__":
    tt = int(input())
    for i in range(1,tt+1):
        print(f"Case #{i}: {Solve()}")