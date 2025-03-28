

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False


def Solution(R,C):
    sol = list()
    for r in range(1,(2*R)+2):
        for c in range(1,(2*C)+2):
            if r<3 and c < 3:
                print('.',end='')
            elif isEven(r) and isEven(c):
                print('.',end='')
            elif not isEven(r) and isEven(c):
                print('-',end='')
            elif not isEven(r) and not isEven(c):
                print('+',end='')
            else:
                print('|',end='')
        print()
          







if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        R,C = tuple(map(int,input().split()))
        print(f"Case #{t}:")
        Solution(R, C)

