
def isMatch(s:str, p:str) -> bool:
    pi = 0
    sj = 0
    
    while pi < len(p) and sj < len(s):
        if p[pi] == ".":
            sj+=1
            pi+=1
            continue

        if p[pi] == "*":
            if (p[pi-1] == s[sj] or p[pi-1] == "."):
                sj+=1
                continue
            else:
                pi+=1

        if p[pi] != s[sj]:
            return False
        else:
            sj += 1
            pi += 1

    return True




if __name__ == "__main__":
    print(isMatch("aa", "a"))
    print(isMatch("aa", "b*"))
    print(isMatch("ab", ".*"))
