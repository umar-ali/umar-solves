
def solve(S):
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            print(1)
            return
    print(len(S))

if __name__ == "__main__":
    n = int(input())
    while n:
        solve(input())
        n-=1