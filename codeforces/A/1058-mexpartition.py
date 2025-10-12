
def solve(s:list[int]) -> int:
    s = sorted(list(set(s)))
    ln = len(s)
    mn = s[0]
    mx = s[ln-1]
    score = 0
    #when lowest is not 0, mex is 0
    if mn > 0: 
        return score
    #when all positive num exist with 1..ln, return mx + 1 that is next num
    if sum(s) == (ln * (ln -1))//2:
        score = mx + 1
    else:
        #find the first mex
        i = 0
        while i < ln - 1:
            if s[i+1] - s[i] > 1:
               score =  s[i] + 1
               break
            i+=1
    return score
        



if __name__ == "__main__":
    t = int(input())
    i = 0
    while i < t:
        _ = int(input())
        s = list(map(int, input().split(" ")))
        print(solve(s))
        i+=1
