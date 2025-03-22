
def solve(n, bins):
    for b in bins:
        cnt = 0
        for d in range(len(b)):
            if int(b[d]): cnt+=1
            while d < len(b) and  int(b[d]) :
                d+=1
                continue
        print(cnt)



if __name__ =="__main__":
    n = int(input())
    bins = [input() for i in range(n)]
    solve(n,bins)