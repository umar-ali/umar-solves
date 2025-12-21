from collections import defaultdict

def minCost(s:str, cost:list[int]) -> int:
    # make the s of same char, with minimum deletion
    s2c = defaultdict(int)
    for s, c in zip(s, cost):
        s2c[s] += c 
    st = sorted(s2c.values(), reverse=True)
    return sum(st[1:])

print(minCost("aabaac", [1, 2, 3, 4, 1, 10]))


