#Lockpicking Chef
def ispresent(s, k):
    return k in s

def diff(S, K):
    res = 0
    S = list(S)
    K = list(K)
    for s, k in tuple(zip(S, K)):
        res +=abs(int(s)-int(k))
        print(res)
    return res

def solve():
   N, M = tuple([int(x) for x in input().split()])
   S = input()
   K = input()
   if ispresent(S, K): return 0
   diff_dic = {}
   ans = min([diff(S[i:i+M], K) for i in range(len(S)-1)])
   
   return ans
   """for i in range(len(s)-2):
    sub = S[i:i+2]
    diff_dic[(i, i+2)] = 
   """



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        print(solve())