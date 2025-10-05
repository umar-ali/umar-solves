

def isMatch(s:str, p:str) -> bool:

    memo = {} #Memoize the intermediate results

    def dp(i:int, j:int) -> bool:
        #check at end of pattern
        if (i,j) not in memo:
            #if j is at end, matched if  i should be at it end otherwise not matched
            if j == len(p):  
                ans = i == len(s)
            else:
                #Checking char at i against char at pat j
                f_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j+1] == '*':
                    ans = (dp(i, j + 2) # matching pattern succeeding *
                            or f_match and dp(i+1, j)) #for matching <c>*, f_match matched one and let's match s[1..sn]
                else:
                    ans = f_match and dp(i+1, j+1) #Handling all other cases.. i.e., we know f_match(0,0) what about [1..sn], [1..pn]
            memo[i,j] = ans
        return memo[i,j]
    return dp(0,0)

if __name__ == "__main__":
    print(isMatch("aa", "a"))   #False
    print(isMatch("aa", "b*"))  #False
    print(isMatch("ab", ".*"))  #True
    print(isMatch("abcccd", "abc*d"))  #True
