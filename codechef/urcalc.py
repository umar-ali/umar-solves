def Solve(A, B, C):
    if C == '+':
        return A+B 
    elif C == '-':
        return A-B 
    elif C == '*':
        return A*B 
    else:
        return A/B
if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = input()
    print(Solve(A, B, C))