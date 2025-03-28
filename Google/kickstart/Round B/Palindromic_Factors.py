import math
def isPalindrome(num):
    s =str(num)
    rev = s[::-1]
    return s == rev
            

def Solution(A):
    count = 0
    fact = set()
    i = 1
    while i*i <= A:
        if A%i == 0 :
            fact.add(i)
            fact.add(A//i)
        i += 1
    for j in fact:
        if isPalindrome(j):
            count += 1
    return count
   
if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        A = int(input())
        result = Solution(A)
        print(f"Case #{i}: {result}")





