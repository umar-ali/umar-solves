

def solve(s:str, numRows:int) -> str:
    res = ""
    slots = [[] for _ in range(numRows)]
    n = len(s)
    i = 0
    v = numRows * 2 - 2
    start = 0
    if n == 1 or numRows == 1 : return s
    while start < n:
        for b, c in enumerate(s[start:start+numRows]):
            slots[b].append(c)
            i+=1
        for k, c in enumerate(s[start+numRows:start+v]):
            slots[numRows-k-2].append(c)
            i+=1
        start+=v
    for i in slots:
        res+="".join(i)
    return res
    

if __name__ == "__main__":
    testcases = (
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
    )
    
    solutions = (
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
        "AB"
    )
    
    for tc, soln in zip(testcases, solutions):
        got = solve(*tc) 
        assert got == soln, "Failed"