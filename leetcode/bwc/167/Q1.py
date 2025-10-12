#Equal Score Substrings


# def scoreBalance(s:str) -> bool:
#     ln = len(s)
#     m = ln // 2
#
#     alpha = "*abcdefghijklmnopqrstuvwxyz"
#     alphaScore = {alpha[i]:i for i in range(len(alpha)) if alpha[i] != "*" }
#
#     scores = [alphaScore[c] for c in s]
#
#
#     l = scores[:m]
#     r = scores[m:]
#
#     lsm = sum(l)
#     rsm = sum(r)
#     # print(lsm, rsm)
#     if lsm == rsm:
#         return True
#
#     i = 1
#     while i <= m:
#         lx = sum(scores[m:m+i])
#         rx = sum(scores[m-i:m])
#         # print(i, m, lsm, rsm, lx, rx)
#         if lsm + lx == rsm - lx:
#             return True
#         if lsm - rx == rsm + rx:
#             return True
#         i+=1
#
#     return False

def scoreBalance(s:str) -> bool:
    alpha = "*abcdefghijklmnopqrstuvwxyz"
    alphaScore = {alpha[i]:i for i in range(len(alpha)) if alpha[i] != "*"}
    scores = [alphaScore[c] for c in s]
    
    total_score = sum(scores)
    mid, odd = divmod(total_score, 2)

    #can't split list whose total is an odd
    if odd:
        return False

    score = 0
    for s in scores:
        score+=s
        if score == mid:
            return True
    return False

  

if __name__ == "__main__":
    print(scoreBalance("adbc")) #True
    print(scoreBalance("bace")) #False
    print(scoreBalance("aab")) #True
    print(scoreBalance("aaa")) #False
    print(scoreBalance("abcdefghijk")) #False
    print(scoreBalance("abccabcba")) #True
    print(scoreBalance("abdcd")) #True
    print(scoreBalance("ecbdaa")) #True
    print(scoreBalance("acabcea")) #False

