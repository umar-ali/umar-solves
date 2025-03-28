"""Xor
"""
import math

def isPalindrome(A):
    p = A[::-1]
    if p == A :
        return True 
    else:
        return False
def Solve(N, A):
    count =0
    if isPalindrome(A):
        return count
    else:
        for i in range(N//2):
            j = N - i -1
            if A[i] != A[j]:
                count +=1
        return math.ceil(count/2)
        
              
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input()
        print(Solve(N, A))