def Solve(N, L):
    temp = {}
    for i in L:
        if i not in temp:
            temp.append(i)
        else:
            temp.remove(i)
    return temp[0]
              
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        L = list()
        for i in range(N):
            L.append(int(input()))
        print(Solve(N, L))