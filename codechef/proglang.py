def Solve(langs):
    A =set(langs[:2])
    if A == set(langs[2:4]):
        return 1
    elif A == set(langs[4:6]):
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        langs = list(map(int, input().split()))
        print(Solve(langs))