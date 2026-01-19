
def hammingWeight(n:int) -> int:
    return n.bit_count()

if __name__ =="__main__":
    print(hammingWeight(5)) #2
    print(hammingWeight(11)) #3
