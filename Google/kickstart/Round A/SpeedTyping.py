def Solution(I, P):
    for i in set(I):
        if i not in set(P):
            return "IMPOSSIBLE"

    if len(P) >len(I):
        i = 0
        j = 0
        count = 0
        while(i<len(I)):
            if I[i] == P[j]:
                i += 1
                j += 1
            else:
                while I[i] != P[j]:
                    j += 1
                    if j<len(P):
                        count+=1
                    else:
                        return "IMPOSSIBLE"
            if i == len(I):
                count = len(P) - len(I)

        return count

    elif len(P) == len(I):
        i = 0
        while(i<len(I)):
            if I[i] != P[i]:
                return "IMPOSSIBLE"
            i += 1 
        return 0

    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        I = input()
        P = input()
        c = i + 1
        ans = Solution(I, P)
        print(f'Case #{c}: {ans}')



