

def isMatch(s:str, p:str) -> bool:

    # if p is empty, then result is True if s i empty, otherwise False
    if not p:
        return not s

    #Checking a char match in pattern
    #f_match is true when s is non-empty and p[0] is either s[0] or '.' 
    f_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:]) # matching pattern succeeding *
                or f_match and isMatch(s[1:], p)) #for matching <c>*, f_match matched one and let's match s[1..sn]
    else:
        return f_match and isMatch(s[1:], p[1:]) #Handling all other cases.. i.e., we know f_match(0,0) what about [1..sn], [1..pn]

if __name__ == "__main__":
    print(isMatch("aa", "a"))   #False
    print(isMatch("aa", "b*"))  #False
    print(isMatch("ab", ".*"))  #True
    print(isMatch("abcccd", "abc*d"))  #True
