


#3498
#bi-153
def reverseDegree(s:str)->int:
    ALPHABHETS = "abcdefghijklmnopqrstuvwxyz"
    lk_table = dict()
    for i, c in enumerate(ALPHABHETS[::-1], 1):
        lk_table[c] = i
    sums = 0
    for j, k in enumerate(s, 1):
        sums+= (j * lk_table[k])
    return sums




if __name__ == "__main__":
    s = input()
    print(reverseDegree(s))