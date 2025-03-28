def Nineremainder(N):
    strN = str(N)
    sum = 0
    for i in strN:
        sum += int(i)
    return sum % 9



def Solution(N):
    rem = Nineremainder(N)
    pass

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        ans = Solution(N)
        print(f"Case #{i+1}: {ans}")
