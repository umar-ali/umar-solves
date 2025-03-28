def Solve():
    img = input()
    img = img+input()
    freq = dict()
    for i in img:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i] = 1
    return freq

    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        print(Solve())