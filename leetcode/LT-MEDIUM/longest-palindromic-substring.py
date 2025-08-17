#dp
def longestPalindrome(s: str) -> str:
#set vars
    n = len(s)
    start, max_len = 0, 1

    #init dp table of size n * n
    dp = [[False] * n for _ in range(n)]

    #substring of len 1 is an palindrome
    for i in range(n):
        dp[i][i] = True
    
    #substring of len 2 with same char (like 'aa') is an palindrome
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            if max_len == 1:
                max_len = 2
                start = i
            
    #substring of len greater than 2
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i + k - 1
            # check s[i:j] is an palindrom
            # by checking s[i+1:j-1] is an palindrome and s[i] == s[j]
            # if yes update dp, maxlen, start if needed
            if  s[i] == s[j] and dp[i+1][j-1] :
                dp[i][j] = True
                if k > max_len:
                    max_len = k
                    start = i 
                

    return s[start:start+max_len]

if __name__ == "__main__":
    s = "babad"                       
    print(longestPalindrome(s))
                    
                



        