def lowest(inp):
    low = list()
    for i in range(4):
        low.append(inp[0][i])
        for j in range(3):
            if inp[j][i] < low[i]:
                low[i] = inp[j][i]
    return lowest(inp)

            

def Solution(inp):
    print(lowest(inp))

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        inp = list()
        for p in range(3):
            inp.append(list(map(int, input().split())))
        Solution(inp)
        print(f"Case #{t}:")
