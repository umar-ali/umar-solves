

def generateParenthesis(n:int) -> list[str]:
    out = []

    def dfs(oP:int, cP:int, s:str):
        """
        oP: no of Open Parens
        cP: no of Close Parens 
        s: string of parens
        """
        # when op equals to cp and their sum equals to 2*n i.e valid string, add to out
        if oP == cP and oP + cP == 2 * n:
            out.append(s)
            return
        
        #when oP is less than n, i.e, we haven't gone to depth of oP, we add open paren to S
        if oP < n:
            dfs(oP+1, cP, s+'(')
        
        #when cP is less than oP, i.e, let's match cp with oP, we add close paren to S
        if  cP < oP:
            dfs(oP, cP+1, s+')')
    
    #start with empty s, no parens
    dfs(0, 0, '')
    return out

if __name__ == "__main__":
    print(generateParenthesis(1)) #["()"]
    print(generateParenthesis(2)) #["()()", "(())"]
    print(generateParenthesis(3)) #["((()))","(()())","(())()","()(())","()()()"]
    print(generateParenthesis(4))